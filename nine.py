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


def calculate_visited(directions):
    """
    Calculate set of visited coordinates by the tail.
    """
    x, y = 0, 0
    visited = {(0, 0)}
    for head_x, head_y in traverse(directions):
        # if we are directly adjacent, then we won't move
        if abs(x - head_x) <= 1 and abs(y - head_y) <= 1:
            continue

        if x != head_x:
            x += move_in_direction(x, head_x)
        if y != head_y:
            y += move_in_direction(y, head_y)

        visited.add((x, y))
    return visited


if __name__ == '__main__':
    with open('inputs/nine_example.txt', 'r') as f:
        input = [line.strip('\n') for line in f]

    directions = parse_directions(input)
    visited = calculate_visited(directions)
    print(len(visited))
