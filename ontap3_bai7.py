# Bài 7: Viết chương trình Python tìm phần tử lớn thứ nhì của danh sách và các vị trí của các phần tử đạt giá trị lớn nhì.
# tim gia tri lon nhat
item1 = [500, 430, 12, 430, 55, 430]

# 2n + 1 -> O(n)


def findMax(item):
    k = item[0]
    for i in range(len(item)):  # n
        if item[i] > k:  # n
            k = item[i]
    return k

# 6n + 2 -> O(n)


def find2ndMax(item):
    max = findMax(item)  # 2n + 1
    secondmax = None
    for i in range(len(item)):  # n + 1
        if (secondmax is None or item[i] > secondmax) and item[i] < max:  # 3n
            secondmax = item[i]
    return secondmax

# 8n + 3 -> O(n)

def index2ndMax(item):
    a = []
    secondmax = find2ndMax(item) # 6n + 2
    for i in range(len(item)): # n+1
        if item[i] == secondmax: #n
            a.append(i)
    return a


print(index2ndMax(item1))
