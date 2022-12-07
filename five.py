
def parse_moves(lines):
    """
    Parsing lines like this:

    move 3 from 5 to 7
    move 2 from 8 to 9
    move 4 from 3 to 5

    into tuples like this:
    (3, 5, 7)
    """
    for line in lines:
        if line.startswith('move'):
            chunks = line.split()
            yield int(chunks[1]), int(chunks[3]), int(chunks[5])


def parse_stacks(lines):
    """
    Input looks like this:

    [F] 
[F] [M] 
[M] [Z] 
 1   2 

Should parse into arrays like this:
[
    [F,M],
    [F,M,Z],
]
    etc...
    """
    stack_lines = []
    for line in lines:
        stack_lines.append(line)
        if line.startswith(' 1'):
            break

    for i, c in enumerate(stack_lines[-1]):
        if c.isdigit():
            stack = []
            for line in stack_lines[:-1]:
                if line[i] != ' ':
                    stack.append(line[i])
            yield stack


def do_moves(stacks, moves):
    """
    Given a list of stacks and a list of moves, perform the moves and
    return the resulting stacks.
    """
    for [num_items, from_stack_i, to_stack_i] in moves:
        for _ in range(num_items):
            to_stack = stacks[to_stack_i - 1]
            from_stack = stacks[from_stack_i - 1]
            item = from_stack.pop(0)
            to_stack.insert(0, item)
    return stacks


if __name__ == '__main__':
    with open('inputs/five.txt') as f:
        input = f.readlines()

    moves = list(parse_moves(input))
    stacks = list(parse_stacks(input))
    result_stacks = do_moves(stacks, moves)

    print(''.join([c[0] for c in result_stacks]))
