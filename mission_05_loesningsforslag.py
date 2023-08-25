# Mission 5
import turtle
import rover

# Opsætning af banen.
# Vinduet er 400x400
# Koordinatet (0,0) ligger i midten af vinduet.
screen = turtle.Screen()
screen.setup(400, 400)
screen.bgpic("./img/mission_05.png")

# Initialisering af roveren
rover = rover.Rover()
rover.hideturtle()
rover.speed(0)
rover.penup()
rover.goto(-160, -135)
rover.pendown()
rover.showturtle()
rover.speed(3)  # Farten kan sættes fra 1 til 10 (0 betyder instantant)

# Herfra skal I selv indsætte instruktioner til roveren
# Stardardmissionen
rover.left(17)
rover.forward(230)
rover.left(45)
rover.forward(150)
rover.left(107)
rover.forward(205)
rover.left(80)
rover.forward(250)
# Standardmission avanceret løsning
# fremadvaerdier = [230, 150, 205, 250]
# vinkelvaerdier = [17, 45, 107, 80]
# while vinkelvaerdier:
#     rover.left(vinkelvaerdier.pop(0))
#     if fremadvaerdier:
#         rover.forward(fremadvaerdier.pop(0))
# Bonusmissionen
# rover.left(17)
# rover.forward(200)
# rover.right(90)
# rover.circle(30, 225)
# rover.right(90)
# rover.forward(75)
# rover.right(90)
# rover.circle(45, 287)
# rover.right(90)
# rover.forward(130)
# rover.right(90)
# rover.circle(30, 260)
# rover.right(90)
# rover.forward(220)
# Bonusmission avanceret løsning
# rover.left(17)
# fremadvaerdier = [200, 75, 130, 220]
# cirkelvæerdier = [(30, 225), (45, 287), (30, 260)]
# while fremadvaerdier:
#     rover.forward(fremadvaerdier.pop(0))
#     if cirkelvæerdier:
#         rover.right(90)
#         rover.circle(*cirkelvæerdier.pop(0))  # * betyder udpakning af tuplen
#         rover.right(90)
# Denne linje skal I ikke gøre noget med.
# Den skal bare være den sidste linje
screen.mainloop()
