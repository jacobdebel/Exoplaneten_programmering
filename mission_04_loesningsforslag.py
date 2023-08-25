# Mission 04
import turtle
import rover

# Opsætning af banen.
# Vinduet er 400x400
# Koordinatet (0,0) ligger i midten af vinduet.
screen = turtle.Screen()
screen.setup(400, 400)
screen.bgpic("./img/mission_04.png")

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
# 330
# 47
for _ in range(3):
    rover.forward(330)
    rover.left(90)

for i in range(1, 7):
    for _ in range(2):
        rover.forward(330 - i * 47)
        rover.left(90)
# rover.forward(330)
# rover.left(90)
# rover.forward(330)
# rover.left(90)
# rover.forward(330)
# rover.left(90)
# rover.forward(330 - 47)
# rover.left(90)
# rover.forward(330 - 47)
# rover.left(90)
# rover.forward(330 - 2 * 47)
# rover.left(90)
# rover.forward(330 - 2 * 47)
# rover.left(90)
# rover.forward(330 - 3 * 47)
# rover.left(90)
# rover.forward(330 - 3 * 47)
# rover.left(90)
# rover.forward(330 - 4 * 47)
# rover.left(90)
# rover.forward(330 - 4 * 47)
# rover.left(90)
# rover.forward(330 - 5 * 47)
# rover.left(90)
# rover.forward(330 - 5 * 47)
# rover.left(90)
# rover.forward(330 - 6 * 47)
# rover.left(90)
# rover.forward(330 - 6 * 47)

# Denne linje skal I ikke gøre noget med.
# Den skal bare være den sidste linje
screen.mainloop()
