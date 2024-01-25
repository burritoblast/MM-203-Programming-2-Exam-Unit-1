import time

current_x = 15
current_y = 15
current_direction = 'left'
obstacles = [(11, 15), (12, 7), (7, 8), (8, 2), (1, 3), (2, 1), (4, 2)]
turns_at_cell = {
    (12, 15) : 1,
    (12, 8) : 3,
    (8, 8) : 1,
    (8, 3) : 3,
    (2, 3) : 1,
    (2, 2) : 1,
    (3, 2) : 1,
}

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
    return (current_x, current_y) == (3, 16)


def navigate_maze():
    time.sleep(0.2)
    while not at_goal():
        cell = (current_x, current_y)
        if cell in turns_at_cell:
            for _ in range(turns_at_cell[cell]):
                turn_clockwise()
                time.sleep(0.2)
        if peek():
            move()
        else:
            while not peek():
                turn()
            move()

        print("Moved to:", current_x, "X,", current_y, "Y -", "Direction:", current_direction)

    print("Goal reached at:", current_x, "X,", current_y, "Y",)


navigate_maze()