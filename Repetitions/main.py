x = input()
prev = ""
max_s = 0
curr_s = 1
for c in x:
    if c == prev:
        curr_s += 1
    else:
        curr_s = 1

    if curr_s > max_s:
        max_s = curr_s

    prev = c

print(max_s)
