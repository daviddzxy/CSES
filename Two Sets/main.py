x = int(input())

sum_x = int((x * (x + 1)) / 2)
set1 = set(i for i in range(1, x + 1)) 
set2 = set()
if not sum_x % 2:
    set1_sum = sum_x
    half_sum = sum_x // 2
    while set1_sum - x > half_sum:
        set1.remove(x)
        set2.add(x)
        set1_sum -= x
        x -= 1 

    diff = set1_sum - half_sum
    set1.remove(diff)
    set2.add(diff)
    print("YES")
    print(len(set1))
    print(*set1, sep=" ")
    print(len(set2))
    print(*set2, sep=" ")
else:
    print("NO")


