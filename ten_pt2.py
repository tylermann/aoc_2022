def parse_instructions(lines):
    for line in lines:
        if line.startswith('noop'):
            yield ('noop', None)
        elif line.startswith('addx '):
            yield ('noop', None)
            yield ('addx', int(line[5:]))
        else:
            raise ValueError('Invalid instruction' + line)


def run(instructions):
    x = 1
    for instruction, arg in instructions:
        yield x
        if instruction == 'noop':
            pass
        elif instruction == 'addx':
            x += arg
        else:
            raise ValueError('Invalid instruction' + instruction)
    return x


def draw(instructions):
    line = ''
    for cycle, x in enumerate(run(instructions), 1):
        pixel = (cycle - 1) % 40
        if pixel == 0 and line:
            yield line
            line = ''

        if x == pixel or x - 1 == pixel or x + 1 == pixel:
            line += '#'
        else:
            line += '.'
    yield line


if __name__ == '__main__':
    with open('inputs/ten.txt', 'r') as f:
        input = [line.strip('\n') for line in f]

    instructions = parse_instructions(input)
    for line in draw(instructions):
        print(line)
