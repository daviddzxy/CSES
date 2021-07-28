n, m, k = list(map(int, input().split()))
apartments = list(map(int, input().split()))
applicants = list(map(int, input().split()))

apartments.sort()
applicants.sort()

result = 0
ii = 0
jj = 0
for i in range(ii, len(applicants)):
    for j in range(jj, len(apartments)):
        if abs(apartments[j] - applicants[i]) <= k:
            result += 1
            jj = j + 1
            break
        elif apartments[j] - applicants[i] > k:
            ii = i
            jj = j
            break


print(result)
