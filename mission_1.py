# [[file:Mars_rover_simulering.org::+begin_src python -n :exports both :results output :eval never-export :comments link :tangle mission_1.py][No heading:1]]
import turtle

screen = turtle.Screen()
screen.setup(400, 400)
screen.bgpic("mars_path_1.png")
# screen.addshape("rover.gif")

# rover_image = turtle.Shape("image", "./rover.gif")
screen.addshape("rover.gif")

rover_image = turtle.Shape("image", "rover.gif")

t = turtle.Turtle()
t.speed(1)
t.shape("classic")
t.tiltangle(-20)
t.forward(100)
screen.mainloop()

# No heading:1 ends here
