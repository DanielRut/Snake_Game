from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("snake_head_right.gif")
        self.head.state = []

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segments(position)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head.shape("snake_head_up.gif")

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head.shape("snake_head_down.gif")

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.shape("snake_head_left.gif")

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head.shape("snake_head_right.gif")

    def add_segments(self, position):
        new_segment = Turtle("snake_segment.gif")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # add new segment to the snake.
    def extend(self):
        self.add_segments(self.segments[-1].position())

    def pause(self):
        if self.head.state == "active":
            self.head.state = "pause"
        else:
            self.head.state = "active"

