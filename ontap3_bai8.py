# Bài 8: Viết chương trình Python tính số lượng các số dương liên tiếp nhiều nhất.
item1 = [0, 3, 4, 5, -5, 6, 8, 7, 7, 7, -1, 8, 7, -2, -3, -4, 5, 6, 7]
item2 = [0, 3, 4, 5, -5, 6, 8, 7, 7, 7, -1, 8, 7, -2, -3, -4, 5, 6, 7, 1, 1, 1]


def count(item):  # 3n+2 -> O(n)
    sequence = 0
    sequenceMax = 0
    for i in item:  # n+1
        if i >= 0:
            sequence += 1
        else:
            if sequence > sequenceMax:  # 2n
                sequenceMax = sequence
            sequence = 0
    if sequence > sequenceMax:  # 1
        sequenceMax = sequence
    return sequenceMax


print(count(item2))

# Bài 9: Viết chương trình Python tính số lượng các số dương liên tiếp có tổng lớn nhất.
