from turtle import Turtle
import os
import pandas as pd
from tabulate import tabulate

ALIGNMENT = "center"
FONT = ("Arial", 26, "bold")
INSTRUCTIONS_ALIGNMENT = "Left"
INSTRUCTIONS_FONT = ('Arial', 13, 'normal')
INSTRUCTIONS_COLOR = "white"

file_path = "C:\\Users\\User\\PycharmProjects\\Snake_game\\snake_scores.csv"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        (self.highest_score, self.highest_scorer_name) = self.load_scores()
        self.penup()
        self.color(INSTRUCTIONS_COLOR)
        self.scores_on_screen()
        self.hideturtle()
        self.run_game()

    def save_scores(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        data = {
            "Name": [self.highest_scorer_name],
            "Highest Score": [self.highest_score],
        }
        df = pd.DataFrame(data)

        if not os.path.exists(file_path):
            df.to_csv(file_path, index=False)
        else:
            # Append the new high score to the existing DataFrame
            existing_df = pd.read_csv(file_path)
            existing_df = existing_df._append(df, ignore_index=True)
            existing_df.to_csv(file_path, index=False)

    @staticmethod
    def load_scores():
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            if not df.empty:
                highest_score = df["Highest Score"].max()
                highest_scorer_name = df.loc[df["Highest Score"].idxmax()]["Name"]
                return highest_score, highest_scorer_name
        return 0, 0

    def get_highest_score(self):
        return self.highest_score

    def scores_on_screen(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Current Score: {self.score}", align='center', font=('Arial', 20, 'normal'))
        self.goto(320, 275)
        self.write(f"Highest Score: {self.highest_score}", align='right', font=INSTRUCTIONS_FONT)
        self.goto(320, 255)
        self.write(f' Set by: {self.highest_scorer_name}', align='right', font=INSTRUCTIONS_FONT)

    def reset_score(self, player_name):
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.highest_scorer_name = player_name
            self.save_scores()
        self.score = 0
        self.scores_on_screen()

    def add_score(self):
        self.score += 1
        self.scores_on_screen()

    def game_over(self):
        self.goto(0, 50)
        self.color("Red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        df = pd.read_csv(file_path)
        self.goto(0, 0)
        self.color(INSTRUCTIONS_COLOR)
        self.write("TOP SCORERS", align='center', font=INSTRUCTIONS_FONT)
        self.goto(0, -80)
        self.color(INSTRUCTIONS_COLOR)
        top_scores = df.nlargest(3, "Highest Score")

        # Convert the top_scores DataFrame to a formatted table string
        top_scores_str = tabulate(top_scores, showindex=False, tablefmt="plain")
        self.write(top_scores_str, align='center', font=('Arial', 14, 'bold'))

    def new_highest_score_greeting(self):
        self.goto(0, 160)
        self.color("blue")
        self.write("Congratulations!", align='center', font=('ubuntu', 18, 'normal'))
        self.goto(0, 135)
        self.write("\nNew Highest Score!!", align='center', font=('ubuntu', 18, 'normal'))

    def player_name(self, player_name):
        self.highest_scorer_name = player_name
        self.color(INSTRUCTIONS_COLOR)
        self.save_scores()
        self.scores_on_screen()

    def run_game(self):
        self.goto(-320, -270)
        self.write("move - arrow keys", align=INSTRUCTIONS_ALIGNMENT, font=INSTRUCTIONS_FONT)
        self.goto(-320, -290)
        self.write("space/resume - pause", align=INSTRUCTIONS_ALIGNMENT, font=INSTRUCTIONS_FONT)
        self.goto(-320, 270)

    def increase_score(self):
        self.score += 1
        self.scores_on_screen()
        self.run_game()
