n, m, k = list(map(int, input().split()))
apartments = list(map(int, input().split()))
applicants = list(map(int, input().split()))

apartments.sort()
applicants.sort()

result = 0
i = 0
j = 0
while i < len(applicants) and j < len(apartments):
    if abs(apartments[j] - applicants[i]) <= k:
        result += 1
        i += 1
        j += 1
    elif apartments[j] - applicants[i] > k:
        i += 1
    else:
        j += 1

print(result)
