from turtle import Turtle
import time
ALIGN = 'Center'
FONT = 'arial', 20, 'normal'


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f'Score : {self.score}', align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align=ALIGN, font=FONT)
        time.sleep(2)
        quit()

