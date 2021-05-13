import turtle
a,b=0,0
turtle.bgcolor("black")
turtle.speed(0)
turtle.pencolor("blue")
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
while True:
    turtle.forward(a)
    turtle.right(b)
    a+=6
    b+=6
    if b==204:
        break
#turtle.close()
