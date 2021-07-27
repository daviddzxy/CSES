n = int(input())
x = list(map(int, input().split()))
s = set()
distinct_vals = 0
for e in x:
    if e not in s:
        s.add(e)
        distinct_vals += 1 

print(distinct_vals)
