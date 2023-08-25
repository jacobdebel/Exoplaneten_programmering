# Mission 2
import turtle
import rover

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
rover.speed(3)  # Farten kan sættes fra 1 til 10 (0 betyder instantant)

# Herfra skal I selv indsætte instruktioner til roveren
for _ in range(4):
    rover.forward(330)
    rover.left(90)
# Denne linje skal I ikke gøre noget med.
# Den skal bare være den sidste linje
screen.mainloop()
