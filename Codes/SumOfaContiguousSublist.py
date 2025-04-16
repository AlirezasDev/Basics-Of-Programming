numbers = list(map(int,input().split()))
maxt = maxc = numbers[0]
for i in range(1,len(numbers)):
    maxc = max(numbers[i],maxc+numbers[i])
    if maxc > maxt:
        maxt = maxc

print(maxt)
