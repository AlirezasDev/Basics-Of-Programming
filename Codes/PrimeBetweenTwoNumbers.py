start = int(input())
end = int(input())
for i in range(start,end+1):
    flag = True
    for j in range(2,int(i**(0.5))+1):
        if i % j == 0:
            flag = False
            break
    if flag and i != 1:
        print(i)
