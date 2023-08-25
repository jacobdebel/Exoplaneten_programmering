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
rover.pendown()
rover.showturtle()
rover.speed(3)  # Farten kan sættes fra 1 til 10 (0 betyder instantant)

# Herfra skal I selv indsætte instruktioner til roveren
# Stardardmissionen
# Koordinater (-120, -20) , (20, -125) , (100 , 120)
# Kører til det øverste krater
rover.left(8)
rover.forward(170)
rover.right(35)
rover.forward(100)
# Skriver E'et
rover.left(27)
rover.forward(15)
rover.backward(15)
rover.right(90)
rover.forward(20)
rover.left(90)
rover.forward(15)
rover.backward(15)
rover.right(90)
rover.forward(20)
rover.left(90)
rover.forward(15)
rover.backward(15)
# Kører til det nederste krater
rover.right(40)
rover.forward(55)
rover.right(85)
rover.forward(200)
# Skriver A'et
rover.left(50)
rover.forward(30)
rover.backward(30)
rover.right(50)
rover.forward(20)
rover.left(122)
rover.forward(15)
rover.backward(15)
rover.right(122)
rover.forward(15)
# Kører til det mellemste krater
rover.right(40)
rover.forward(80)
rover.right(77)
rover.forward(105)
rover.right(132)
# Skriver S'et
rover.circle(15, 180)
rover.circle(-15, 180)
# Kører tilbage til start
rover.left(123)
rover.forward(170)
rover.right(110)

# rover.right(68)
# rover.forward(155)
# rover.right(112)
# rover.circle(10, 180)
# rover.circle(-10, 180)
# Bonusmissionen
# Denne linje skal I ikke gøre noget med.
# Den skal bare være den sidste linje
screen.mainloop()
