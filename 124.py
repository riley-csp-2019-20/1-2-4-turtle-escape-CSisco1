import turtle as trtl
import random as rand




def reset_button():
    t = trtl.Turtle()
    t.pensize(10000)
    t.pencolor("white")
    t.forward(200)
    t.back(400)
    t.forward(200)
    def draw_door():
        t.pencolor("white")
        t.forward(gapsize)
        t.pencolor("black")

    wn = trtl.Screen() 
    l = 0
    w = 45
    t.pencolor("black")
    t.left(90)
    t.pensize(15)
    t.speed(100000000)
    wall_width = 15
    gapsize = 23
    #draw the maze outline
    for i in range(w):
        l += wall_width
        t.pendown()
        t.forward(l)
        t.left(90)
    t.left(90)
    #random gaps and barriers
    for i in range(w - 7):
        c = l - 55
        indent = rand.randint(35,c)
        barrier_spot = rand.randint(35,c)
        t.forward(barrier_spot)
        t.forward(gapsize + 5)
        t.right(90)
        t.forward(gapsize + 4) 
        t.back(gapsize + 5)
        t.left(90)
        t.forward(l - gapsize - barrier_spot - 5) 
        t.right(180)
        t.forward(l)
        t.right(180)
        t.forward(indent)
        draw_door()
        t.forward(5)
        t.forward(l - indent - gapsize - 5)
        t.right(90)
        l = l - 15
    #random gaps for the inner area, no barriers
    for i  in range(3):
        indent = rand.randint(20,(l - 20))
        t.forward(indent)
        t.pencolor("white")
        t.forward(gapsize)
        t.pencolor("black") 
        t.forward(l - indent - gapsize)
        t.right(90)
        l = l - 15
    toortle = trtl.Turtle()
    toortle.shape("turtle")
    toortle.pencolor("blue")
    toortle.goto(-15,0)
    toortle.pensize(15)




    def up():
        toortle.setheading(90)
        toortle.forward(15)
        wn.listen()
    def down():
        toortle.setheading(270)
        toortle.forward(15)
        wn.listen()
    def left():
        toortle.setheading(180)
        toortle.forward(15)
        wn.listen()
    def right():
        toortle.setheading(360)
        toortle.forward(15)
        wn.listen()

    wn.onkeypress(up, "w")
    wn.onkeypress(left, "a")
    wn.onkeypress(down, "s")
    wn.onkeypress(right, "d")
    wn.listen()
wn = trtl.Screen()
reset_button()
wn.onkeypress(reset_button, "p")

wn.listen()
wn.mainloop()