n = int(input())
if n == 1:
    print(n)
    exit()
elif 1 < n < 4:
    print("NO SOLUTION")
    exit()

odd = []
even = []

for i in range(2, n+1, 2):
    even.append(i)

for i in range(1, n+1, 2):
    odd.append(i)

print(*even, sep=" ", end=" ")
print(*odd, sep= " ",end="")
# its faster to add items into array and print
# whole array rather than printing every number separately

