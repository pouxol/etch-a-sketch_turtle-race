import turtle as t

tony = t.Turtle()
screen = t.Screen()


def move_forward():
    tony.forward(10)


def move_backward():
    tony.backward(10)


def turn_right():
    tony.right(10)


def turn_left():
    tony.left(10)


def reset():
    tony.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)

screen.exitonclick()
