from manim import *


class Diagram(Scene):
    def construct(self):
        pass


class GreenTheoremVisual(Scene):
    CONFIG = {
        "color_list": ['#e22b2b', '#e88e10', '#eae600', '#88ea00',
                       '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078'],
        "prop": 0
    }

    def construct(self):
        axes_config = {"x_min": -5,
                       "x_max": 5,
                       "y_min": -5,
                       "y_max": 5,
                       "z_axis_config": {},
                       "z_min": -1,
                       "z_max": 1,
                       "z_normal": DOWN,
                       "num_axis_pieces": 20,
                       "light_source": 9 * DOWN + 7 * LEFT + 10 * OUT,
                       "number_line_config": {
                           "include_tip": False,
                       },
                       }
        r_config = {"x_min": -3,
                    "x_max": 3,
                    "y_min": 0,
                    "y_max": 0.01,
                    "z_axis_config": {},
                    "z_min": -1,
                    "z_max": 1,
                    "z_normal": DOWN,
                    "num_axis_pieces": 20,
                    "light_source": 9 * DOWN + 7 * LEFT + 10 * OUT,
                    "number_line_config": {
                        "include_tip": False,
                    },
                    }

        axes = Axes(**axes_config)
        f = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP, lambda x, y: np.array([y, x]), prop=0)
              for x in np.arange(-5, 5, 1)
              for y in np.arange(-5, 5, 1)
              ]
        )

        field = VGroup(axes, f)
        field.scale(0.6)

        c = ParametricFunction(
            self.func,
            t_min=-3,
            t_max=3,
        )
        c.set_stroke(opacity=0.75)
        label = TextMobject("C")
        label.shift(2 * LEFT)
        label.scale(2)

        curve = VGroup(label, c)
        curve.scale(0.6)

        r_axes = Axes(**r_config)
        c2 = ParametricFunction(
            self.line_evaluated,
            t_min=-3,
            t_max=3,
            color=RED
        )
        func = VGroup(r_axes)
        func.shift(3 * DOWN + 2 * LEFT)

        self.play(ShowCreation(field))
        self.wait()

        self.play(Write(curve))
        self.wait()

    def calc_field_color(self, point, f, prop=0.0, opacity=None):
        x, y = point[:2]
        func = f(x, y)
        magnitude = math.sqrt(func[0] ** 2 + func[1] ** 2)
        func = func / magnitude if magnitude != 0 else np.array([0, 0])
        func = func / 1.5
        v = int(magnitude / 10 ** prop)
        index = len(self.color_list) - 1 if v > len(self.color_list) - 1 else v
        c = self.color_list[index]
        v = Vector(func, color=c).shift(point)
        if opacity:
            v.set_fill(opacity=opacity)
        return v

    @staticmethod
    def func(t):
        return np.array([
            2 * np.arctan(t),
            t,
            0
        ])