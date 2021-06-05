def get_non_attacking_positions(n):
    all_positions = int(((n**2) * ((n**2) - 1)) / 2)
    attacking_positions = int((n - 2) * (n - 1) * 4)
    non_attacking_positions = all_positions - attacking_positions
    return non_attacking_positions 


n = int(input())
for i in range(1, n + 1):
    print(get_non_attacking_positions(i))
