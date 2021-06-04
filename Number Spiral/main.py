def find(y1, x1):
    n = max(y1, x1)
    n_p = n ** 2
    
    if n_p % 2 == 0:
        y2 = n
        x2 = 1
    else:
        y2 = 1
        x2 = n

    return n_p - (abs(x2 - x1) + abs(y2 - y1))


t = int(input())

for i in range(t):
    # column x
    # row y
    y, x = list(map(int, input().split()))
    print(find(y, x))


