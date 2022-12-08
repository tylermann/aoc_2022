def parse_to_2d_array(lines):
    return [list(line) for line in lines]


def find_visible(array):
    visible = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if i == 0 or i == len(array) - 1 or j == 0 or j == len(array[i]) - 1:
                visible += 1
                continue

            curr_height = array[i][j]

            left_tallest = max(array[i][:j])
            right_tallest = max(array[i][j + 1:])
            top_tallest = max([array[k][j] for k in range(i)])
            bottom_tallest = max([array[k][j]
                                 for k in range(i + 1, len(array))])

            if curr_height > left_tallest or curr_height > right_tallest or curr_height > top_tallest or curr_height > bottom_tallest:
                visible += 1
    return visible


if __name__ == '__main__':
    with open('inputs/eight.txt', 'r') as f:
        input = [line.strip('\n') for line in f]

    array = parse_to_2d_array(input)

    print(find_visible(array))
