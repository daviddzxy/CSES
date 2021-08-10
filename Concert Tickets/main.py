from collections import Counter
from bisect import bisect_left

n, m = list(map(int, input().split()))
h = list(map(int, input().split()))
t = list(map(int, input().split()))

h.sort()
occurences = Counter(h)

def decrement_occurences(num, occ_set):
    occ_set[num] -= 1
    if occ_set[num] < 1:
        del occ_set[num]


def get_ticket(t):
    if t < h[0]:
        return(-1)

    if t in occurences:
        decrement_occurences(t, occurences)
        return t

    idx = bisect_left(h, t) - 1
    
    while idx > -1:
        if h[idx] in occurences:
            decrement_occurences(h[idx], occurences)
            return h[idx]
        else:
            idx -= 1

    return -1

for customer in t:
    print(get_ticket(customer))


