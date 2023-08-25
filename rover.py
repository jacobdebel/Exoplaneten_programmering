import turtle

body_color = "#f54e4e"
wheel_color = "#810202"


class Rover(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(1)
        self.color(wheel_color)
        self.pensize(4)
        s = turtle.Shape("compound")
        body = (
            (0, 0),
            (11, 0),
            (11, 42),
            (-11, 42),
            (-11, 0),
        )
        s.addcomponent(body, body_color, wheel_color)
        front = (
            (-7, 42),
            (7, 42),
            (0, 50),
        )
        s.addcomponent(front, wheel_color, wheel_color)
        wheels = []
        for i in range(3):
            wheel_left_side = (
                (-11, 2 + 14 * i),
                (-11, 2 + 14 * i + 10),
                (-16, 2 + 14 * i + 10),
                (-16, 2 + 14 * i),
            )
            wheels.append(wheel_left_side)
            wheel_right_side = (
                (11, 2 + 14 * i),
                (11, 2 + 14 * i + 10),
                (16, 2 + 14 * i + 10),
                (16, 2 + 14 * i),
            )
            wheels.append(wheel_right_side)

        for wheel in wheels:
            s.addcomponent(wheel, wheel_color, wheel_color)
        turtle.register_shape("rover", s)
        self.shape("rover")
