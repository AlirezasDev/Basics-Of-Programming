line, k = input(), int(input())
stones = sorted(map(int, line.split(',')))
n = len(stones)
used = [False] * n
result = []

for i in range(n):
    if not used[i]:
        subset = []
        current = stones[i]
        for j in range(k):
            found = False
            for w in range(n):
                if not used[w] and stones[w] == current:
                    subset.append(stones[w])
                    used[w] = True
                    current += 1
                    found = True
                    break
            if not found:
                print("no possible partition")
                exit()
        result.append(subset)

for subset in result:
    print(subset)
