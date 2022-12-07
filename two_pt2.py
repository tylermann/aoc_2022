
ROCK = 1
PAPER = 2
SCISSORS = 3

them_map = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
}

action_map = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}


def parse(lines):
    """
    Parse the input lines and return a list of rock,paper,scissors pairs.
    """
    for line in lines:
        them, action = line.split()
        yield them_map[them], action_map[action]


def score(move):
    them, you = move

    lost = you
    won = you + 6
    tied = you + 3

    if you == them:
        return tied
    elif you == ROCK and them == SCISSORS:
        return won
    elif you == PAPER and them == ROCK:
        return won
    elif you == SCISSORS and them == PAPER:
        return won

    return lost


def get_move(play):
    """
    Given a play, return the move that would have been made.
    """
    them, action = play
    if action == 'draw':
        return them, them
    elif action == 'lose':
        if them == ROCK:
            return them, SCISSORS
        return them, them - 1
    elif action == 'win':
        if them == SCISSORS:
            return them, ROCK
        return them, them + 1
    else:
        raise ValueError('unknown action: %s' % action)


if __name__ == '__main__':
    with open('inputs/two.txt') as f:
        input = f.readlines()

    scores = [score(get_move(play)) for play in parse(input)]
    print(sum(scores))
