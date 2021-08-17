n, x = list(map(int, input().split()))
a = list(map(int, input().split()))

d = {}

for i, m in enumerate(a, 1):
    if x - m in d:
        print('{} {}'.format(i, d[x - m]))
        exit()
    else:
        d[m] = i

print('IMPOSSIBLE')
