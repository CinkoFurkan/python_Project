from turtle import Turtle
move_distance = 20
up = 90
down = 270
right = 0
left = 180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x_position = 0

        for i in range(3):
            segment = Turtle(shape="square")
            segment.color("blue")
            segment.penup()
            segment.goto(x_position, 0)
            self.segments.append(segment)
            x_position -= 20

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def reset(self):
        for seg in self.segments:
            seg.goto(-1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]



