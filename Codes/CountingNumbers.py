n = int(input())
if n == 0 :
    print("0")
else:
    a = []
    for i in range(1,n+1):
        if n % i == 0:
            a.append(i)

    print(" ".join(str(j) for j in a))
