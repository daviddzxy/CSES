import math

n = int(input())
x = list(map(int, input().split()))
loc_max = 0
glob_max = -math.inf
for i in x:
    loc_max = max(i, i + loc_max)
    glob_max = max(loc_max, glob_max)

print(glob_max)
