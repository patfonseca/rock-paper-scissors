file = open('sums.txt', 'r')
for line in file:
    numbers_list = line.split()
    print(int(numbers_list[0]) + int(numbers_list[1]))
file.close()