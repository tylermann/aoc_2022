def parse_to_2d_array(lines):
    array = [list(line) for line in lines]
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = int(array[i][j])
    return array


def find_max_visiblity(array):
    max_score = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if i == 0 or i == len(array) - 1 or j == 0 or j == len(array[i]) - 1:
                continue

            curr_height = array[i][j]

            left_array = list(reversed(array[i][:j]))
            left_distance = 0

            for num, height in enumerate(left_array):
                left_distance = num + 1
                if curr_height <= height:
                    break

            right_array = array[i][j + 1:]
            right_distance = 0

            for num, height in enumerate(right_array):
                right_distance = num + 1
                if curr_height <= height:
                    break

            top_array = list(reversed([array[k][j] for k in range(i)]))
            top_distance = 0

            for num, height in enumerate(top_array):
                top_distance = num + 1
                if curr_height <= height:
                    break

            bottom_array = [array[k][j] for k in range(i + 1, len(array))]
            bottom_distance = 0

            for num, height in enumerate(bottom_array):
                bottom_distance = num + 1
                if curr_height <= height:
                    break

            score = left_distance * right_distance * top_distance * bottom_distance
            if score > max_score:
                max_score = score

    return max_score


if __name__ == '__main__':
    with open('inputs/eight.txt', 'r') as f:
        input = [line.strip('\n') for line in f]

    array = parse_to_2d_array(input)

    print(find_max_visiblity(array))
