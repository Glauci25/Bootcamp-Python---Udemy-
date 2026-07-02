from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.color("black")
        self.penup()
        self.goto(0,270)
        self.write(f'Score: {self.score}', align= "center",font=("Arial", 12, "normal"))
        self.hideturtle()

    def win(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align= "center", font=("Arial", 12, "normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align= "center",font=("Arial", 12, "normal"))

