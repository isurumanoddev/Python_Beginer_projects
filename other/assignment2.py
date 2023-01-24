def read_file(file_name):

    with open(file_name, 'r') as file:
        contents = file.read()
    return contents

    raise NotImplementedError()


def read_file_into_list(file_name):

    list = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            list.append(line)
    return list

    raise NotImplementedError()


def write_first_line_to_file(file_contents, output_filename):

    first_newline = file_contents.split("\n")[0]

    with open(output_filename, 'w') as file:
        file.write(first_newline)

    raise NotImplementedError()


def read_even_numbered_lines(file_name):

    list = []
    with open(file_name, "r") as f:
        readline = f.readlines()

        for i, line in enumerate(readline):
            split = line.split("\n")
            if i % 2 == 0:
                list.append(split)
    return list

    raise NotImplementedError()


def read_file_in_reverse(file_name):

    reverse_lines = []
    with open(file_name, "r") as f:
        readline = f.readlines()
        readline.reverse()
        for i, line in enumerate(readline):
            reverse_lines.append(line)

    print(reverse_lines)
    return reverse_lines

    raise NotImplementedError()


'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''


def main():
    # file_contents = read_file("sampletext.txt")
    # print(read_file_into_list("sampletext.txt"))
    # write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    # print(read_file_in_reverse("sampletext.txt"))


if __name__ == "__main__":
    main()