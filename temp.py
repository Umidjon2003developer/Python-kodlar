import turtle

def draw_cristiano_ronaldo():
    window = turtle.Screen()
    window.bgcolor("white")

    # Create a turtle instance
    ronaldo = turtle.Turtle()
    ronaldo.speed(2)

    # Head
    ronaldo.fillcolor("tan")
    ronaldo.begin_fill()
    ronaldo.circle(100)
    ronaldo.end_fill()

    # Eyes
    ronaldo.penup()
    ronaldo.goto(-35, 150)
    ronaldo.pendown()
    ronaldo.dot(25, "black")
    ronaldo.penup()
    ronaldo.goto(35, 150)
    ronaldo.pendown()
    ronaldo.dot(25, "black")

    # Mouth
    ronaldo.penup()
    ronaldo.goto(-20, 120)
    ronaldo.pendown()
    ronaldo.left(45)
    ronaldo.circle(30, 90)

    # Hair
    ronaldo.penup()
    ronaldo.goto(-100, 170)
    ronaldo.pendown()
    ronaldo.right(15)
    for _ in range(6):
        ronaldo.forward(200)
        ronaldo.right(150)

    # Body
    ronaldo.penup()
    ronaldo.goto(-50, -100)
    ronaldo.pendown()
    ronaldo.forward(100)
    ronaldo.left(90)
    ronaldo.forward(200)
    ronaldo.left(90)
    ronaldo.forward(100)

    # Legs
    ronaldo.left(90)
    ronaldo.forward(200)
    ronaldo.left(90)
    ronaldo.forward(50)
    ronaldo.left(90)
    ronaldo.forward(200)

    # Arms
    ronaldo.left(90)
    ronaldo.forward(50)
    ronaldo.left(90)
    ronaldo.forward(150)
    ronaldo.right(90)
    ronaldo.forward(50)
    ronaldo.right(90)
    ronaldo.forward(150)

    # Cleanup
    ronaldo.penup()
    ronaldo.hideturtle()

    # Keep the window open until it's closed by the user
    window.mainloop()

# Draw Cristiano Ronaldo
draw_cristiano_ronaldo()
