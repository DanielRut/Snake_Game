import time
import tkinter
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard


new_game = True


screen = Screen()

while new_game:
    screen.clear()
    screen.setup(width=700, height=600)
    screen.cv._rootwindow.resizable(False, False)
    screen.bgpic("background.png")
    screen.title("Snake Game")
    screen.tracer(0)
    img = tkinter.Image("photo", file="snake.ico")
    turtle._Screen._root.iconphoto(True, img)
    screen.register_shape("apple.gif")
    screen.register_shape("snake_head_up.gif")
    screen.register_shape("snake_head_down.gif")
    screen.register_shape("snake_head_right.gif")
    screen.register_shape("snake_head_left.gif")
    screen.register_shape("snake_segment.gif")
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.pause, "space")

    game_is_on = True
    try:
        while game_is_on:
            screen.update()
            time.sleep(20/(scoreboard.score+100))
            if snake.head.state == "active":
                pass
            else:
                snake.move()

        # Detect collision with food.
            if snake.head.distance(food) < 15:
                food.refresh()
                snake.extend()
                scoreboard.increase_score()


            def when_game_end():
                scoreboard.game_over()
                if scoreboard.score > scoreboard.highest_score:
                    # congrats highest scorer in display screen
                    scoreboard.new_highest_score_greeting()
                    winner_name = screen.textinput(title="Highest scorer!",
                                                   prompt="Enter your name:")

                    # at the same time  display the name of the winner and the highest score together
                    scoreboard.player_name(winner_name)
                    scoreboard.game_over()

        # Detect collision with wall.
            if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
                scoreboard.game_over()
                when_game_end()
                play_again = (screen.textinput(title="Play again?", prompt="yes/no"))
                if play_again == "yes":
                    new_game = True
                else:
                    new_game = False
                game_is_on = False

        # Detect collision with tail.
            for segment in snake.segments[1:]:
                if snake.head.distance(segment) < 10:
                    scoreboard.game_over()
                    when_game_end()
                    play_again = (screen.textinput(title="Play again?", prompt="yes/no"))
                    if play_again == "yes":
                        new_game = True
                    else:
                        new_game = False
                    game_is_on = False
    except:
        break

screen.mainloop()
