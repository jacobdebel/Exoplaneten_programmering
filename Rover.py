import turtle

screen = turtle.Screen()
screen.setup(400, 400)

body_color = "#f54e4e"
wheel_color = "#810202"


class Rover(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(1)
        s = turtle.Shape("compound")
        body = (
            (0, 0),
            (11, 0),
            (11, 42),
            (-11, 42),
            (-11, 0),
        )
        s.addcomponent(body, body_color, wheel_color)
        wheel_1 = (
            (-11, 2),
            (-11, 12),
            (-16, 12),
            (-16, 2),
        )
        wheel_2 = (
            (-11, 16),
            (-11, 26),
            (-16, 26),
            (-16, 16),
        )
        wheel_3 = (
            (-11, 30),
            (-11, 40),
            (-16, 40),
            (-16, 30),
        )
        wheel_4 = (
            (11, 2),
            (11, 12),
            (16, 12),
            (16, 2),
        )
        wheel_5 = (
            (11, 16),
            (11, 26),
            (16, 26),
            (16, 16),
        )
        wheel_6 = (
            (11, 30),
            (11, 40),
            (16, 40),
            (16, 30),
        )
        s.addcomponent(wheel_1, wheel_color, wheel_color)
        s.addcomponent(wheel_2, wheel_color, wheel_color)
        s.addcomponent(wheel_3, wheel_color, wheel_color)
        s.addcomponent(wheel_4, wheel_color, wheel_color)
        turtle.register_shape("myshape", s)
        self.shape("myshape")


rover = Rover()
rover.goto(20, 0)
turtle.mainloop()
