
def split_in_two(line):
    """
    Split the line in two halves
    """
    half = len(line) // 2
    return line[:half], line[half:]


def parse(lines):
    """
    Parse the input lines
    """
    for line in lines:
        section1, section2 = split_in_two(line)
        # find the common character that is in both sections of the text
        common = set(section1).intersection(set(section2)).pop()
        # get the associated number for the character (a = 1, b = 2, A = 27, B = 28, etc)
        if common.isupper():
            number = ord(common) - 64 + 26
        else:
            number = ord(common) - 96
        #print(f'Common character: {common}, number: {number}')
        # yield the number
        yield number


if __name__ == '__main__':
    with open('inputs/three.txt') as f:
        input = f.readlines()

    print(sum(parse(input)))
