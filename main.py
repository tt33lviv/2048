def pretty_print(mas):
    print('-' * 10)
    for row in mas:
        print(*row)
    print('-' * 10)
                    #j
    # [1,  2,  3,  4],
    # [5,  6,  7,  8],
    # [9,  10, 11, 12],
    # [13, 14, 15, 16],
   #i   i * 4 + j + 1   9
   #    2 * 4 + j + 1 = 9
   #123


def get_number_from_index(i,j):
    return i * 4 + j + 1

def get_empty_list(mas):
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i,j)
                empty.append(num)
    return empty

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

mas[1] [2] = 2
mas[3] [0] = 4
print(get_empty_list(mas))
pretty_print(mas)

