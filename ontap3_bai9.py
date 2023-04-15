# Bài 9: Viết chương trình Python tính số lượng các số dương liên tiếp có tổng lớn nhất.
item1 = [0, 100, 101, -5, -5, 6, 8, 7, 7, 7, -1, 8, 7, -2, -3, -4, 5, 6, 7, 70]


def sumMax(item):  # 3n + 2 -> O(n) = n
    sequence = 0
    sequenceMax = 0
    totalMax = 0
    total = 0
    for v in item:  # n + 1
        if v >= 0:
            sequence += 1
            total += v
        else:
            if total > totalMax:  # 2n
                totalMax = total
                sequenceMax = sequence
            sequence = 0
            total = 0
    if total > totalMax:  # 1
        sequenceMax = sequence

    return sequenceMax


print(sumMax(item1))
