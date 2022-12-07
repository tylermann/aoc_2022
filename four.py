def parse(line):
    """
    Parse a line like:
    2-4,4-5
    """
    # split the line on the comma
    parts = line.split(',')
    # split the parts on the dash
    parts = [part.split('-') for part in parts]
    # convert the parts to integers
    parts = [[int(part) for part in part] for part in parts]
    # return the parts
    return parts


def to_range(parts):
    """
    Convert the parts to a range set
    """
    return set(range(parts[0], parts[1] + 1))


def completely_overlapping(ranges):
    """
    Check if the ranges are completely overlapping
    """
    # get the intersection of the ranges
    intersection = set.intersection(*ranges)
    # check if the intersection is equal to either of the ranges
    return intersection == ranges[0] or intersection == ranges[1]


def partially_overlapping(ranges):
    """
    Check if the ranges are partially overlapping
    """
    # get the intersection of the ranges
    intersection = set.intersection(*ranges)
    # check if the intersection is not empty
    return len(intersection) > 0


if __name__ == '__main__':
    with open('inputs/four.txt') as f:
        input = f.readlines()
        # trim the newline characters
        input = [line.strip("\n") for line in input]

    total = 0
    for line in input:
        ranges = [to_range(part) for part in parse(line)]
        if partially_overlapping(ranges):
            total += 1
    print(total)
