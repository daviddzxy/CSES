from operator import itemgetter
import sys
 
n = int(input())
x = [None] * n
 
for i in range(n):
    start, end = sys.stdin.readline().split()
    x[i] = (int(start), int(end))

x.sort(key=itemgetter(1))

movies = 0
prev_end = 0
for m in x:
    if m[0] >= prev_end and m[1] > prev_end:
        movies += 1
        prev_end = m[1]

print(movies)



