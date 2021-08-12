from operator import itemgetter
import sys

n = int(input())
x = [0] * 2 * n 
 
for i in range(0, n * 2, 2):
    x[i], x[i + 1] = sys.stdin.readline().split()
    x[i], x[i + 1] = (int(x[i]), 1), (int(x[i + 1]), -1)
 
x.sort(key=itemgetter(0))
 
max_customers = 0
curr_customers = 0
for i in x:
    curr_customers += i[1]
    max_customers = max(curr_customers, max_customers)
 
print(max_customers)
 
