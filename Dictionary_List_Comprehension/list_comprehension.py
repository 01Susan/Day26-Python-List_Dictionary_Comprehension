def read_file(filename):
    with open(filename, mode="r") as file:
        numbers = file.readlines()
        return numbers


file1_num = read_file("file1.txt")
file2_num = read_file("file2.txt")

result = [int(num) for num in file1_num if num in file2_num]
print(result)
