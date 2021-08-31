n = int(input())
p = list(map(int, input().split()))
p.sort()
median = p[n // 2]
diff = 0
for i in p:
    diff += abs(median - i)

print(diff)
