n = int(input())


i = 5
zeros = 0
while n // i > 0:
    zeros += n // i
    i *= 5

print(zeros)
