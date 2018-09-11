import turtle

COLOR = ((0,0,0),(51,0,0),(51,0,0),(102,51,0),(102,51,0),(132,51,0),(132,51,0),(0,204,0))

def tree(level):
	turtle.pencolor(COLOR[level])
	turtle.pendown()
	turtle.pensize(9 - level)
	turtle.forward(100-(10 * level))
	turtle.penup()

	p = turtle.pos()
	h = turtle.heading()

	level = level+1

	if level < 8:
		turtle.left(30)
		tree(level)

		turtle.goto(p)
		turtle.setheading(h)

		turtle.right(30)
		tree(level)

turtle.reset()
turtle.colormode(255)

turtle.speed(0)
turtle.penup()
turtle.goto(0,-300)
turtle.setheading(90)


tree(0)

turtle.exitonclick()