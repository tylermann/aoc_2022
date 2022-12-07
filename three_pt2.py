def chunk_in_three(lines):
    """
    yield batches of 3 lines
    """
    for i in range(0, len(lines), 3):
        yield lines[i:i+3]


def parse(lines):
    """
    """
    # find the common character in the lines
    sets = [set(line) for line in lines]
    common = sets[0].intersection(sets[1], sets[2])
    common = common.pop()

    # get the associated number for the character (a = 1, b = 2, A = 27, B = 28, etc)
    if common.isupper():
        number = ord(common) - 64 + 26
    else:
        number = ord(common) - 96
    # print(f'Common character: {common}, number: {number}')

    return number


if __name__ == '__main__':
    with open('inputs/three.txt') as f:
        input = f.readlines()

    # trim the newline characters
    input = [line.strip() for line in input]

    print(sum(parse(chunk) for chunk in chunk_in_three(input)))
