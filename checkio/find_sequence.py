from collections import Counter


def add(ls1, n):
    for i in range(n):
        ls1.append([])


def count(ls):
    t = []
    # print(ls)
    for i in range(1, 10):
        t.append(str(i) * 4)
    # print(t)
    for i in ls:
        # print(i)
        s = ''
        for j in i:
            s += str(j)
        for k in t:
            if k in s:
                return True

    return False

    return False


def checkio(matrix):
    row = matrix.copy()
    column = []
    matrix.reverse()
    add(column, len(matrix))
    left_bias = []
    right_bias = []

    # print(matrix)
    # print(row)
    for i in range(len(matrix)):
        for j in matrix:
            column[i].append(j[i])
    for i in range(2 * len(matrix) - 1):
        s = []
        l = []
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if j + k == i:
                    s.append(row[j][k])
                    l.append(matrix[j][k])

        left_bias.append(s)
        right_bias.append(l)
    # print(row,count(row))

    if count(row) == True or count(column) == True or count(left_bias) == True or count(right_bias) == True:
        return True
    else:
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    print("It is all good. Let's check it now")