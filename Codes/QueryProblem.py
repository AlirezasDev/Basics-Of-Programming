def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]
    return prefix


n, q = map(int, input().split())
arr = list(map(int, input().split()))

prefix = prefix_sum(arr)

results = []
for _ in range(q):
    l, r = map(int, input().split())
    result = prefix[r] - prefix[l - 1]
    results.append(result)

for res in results:
    print(res)
