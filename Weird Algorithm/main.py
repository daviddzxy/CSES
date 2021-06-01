def solve(x):
    print(int(x), end=" ")
    if(x == 1):
        return
    elif not (x % 2): 
        x = x / 2
    else:
        x = x * 3
        x += 1
    solve(x)


x = input()
solve(int(x))


