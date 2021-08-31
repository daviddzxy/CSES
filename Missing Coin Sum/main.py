n = int(input())
x = sorted(list(map(int, input().split())))
min_sum = 0
curr_sum = 0
res = 0
for i in x:
    if curr_sum + 1 < i:
        break
    curr_sum += i 

print(curr_sum + 1)

