import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Handling Keypresses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
jess = turtle.Turtle()
ness = turtle.Turtle()


def draw_housing():
    """creates the housing for the traffic lights"""
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
    """ replicates the light positions in a traffic light"""
    if hide == 1:
        turtle.hideturtle()
    turtle.penup()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(pos)
    turtle.shape("circle")
    turtle.shapesize(3)
    turtle.fillcolor(color)


def advance_state_machine():
    """advances through the states in a traffic light sequence"""
    global state_num

    if state_num == 0:
        jess.showturtle()
        ness.hideturtle()
        tess.hideturtle()
        state_num = 1
        wn.ontimer(advance_state_machine, 3000)

    elif state_num == 1:
        ness.showturtle()
        tess.hideturtle()
        jess.hideturtle()
        state_num = 2
        wn.ontimer(advance_state_machine, 3000)

    else:
        tess.showturtle()
        jess.hideturtle()
        ness.hideturtle()
        state_num = 0
        wn.ontimer(advance_state_machine, 3000)


state_num = 0
draw_housing()

light_positions(tess, "green", 50)
light_positions(jess, "orange", 120, 1)
light_positions(ness, "red", 190, 1)

advance_state_machine()
wn.mainloop()
