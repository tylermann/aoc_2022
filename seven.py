def parse_commands(lines):
    """
    Parse lines into commands and outputs
    """
    commands = []
    curr_command = ''
    curr_output = []
    for line in lines:
        if line.startswith('$ '):
            if curr_command:
                commands.append([curr_command, curr_output])
            curr_command = line[2:]
            curr_output = []
            continue

        curr_output.append(line)

    commands.append([curr_command, curr_output])

    return commands


class Node:
    def __init__(self, name, is_dir, parent=None):
        self.name = name
        self.is_dir = is_dir
        self.parent = parent


class File(Node):
    def __init__(self, name, file_size):
        super().__init__(name, False)
        self.file_size = file_size

    def __repr__(self) -> str:
        return super().__repr__() + f' {self.file_size}'


class Dir(Node):
    def __init__(self, name, parent=None):
        super().__init__(name, True, parent=parent)
        self.children = []
        self.file_size = 0


def create_fs(commands):
    root = Dir('/')
    node = root

    # skip the first command since it is just going to cd /
    for command, output in commands[1:]:
        if command == 'ls':
            for line in output:
                meta, name = line.split(' ')
                if meta == 'dir':
                    node.children.append(
                        Dir(name, parent=node))
                else:
                    node.children.append(File(name, file_size=meta))

        elif command.startswith('cd '):
            # get the directory
            directory = command[3:]

            if directory == '..':
                node = node.parent
                continue

            if directory == '/':
                node = root
                continue

            # find the directory in the children
            for child in node.children:
                if child.name == directory:
                    node = child
                    break
        else:
            raise ValueError(f'Unknown command: {command}')

    return root


def dir_disk_size(node, dirs=None, parent_prefix=''):
    """
    Calculate the disk size of each directory and return in a dictionary
    """
    if dirs is None:
        dirs = {}
    
    if node.is_dir:
        key = parent_prefix + node.name
        dirs[key] = 0
        for child in node.children:
            if child.is_dir:
                dir_disk_size(child, dirs, key + '/')
                dirs[key] += child.file_size
            else:
                dirs[key] += int(child.file_size)
        
        node.file_size = dirs[key]

    return dirs


def print_nodes(node, indent=0):
    """
    Print the nodes in the file system
    """
    print(' ' * indent, node.name)
    if node.is_dir:
        for child in node.children:
            print_nodes(child, indent + 2)


if __name__ == '__main__':
    with open('inputs/seven.txt') as f:
        input = f.readlines()
        # trim the newline characters
        input = [line.strip("\n") for line in input]

    commands = parse_commands(input)
    # print(commands)
    fs = create_fs(commands)

    sizes = dir_disk_size(fs)

    max_size = 100000
    total = 0
    for name, size in sizes.items():
        if size < max_size:
            total += size
    print(total)
    # print(sizes)
    # print_nodes(fs)
