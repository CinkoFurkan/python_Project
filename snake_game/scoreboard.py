from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()

    def scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.color("red")
        self.hideturtle()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(f"{self.high_score}"))
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.scoreboard()

    def read_high_score(self):
        with open("data.txt") as data:
            high_score = int(data.read())
            return high_score









