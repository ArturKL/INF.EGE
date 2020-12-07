def can_win(state):
    if (max(state) * 3 + min(state)) >= 45:
        return True



def move(state, player, move_number, history):
    history.append(state)
    if can_win(state):
        if player is False and move_number == 4:
            return state, player, move_number, history[0][1]
    else:
        if player is True:
            if state[0] < state[1]:
                a = move([state[0] + 1, state[1]], not player, move_number + 1, history)
                if a:
                    print(a)
            else:
                a = move([state[0], state[1] + 1], not player, move_number + 1, history)
                if a:
                    print(a)
        else:
            a = move([state[0] * 3, state[1]], not player, move_number + 1, history)
            if a:
                print(a)
            a = move([state[0] + 1, state[1]], not player, move_number + 1, history)
            if a:
                print(a)
            a = move([state[0], state[1] * 3], not player, move_number + 1, history)
            if a:
                print(a)
            a = move([state[0], state[1] + 1], not player, move_number + 1, history)
            if a:
                print(a)


for s in range(1, 40):
    move([4, s], True, 1, [])