def can_win(state):
    if (max(state) * MULT + min(state)) >= GOAL:
        return True

GOAL = 61
KNOWN = 7
MULT = 2
DIF = 1


def move(state, player=True, move_number=1, history=[], winner=True, move_n=[]):
    history.append(state)
    if can_win(state):
        if player is winner and (move_number == move_n[0] or move_number == move_n[1]):
            return state, player, move_number, history[0][1]
    else:
        if player is not winner:
            if state[0] < state[1]:
                a = move([state[0] + DIF, state[1]], not player, move_number + 1, history, winner, move_n)
                if a:
                    print(a)
            else:
                a = move([state[0], state[1] + DIF], not player, move_number + 1, history, winner, move_n)
                if a:
                    print(a)
        else:
            a = move([state[0] * MULT, state[1]], not player, move_number + 1, history, winner, move_n)
            if a:
                print(a)
            a = move([state[0] + DIF, state[1]], not player, move_number + 1, history, winner, move_n)
            if a:
                print(a)
            a = move([state[0], state[1] * MULT], not player, move_number + 1, history, winner, move_n)
            if a:
                print(a)
            a = move([state[0], state[1] + DIF], not player, move_number + 1, history, winner, move_n)
            if a:
                print(a)


nin3 = True
for s in range(1, 53):
    if (KNOWN + s * 2 * 2 >= GOAL or KNOWN * 2 * 2 + s >= GOAL) and nin3:
        print(s)
        nin3 = False
    move([KNOWN, s], history=[], winner=True, move_n=[3, 3])
    move([KNOWN, s], history=[], winner=False, move_n=[2, 4])