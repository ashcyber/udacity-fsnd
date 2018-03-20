"""
    udacity fsnd
    lesson 4 practice problem
    turtle graphics 

"""


import turtle

def draw_square_circle():
    window = turtle.Screen()
    window.bgcolor("red")

    t = turtle.Turtle()
    t.shape('turtle')
    t.color('green')
    t.speed(10)
    for j in range(0,36):
        t.right(10)
        for i in range(4):  
            t.forward(100)
            t.right(90)


    window.exitonclick()




def wheel():
    window = turtle.Screen()
    window.bgcolor("red")

    t = turtle.Turtle()
    t.shape('turtle')
    t.color('green')
    t.speed(10)
    for j in range(0,36):
        t.right(10)
        for i in range(3):  
            t.forward(100)
            t.right(120)


    window.exitonclick()
    


wheel()
