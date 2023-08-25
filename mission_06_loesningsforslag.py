# Mission 06
import turtle
import rover

# Opsætning af banen.
# Vinduet er 400x400
# Koordinatet (0,0) ligger i midten af vinduet.
screen = turtle.Screen()
screen.setup(400, 400)
screen.bgpic("./img/mission_06.png")

# Initialisering af roveren
rover = rover.Rover()
rover.hideturtle()
rover.speed(0)
rover.penup()
rover.goto(-160, 160)
rover.dot(5)
rover.goto(-120, -20)
rover.dot(5)
rover.goto(20, -125)
rover.dot(5)
rover.goto(100, 120)
rover.dot(5)
rover.pendown()
rover.showturtle()
rover.speed(3)  # Farten kan sættes fra 1 til 10 (0 betyder instantant)

# Herfra skal I selv indsætte instruktioner til roveren
# Stardardmissionen
# Bonusmissionen
# Denne linje skal I ikke gøre noget med.
# Den skal bare være den sidste linje
screen.mainloop()
