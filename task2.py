import time

current_x = 11
current_y = 8
current_direction = 'left'
obstacles = [(7, 8), (8, 5), (14, 6), (13, 11), (5, 10), (6, 3), (16, 4), (15, 13), (3, 12), (4, 1), (18, 2), (17, 15), (1, 14)]

def move():
    time.sleep(0.2)
    global current_x, current_y

    if peek():
        if current_direction == 'up':
            current_y -= 1
        elif current_direction == 'down':
            current_y += 1
        elif current_direction == 'left':
            current_x -= 1
        elif current_direction == 'right':
            current_x += 1
    else:
        turn()


def turn_clockwise():
    global current_direction
    if current_direction == 'up':
        current_direction = 'right'
    elif current_direction == 'right':
        current_direction = 'down'
    elif current_direction == 'down':
        current_direction = 'left'
    elif current_direction == 'left':
        current_direction = 'up'

    print("Turned clockwise. New direction:", current_direction)


def turn():
    global current_direction
    turn_clockwise()
    if peek():
        pass
    else:
        for _ in range(2):
            turn_clockwise()


def peek():
    global current_x, current_y, current_direction
    next_x, next_y = current_x, current_y
    if current_direction == 'up':
        next_y -= 1
    elif current_direction == 'down':
        next_y += 1
    elif current_direction == 'left':
        next_x -= 1
    elif current_direction == 'right':
        next_x += 1
    return (next_x, next_y) not in obstacles


def at_goal():
    return (current_x, current_y) == (2, 1)


def navigate_maze():
    time.sleep(0.2)
    while not at_goal():
        if peek():
            move()
        else:
            while not peek():
                turn()
            move()

        print("Moved to:", current_x, "X,", current_y, "Y -", "Direction:", current_direction)

    print("Goal reached at:", current_x, "X,", current_y, "Y",)


navigate_maze()