# colA: cot nguon
# colB: cot trung gian
# colC: cot dich

def move(n, colA, colB, colC):
    # di chuyen dc dia n qa col c
    if n == 1:
        print(f'di chuyen dia {n} tu {colA} qua {colC}')
    else:
        # di chuyen n-1 dia qua col b
        move(n-1, colA, colC, colB)
        print(f'di chuyen dia {n} tu {colA} qua {colC}')
        # di chuyen dia n qua col c
        move(n-1, colB, colA, colC)


move(4, "A","B","C")
