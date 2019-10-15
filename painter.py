from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        pass


class Revolution(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        f1 = FunctionGraph(lambda x: 1/x, x_min=0.1)
        f2 = FunctionGraph(lambda x: 1/x, x_max=-0.1, x_min=-10)
        func = VGroup(f1, f2)
        func2 = FunctionGraph(lambda x: 1/x, x_min=1)

        surface = ParametricSurface(
            self.surface,
            u_min=1,
            u_max=10,
            v_min=0,
            v_max=0.001,
            checkerboard_colors=**COLOR_MAP,
            fill_color=YELLOW,
            stroke_color=YELLOW
        )

        self.play(Write(func), Write(axes))
        self.wait()

        self.play(Transform(f1, func2), Uncreate(f2), Write(surface))
        self.wait()

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.remove(f1)
        self.begin_ambient_camera_rotation(rate=0.04)
        self.play(
            UpdateFromAlphaFunc(surface, self.update_f),
            rate_func=linear,
            run_time=2
        )

        self.play(Uncreate(axes), surface.center)
        self.wait(5)

    def update_f(self, c, dt):
        a = interpolate(0.1, 2*PI, dt)
        s = ParametricSurface(
            self.surface,
            u_min=1,
            u_max=10,
            v_min=0,
            v_max=a,
            checkerboard_colors=[],
            color=YELLOW,
            fill_color=YELLOW,
        )
        c.become(s)

    @staticmethod
    def surface(u, v):
        return np.array([
            u,
            (1/u)*np.cos(v),
            (1/u)*np.sin(v)
        ])


class Volume(ThreeDScene):
    def construct(self):
        surface = ParametricSurface(
            self.func,
            u_min=1,
            u_max=10,
            v_min=0,
            v_max=2*PI,
            checkerboard_colors=[],

        )
        surface.center()

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(surface))
        self.wait()

        surface.set_fill(opacity=0.5)
        surface.set_stroke(opacity=0.5)
        self.wait()

    @staticmethod
    def func(u, v):
        return np.array([
            u,
            (1/u)*np.cos(v),
            (1/u)*np.sin(v)
        ])



class Horn(ThreeDScene):
    def construct(self):
        surface = ParametricSurface(
            self.func,
            u_min=1,
            u_max=10,
            v_min=0,
            v_max=2*PI,
            checkerboard_colors=[],

        )
        surface.center()

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(surface))
        self.wait()

    @staticmethod
    def func(u, v):
        return np.array([
            u,
            (1/u)*np.cos(v),
            (1/u)*np.sin(v)
        ])
