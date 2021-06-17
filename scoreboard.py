from turtle import  Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 1
        self.goto(-280, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=("Courier", 24, "normal"))
    def increase_level(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 16, "bold"))