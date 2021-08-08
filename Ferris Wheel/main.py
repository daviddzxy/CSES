n, x = list(map(int, input().split()))
p = list(map(int, input().split()))

p.sort()

i = 0
j = n - 1
gondolas = 0

while i < j:
    if p[i] + p[j] <= x:
        gondolas += 1
        i += 1
        j -= 1
    elif p[i] + p[j] > x and p[j] <= x:
        gondolas += 1
        j -= 1
    elif p[j] > x:
        j -= 1

if i == j and p[i] <= x:
    gondolas += 1


print(gondolas)
