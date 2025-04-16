def solve():
    n, m = map(int, input().split())
    col = [0 for j in range(m)]

    for i in range(n):
        s = input()

        for j in range(m - 1):
            if s[j] != s[j + 1]:
                col[j] += 1

        if s[m - 1] == '1':
            col[m - 1] += 1

    print(sum([min(col[j], n - col[j]) for j in range(m)]))


t = int(input())
for i in range(t):
    solve()
