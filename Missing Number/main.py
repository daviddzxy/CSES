x = int(input())
y = list(map(int, input().split()))
sum_x = int(x * (x + 1) / 2)
sum_y = int(sum(y))
print(sum_x - sum_y)

