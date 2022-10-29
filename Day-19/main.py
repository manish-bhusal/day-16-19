from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def anti_clockwise():
    tim.left(45)


def clockwise():
    tim.right(45)


def reset_screen():
    tim.reset()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=anti_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=reset_screen, key="c")

screen.exitonclick()
