
def parse(input, num=4):
    """
    Parse the input and find the first 4 unique characters that are back to back.
    """
    for i in range(len(input) - num - 1):
        if len(set(input[i:i+num])) == num:
            return i + num
    return None


if __name__ == '__main__':
    with open('inputs/six.txt') as f:
        input = f.readline()

    first_marker = parse(input, 14)
    print(first_marker)
