import turtle

def square(turtle):
    for i in range(4):
        turtle.speed(1)
        turtle.fd(100)
        turtle.right(90)

bob = turtle.Turtle()
square(bob)

# In the browser, you need to use the following rather than turtle.mainloop()
turtle._Screen().mainloop()