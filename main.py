import turtle
import random
import time

# Game settings
screen = turtle.Screen()
screen.title("Catch the Turtle")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Turtle object (game character)
game_turtle = turtle.Turtle()
game_turtle.shape("turtle")
game_turtle.color("red")
game_turtle.penup()  # Prevent drawing
game_turtle.speed(0)  # Instant movement

# Score and timer
score = 0
time_limit = 30
start_time = time.time()

# Display the score
score_board = turtle.Turtle()
score_board.hideturtle()
score_board.penup()
score_board.goto(0, 260)
score_board.write(f"Score: {score}  Time: {time_limit}", align="center", font=("Arial", 16, "normal"))

# Move the turtle to a new position
def move_to_new_position():
    x = random.randint(-280, 280)  # Random x-coordinate within screen boundaries
    y = random.randint(-280, 280)  # Random y-coordinate within screen boundaries
    game_turtle.goto(x, y)

# Function triggered when the turtle is clicked
def on_turtle_click(x, y):
    global score
    score += 1
    move_to_new_position()
    update_score()

# Update the score and timer
def update_score():
    global time_limit
    remaining_time = int(time_limit - (time.time() - start_time))
    score_board.clear()
    score_board.write(f"Score: {score}  Time: {remaining_time}", align="center", font=("Arial", 16, "normal"))

# End the game
def end_game():
    game_turtle.hideturtle()
    score_board.clear()
    score_board.write(f"Game Over! Final Score: {score}", align="center", font=("Arial", 20, "bold"))

# Bind the click event
game_turtle.onclick(on_turtle_click)

# Game loop
while True:
    remaining_time = int(time_limit - (time.time() - start_time))
    if remaining_time <= 0:
        end_game()
        break
    move_to_new_position()
    time.sleep(1)  # Turtle moves every 1 second
    update_score()

screen.mainloop()
