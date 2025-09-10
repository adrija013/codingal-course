import turtle

sc = turtle.Screen()

sc.bgcolor("pink")
sc.setup(700,700)

turtle.title("Welcome to turtle Window")

board = turtle.Turtle()

n= 10
for i in range(0,n):
    board.forward(100)
    board.left(360/n)

turtle.done()    