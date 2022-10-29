from turtle import Screen
import random
import turtle

t = turtle.Turtle()
turtle.colormode(255)

# Drawing a square
# for _ in range(4):
#     t.forward(100)
#     t.left(90)

# Drawing - - - - - using penup and pendown tool
# for _ in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(5)
#     t.pendown()

# Drawing Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon and Decagon all in one place
# for i in range(3, 11):
#     t.color(random.random(), random.random(), random.random())
#     for _ in range(i):
#         t.forward(100)
#         t.right(360/i)

# Draw a Random Walk


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)


# directions = [0, 90, 180, 270]
# t.pensize(10)
# t.speed("fastest")
# for i in range(200):
#     t.color(random_color())
#     t.forward(50)
#     t.setheading(random.choice(directions))


# Draw a Spirograph
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


t.speed("fastest")
for _ in range(72):
    t.color(random_color())
    t.circle(100)
    t.left(5)
    # t.setheading(t.heading()+5)


screen = Screen()
screen.exitonclick()
