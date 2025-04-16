n = "1"
flag = []

while n  != "-1":
    n = input()
    s = 0
    if n != "-1":
        for i in range(len(n)):
            s+=(int(n[i]))**len(n)
        flag.append(s==int(n))

for j in flag:
    print(j)
