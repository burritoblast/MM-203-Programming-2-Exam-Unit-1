import time

current_x = 40
current_y = 30
current_direction = 'left'
obstacles = [(40, 25), (35, 26), (36, 24), (34, 16), (30, 17), (31,15), (32, 16), (29, 16), (30, 13), (31, 11), (25, 12), (26, 10), (24, 11), (25, 8), (21, 9), (22, 5), (20, 6), (21, 3), (18, 8), (12, 7), (13, 5), (14, 6), (8, 6), (9, 4), (10, 5), (7, 5), (9, 4), (5, 4), (7, 3), (1, 3)]
turns_at_cell = {
    (40, 30) : 1,
    (40, 26) : 3,
    (36, 26) : 1,
    (36, 25) : 3,
    (35, 25) : 1,
    (35, 22) : 3,
    (34, 22) : 1,
    (34, 17) : 3,
    (31, 17) : 1,
    (31, 16) : 3,
    (30, 16) : 1,
    (30, 14) : 1,
    (31, 14) : 3,
    (31, 12) : 3,
    (26, 12) : 1,
    (26, 11) : 3,
    (25, 11) : 1,
    (25, 9) : 3,
    (22, 9) : 1,
    (22, 6) : 3,
    (21, 6) : 1,
    (21, 4) : 3,
    (18, 4) : 3,
    (18, 7) : 1,
    (13, 7) : 1,
    (13, 6) : 3,
    (9, 6) : 1,
    (9, 5) : 3,
    (8, 5) : 1,
    (8, 4) : 3,
    (6, 4) : 1,
    (6, 3) : 3,
    (2, 3) : 1,

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
    return (current_x, current_y) == (2, 1)


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