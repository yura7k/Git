import random
import turtle

paint = turtle.Pen()

paint.speed(1)

turtle.bgcolor("light blue")
paint.pencolor("blue")
paint.width(3)

distance = 650

while distance > 0:
    trip = random.randint(1, distance)
    paint.forward(trip)
    if trip // 2 == 0:
        paint.left(random.randint(50, 120))
    else:
        paint.right(random.randint(50, 120))
    distance -= trip