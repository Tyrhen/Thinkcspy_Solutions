import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Handling Keypresses!")
wn.bgcolor("ivory4")
tess = turtle.Turtle()
jess = turtle.Turtle()
ness = turtle.Turtle()


def draw_housing():
    """creates housing for the lights"""
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


def light_positions(turtle, color, pos, hide=0):
    """positions lights in the housing"""
    if hide == 1:
        turtle.hideturtle()
    turtle.penup()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(pos)
    turtle.shape("circle")
    turtle.shapesize(3)
    turtle.fillcolor(color)


def dimmer_switch(turtle, color):
    """dims a traffic light via fillcolor of thr turtle"""
    turtle.fillcolor(color + "4")


def brighter_switch(turtle, color):
    """brightens a traffic light via fillcolor of the turtle"""
    turtle.fillcolor(color + "1")


def advance_state_machine():
    """cycles through the states in a traffic light sequence"""
    global state_num

    if state_num == 0:
        brighter_switch(jess, "orange")
        dimmer_switch(ness, "red")
        dimmer_switch(tess, "green")
        state_num = 1

    elif state_num == 1:
        brighter_switch(ness, "red")
        dimmer_switch(jess, "orange")
        dimmer_switch(tess, "green")

        state_num = 2

    else:
        brighter_switch(tess, "green")
        dimmer_switch(ness, "red")
        dimmer_switch(jess, "orange")

        state_num = 0


state_num = 0
draw_housing()

light_positions(tess, "green1", 50)
light_positions(jess, "orange4", 120)
light_positions(ness, "red4", 190)

wn.onkey(advance_state_machine, "space")
wn.listen()
wn.mainloop()
