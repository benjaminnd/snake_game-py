import random
import curses
# this game use curse library which can be run only on Unix and IOS
# initialize screen using curses
screen = curses.initscr()
#make the cursor invisible
curses.curs_set(0)
# get tuple (y,x) of the screen
screen_height, screen_width = screen.getmaxyx()

# create a new window using sh
window = curses.newwin(screen_height,screen_width, 0, 0)
window.keypad(1)
window.timeout(100)

# create snake initial position
snake_x = screen_width/4
snake_y = screen_height/2

# draw snake's body
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

# draw food with initial position at the center of the screen
food = [screen_height/2, screen_width/2]
window.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT  # default direction of the snake

while True:
    next_key = window.getch()  # read key from player
    key = key if next_key == - 1 else next_key

    # game end cases
    if snake[0][0] in [0, screen_height] or snake [0][1] in [0, screen_width] or snake [0] in snake[1:]:
        curses.endwin()
        quit()

    new_pos = [snake[0][0], snake [0][1]] # new position of the head, default by the current position of the snake
    # read actual key pressed by player
    if key == curses.KEY_DOWN:
        new_pos[0] += 1
    if key == curses.KEY_UP:
        new_pos[0] -= 1
    if key == curses.KEY_LEFT:
        new_pos[1] -= 1
    if key == curses.KEY_DOWN:
        new_pos[0] += 1

    # add the new head to the snake
    snake.insert(0, new_pos)

    # check if the snake ran into the food
    if snake[0] == food:
        food = None # erase the food
        # loop to generate new food
        while food is None:
            new_f = [
                random.randint(1, screen_height - 1),
                random.randint(1, screen_width - 1)
            ]
            food = new_f if new_f not in snake else None
        window.addch(food[0], food[1], curses.ACS_PLUS) # add new food to the screen
    else:
        tail = snake.pop() # pop the tail off the snake when it move
        window.addch(tail[0], tail[1], ' ') # add a space where the tail disappears

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)










































