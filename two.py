
ROCK = 1
PAPER = 2
SCISSORS = 3

them_map = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
}

you_map = {
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS,
}


def parse(lines):
    """
    Parse the input lines and return a list of rock,paper,scissors pairs.
    """
    for line in lines:
        them, you = line.split()
        yield them_map[them], you_map[you]


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


if __name__ == '__main__':
    with open('inputs/two.txt') as f:
        input = f.readlines()

    scores = [score(move) for move in parse(input)]
    print(sum(scores))
