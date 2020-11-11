import turtle
turtle.setup(400,500)
wn = turtle.Screen()
wn.title('Handling Keypresses!')
wn.bgcolor('ivory4')
tess = turtle.Turtle()
pensize = 5
tess.pensize(pensize)

def forward():
    """move the turtle forward by an increment"""
    tess.forward(30)

def left():
    """turn the turtle 45 degrees to the left"""
    tess.left(45)
def right():
    """turn the turtle 45 degrees to the right"""
    tess.right(45)

def terminate():
    """terminate the program"""
    wn.bye()

def color_red():
    """turn turtle color red"""
    tess.color('red')

def color_green():
    """turn turtle color green"""
    tess.color('green')

def color_blue():
    """turn turtle color blue"""
    tess.color('DodgerBlue')

def pen_increase():
    """increase pensize of turtle in range 1 to 20"""
    global pensize
    pensize = pensize + 1
    if pensize > 20:
        tess.pensize(pensize-1)
    else:
        tess.pensize(pensize)


def pen_decrease():
    """decrease pensize of turtle in range 1 to 20"""
    global pensize
    pensize = pensize - 1
    if pensize < 1:
        tess.pensize(pensize+1)
    else:
        tess.pensize(pensize)
    
    
wn.onkey(forward,'Up')
wn.onkey(left,'Left')
wn.onkey(right,'Right')
wn.onkey(terminate,'q')
wn.onkey(color_red,'r')
wn.onkey(color_green,'g')
wn.onkey(color_blue,'b')
wn.onkey(pen_increase,'=')
wn.onkey(pen_decrease,'-')

        
wn.listen()
wn.mainloop()
