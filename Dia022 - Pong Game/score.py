from turtle import Turtle

class Score(Turtle):
    def __init__(self, x,y):
        super().__init__()
        self.score = 0

        self.color("white")
        self.penup()
        self.goto(x,y)
        self.write(f'{self.score}', align= "center",font=("Arial", 15, "normal"))
        self.hideturtle()
       
    def update_score(self):
        self.write(f'{self.score}', align= "center", font=("Arial", 15, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.write(f'{self.score}', align= "center", font=("Arial", 15, "normal"))
        