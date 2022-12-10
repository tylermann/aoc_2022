def parse_directions(lines):
    out = []
    for line in lines:
        direction, distance = line.split()
        out.append((direction, int(distance)))
    return out


def traverse(directions):
    """
    Traverse the directions given and yield the coordinates.
    """
    x, y = 0, 0
    yield x, y

    for direction, distance in directions:
        if direction == 'R':
            for _ in range(distance):
                x += 1
                yield x, y
        elif direction == 'L':
            for _ in range(distance):
                x -= 1
                yield x, y
        elif direction == 'U':
            for _ in range(distance):
                y += 1
                yield x, y
        elif direction == 'D':
            for _ in range(distance):
                y -= 1
                yield x, y
        else:
            raise ValueError('Invalid direction')


def move_in_direction(c, desired_c):
    return 1 if c < desired_c else -1


def knot(coords):
    """
    Calculate the coordinates of a new knot in relation to the head coordinates given.
    """
    x, y = 0, 0
    for head_x, head_y in coords:
        # if we are directly adjacent, then we won't move
        if abs(x - head_x) <= 1 and abs(y - head_y) <= 1:
            yield x, y
            continue

        if x != head_x:
            x += move_in_direction(x, head_x)
        if y != head_y:
            y += move_in_direction(y, head_y)
        yield x, y


if __name__ == '__main__':
    with open('inputs/nine.txt', 'r') as f:
        input = [line.strip('\n') for line in f]

    directions = parse_directions(input)
    head_coords = traverse(directions)
    tail_coords = head_coords
    for _ in range(9):
        tail_coords = knot(tail_coords)
    visited = set(tail_coords)
    print(len(visited))
