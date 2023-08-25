# Mission 7
import turtle
import rover
import random

# Opsætning af banen.
# Vinduet er 400x400
# Koordinatet (0,0) ligger i midten af vinduet.
screen = turtle.Screen()
screen.setup(400, 400)
screen.bgpic("./img/mission_1.gif")

# Initialisering af roveren
rover = rover.Rover()
rover.hideturtle()
rover.speed(0)
rover.penup()
rover.goto(-165, -165)
rover.pendown()
rover.showturtle()
rover.speed(10)  # Farten kan sættes fra 1 til 10 (0 betyder instantant)

# Herfra skal I selv indsætte instruktioner til roveren
# rover.left(random.uniform(-90, 90))
while True:
    rover.forward(10)
    if (
        rover.xcor() >= 200
        or rover.xcor() <= -200
        or rover.ycor() >= 200
        or rover.ycor() <= -200
    ):
        rover.backward(20)
        rover.left(random.uniform(0, 360))
    # Bonusmission
    if rover.distance((35, 90)) < 65:
        rover.backward(20)
        rover.left(random.uniform(0, 360))


# Denne linje skal I ikke gøre noget med.
# Den skal bare være den sidste linje
screen.mainloop()
