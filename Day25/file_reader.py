def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())


read_file("sample.txt")