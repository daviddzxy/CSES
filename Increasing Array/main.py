x = int(input())
y = list(map(int, input().split()))
incs = 0

for i in range(1, x):
    if y[i-1] > y[i]:
        incs += y[i-1] - y[i]
        y[i] = y[i-1]

print(incs)

