import turtle
import random

def comchest(spot, card):
    # community chest cards
    card = (card % 16)
    if card == 1:
        return 10
    elif card == 13:
        return 0
    else:
        return spot


def chance(spot, card):
    # chance cards
    card = (card % 16)
    if card == 4 or card == 10:
        if spot == 7:
            return 15
        if spot == 22:
            return 25
        if spot == 36:
            return 5
    elif card == 7:
        return 0
    elif card == 2:
        return 39
    elif card == 12:
        return 5
    elif card == 5:
        return 24
    elif card == 14:
        return 11
    elif card == 15:
        return (spot - 3)
    elif card == 11:
        return 10
    elif card == 13:
        if spot == 7 or spot == 36:
            return 12
        if spot == 22:
            return 28
    else:
        return spot


def display(board, iterations, properties):
    # displays results
    # print(board)
    tom = turtle.Turtle()
    tom.ht()
    tom.up()
    tom.pensize(5)
    tom.goto(-300, -120)
    for i in range(40):
        print(((board[i] / iterations) * 100), "%")
        height = board[i] / iterations * 5000
        tom.seth(90)
        tom.down()
        tom.fd(height)
        tom.write(properties[i])
        tom.up()
        tom.rt(180)
        tom.fd(height)
        tom.lt(90)
        tom.fd(15)


def roll():
    # rolls dice, returns result and if they're doubles
    die1 = random.randint(1, 7)
    die2 = random.randint(1, 7)
    if die1 == die2:
        dubs = True
    else:
        dubs = False
    out = [(die1 + die2), dubs]
    return out


def main():
    # sets number of rolls and runs simulation
    iterations = 1000000
    board = []
    for i in range(40):
        board.insert(i, 0)
    spot = 0
    dubs = 0
    jail = False
    chancecount = 0
    comcount = 0

    for i in range(iterations):
        # checks for doubles, and decides if in/out of jail
        if spot == 10 and jail:
            free = False
            attempt = 0
            while not free and attempt != 3:
                x = roll()
                free = x[1]
                attempt += 1
            out = [x[0], False]
        else:
            out = roll()
        if out[1]:
            dubs += 1
        else:
            dubs = 0
        if dubs == 3:
            spot = 10
            jail = True
        else:
            spot = spot + out[0]
            if spot > 39:
                spot = spot - 40
            if spot == 30:
                board[spot] += 1
                spot = 10
                jail = True
            if spot == 7 or spot == 22 or spot == 36:
                save = spot
                spot = chance(spot, chancecount)
                if save != spot:
                    board[save] += 1
                if spot == 10:
                    jail = True
                chancecount += 1
            if spot == 2 or spot == 17 or spot == 33:
                save = spot
                spot = comchest(spot, comcount)
                if save != spot:
                    board[save] += 1
                if spot == 10:
                    jail = True
                comcount += 1

        board[spot] += 1

    properties = []
    for i in range(40):
        properties.insert(i, i)
    properties[0] = "Go"
    properties[10] = "Jail"
    properties[24] = "Illinois"
    display(board, iterations, properties)
    quit = 0
    while quit == 0:
        quit = input()


main()