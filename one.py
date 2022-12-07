
def parse(lines):
    """
    Parse the input lines and return a list of elves and their total calories.
    """
    sum = 0
    for line in lines:
        if line.strip() == '':
            yield sum
            sum = 0
            continue

        calories = int(line.split()[-1])
        sum += calories
    yield sum


if __name__ == '__main__':
    with open('inputs/one.txt') as f:
        input = f.readlines()

    elf_calories = list(parse(input))

    # sort the list of calories with the highest first
    elf_calories.sort(reverse=True)
    # print the sum of the first three
    print(sum(elf_calories[0:3]))
