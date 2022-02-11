# Snake game by uisng turtle
# created by rafursimanto03065@gmail.com

import turtle
from turtle import Turtle
import time
import random

delay = 0.1

# Getting high_score from file
fh = open("high_score.txt", "r")
for line in fh:
    score, value = line.strip().split(":")
fh.close()

# setting score
high_score = int(value)
score = 0

# Setup screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("light green")
wn.setup(width=600, height=600)
wn.tracer(0)  # stop update


class BodyPart(Turtle):
    def __init__(self, Shape, Color, direction):
        # Turtle.__init__()  # reference of parent class
        super().__init__()  # reference of parent class
        self.Shape = Shape
        self.shape(self.Shape)
        self.Color = Color
        self.color(self.Color)
        self.direction = direction
        self.speed(0)  # Animation speed
        self.penup()  # remove drawing  while moving
        self.goto(0, 0)


class SnakeHead(BodyPart):
    def __init__(self, Shape, Color, direction):
        super().__init__(Shape, Color, direction)  # reference of parent class
        # BodyPart.__init__(self, Shape, Color, direction)  # reference of parent class
        self.speed(0)  # Animation speed
        self.penup()  # remove drawing  while moving
        self.goto(0, 0)

    def go_up(self):
        if self.direction != "down":
            self.direction = "up"

    def go_down(self):
        if self.direction != "up":
            self.direction = "down"

    def go_right(self):
        if self.direction != "left":
            self.direction = "right"

    def go_left(self):
        if self.direction != "right":
            self.direction = "left"

    """def go_pauss(self):
        self.direction = "space"""

    def move(self):
        if self.direction == "right":
            x = self.xcor()
            self.setx(x+20)
        if self.direction == "left":
            x = self.xcor()
            self.setx(x-20)
        if self.direction == "up":
            y = self.ycor()
            self.sety(y+20)
        if self.direction == "down":
            y = self.ycor()
            self.sety(y-20)
        """if self.direction == "space":
            x = self.xcor()
            y = self.ycor()
            self.goto(x, y)"""


# Snake head
head = SnakeHead("square", "black", "stop")

# Snake food
food = BodyPart("circle", "red", "stop")
food.goto(0, 100)

count = 0
segments = []


# Pen
pen = BodyPart("square", "white", "stop")
pen.hideturtle()
pen.goto(0, 260)


def write():
    pen.write("Score: {} High Score: {}".format(score, high_score),
              align="center", font=("Arial", 24, "normal"))


# score save
def save_score(high_score):
    fh = open("high_score.txt", "w")
    fh.write("High_score: "+str(high_score))


# keyboard binding
wn.listen()
wn.onkeypress(head.go_up, "Up")
wn.onkeypress(head.go_down, "Down")
wn.onkeypress(head.go_left, "Left")
wn.onkeypress(head.go_right, "Right")
# wn.onkeypress(head.go_pauss, "space")


# main gameloop
while True:
    wn.update()

    # check collison with food
    if head.distance(food) < 20:

        # setting color green
        if (count+1) % 7 == 0:
            food.color("green")

        if count % 7 == 0 and count != 0:
            score += 50
            # reset color:
            food.color("red")

        else:
            # increase score
            score += 10

        # move food to random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 270)
        food.goto(x, y)

        # add new segment
        Color = "gray"
        if count % 2 == 0:
            Color = "white"
        new_segment = BodyPart("square", Color, "stop")
        segments.append(new_segment)

        if score > high_score:
            high_score = score

        # increase speed
        delay -= 0.001

        pen.clear()
        write()
        # increase count
        count += 1

    # for end segments appended to reverse border
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # for 1st segment:
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # collison with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segments
        segments.clear()

        # reset score
        score = 0

        # reset count
        count = 0

        # reset color
        food.color("red")

        # reset speed
        delay = 0.1

        # Reset the score screen
        pen.clear()
        write()

        # save score
        save_score(high_score)

    head.move()

    # Check collison with body segment
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            print("stop")
            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segments
            segments.clear()

            # reset score
            score = 0

            # reset count
            count = 0

            # reset color
            food.color("red")

            # reset speed
            delay = 0.1

            # Reset the score screen
            pen.clear()
            write()

            # save score
            save_score(high_score)

    time.sleep(delay)

wn.mainloop()
