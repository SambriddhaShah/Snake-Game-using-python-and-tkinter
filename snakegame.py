from tkinter import *
import random


# keeping the constants that we will use through-out the game, will not change and have all capital letter name
GAME_HEIGHT = 700
GAME_WIDTH = 700
SPEED = 500
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


# Defining all the classes and functions that we need for tha game
class snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            # our snake will appear at the top left at the first as the coordinates are [0,0]
            self.coordinates.append([0, 0])

            # craeting some squares after thhis we will have the snake at the top left corner
        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag="sanke")
            self.squares.append(square)


class Food:
    def __init__(self):
        # cause we will have the total spaces which is obtained by dividing the following exclusive the final one and converting it to pixel
        x = random.randint(0, int((GAME_WIDTH/SPACE_SIZE)-1)) * SPACE_SIZE
        y = random.randint(0, int((GAME_HEIGHT/SPACE_SIZE)-1)) * SPACE_SIZE

        self.coordinates = [x, y]

        # drawing the food into the canvas
        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE,
                           fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):

    # unpacking the snakes head
    x, y = snake.coordinates[0]
    # if else statements for directions
    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    # changing the coordinates for the head for next turn
    snake.coordinates.insert(0, (x, y))
    # creating a new graphic for the head and insert the new snake head into the squares
    square = canvas.create_rectangle(
        x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:

        # deleting the last index of the snake as it moves
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # checking collisions and then update the game as gameover if there is any collisions and continue if there isint any
    if check_collissions(snake):
        game_over()
    else:
        # calling next turn fucntion for nect turn
        window.after(SPEED, next_turn, snake, food)


def change_directions(new_direction):
    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction

    elif new_direction == "right":
        if direction != "left":
            direction = new_direction

    elif new_direction == "up":
        if direction != "down":
            direction = new_direction

    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_collissions(snake):
    x, y = snake.coordinates[0]

    # game over if sanke goes out of the snake game window height and weight
    if x < 0 or x > GAME_WIDTH:
        print('GAME OVER')
        return True
    elif y < 0 or y > GAME_HEIGHT:
        print('GAME OVER')
        return True

    # game over if our snake touches itself
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")


# making a window for working or graphical interface
window = Tk()
# setting the name of the graphical window
window.title("Snake Game")
# making the window that we made static and not change its size
window.resizable(False, False)
# #calling the main loop of the window function of tkinter
# window.mainloop()

# making the score
score = 0
direction = "down"
# making the score label
label = Label(window, text="score:{}".format(score), font=("consolas", 40))
label.pack()
# creating a canvas
canvas = Canvas(window, bg=BACKGROUND_COLOR,
                height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# updating the windows
window.update()

# making the window popup at the middle
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenheight()

# findind out the exact int value
x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))

# setting the geometry to be in the middle
# window.geometry(f"{window_height}*{window_width}+{x}+{y}")

# binding the keys to run the snake
window.bind('<Left>', lambda event: change_directions("left"))
window.bind('<a>', lambda event: change_directions("left"))
window.bind('<Right>', lambda event: change_directions("right"))
window.bind('<d>', lambda event: change_directions("right"))
window.bind('<Up>', lambda event: change_directions("up"))
window.bind('<w>', lambda event: change_directions("up"))
window.bind('<Down>', lambda event: change_directions("down"))
window.bind('<s>', lambda event: change_directions("down"))


# calling the classes
snake = snake()
food = Food()
next_turn(snake, food)


# calling the main loop of the window function of tkinter
window.mainloop()
