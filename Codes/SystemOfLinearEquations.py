def swap_col(M,n,c):
    temp=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j!=c:
                temp[i][j]=M[i][j]
            else:
                temp[i][j]=M[i][n]
    return temp


def del_row(M,dr,r,c):
    temp=[[] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            temp[i].append(M[i][j])
    del temp[dr]
    return temp 

def del_col(M,dc,r,c):
    temp=[[] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if j!=dc:
                temp[i].append(M[i][j])
    return temp

def cal_det(M,n):
    if n==1:
        return M[0][0]
    if n==2:
        return M[0][0]*M[1][1]-M[0][1]*M[1][0]
    s=0
    for i in range(n):
        del_col_M=del_col(M,i,n,n)
        kahad=del_row(del_col_M,0,n,n-1)
        s+=M[0][i]*cal_det(kahad,n-1)*((-1)**int(i%2!=0))
    return s


n = int(input())
matrix = []
for _ in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

M=[[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        M[i].append(matrix[i][j])

det=cal_det(M,n)
ans=[[] for _ in range(n)]

for i in range(n):
    M_swap=swap_col(matrix,n,i)
    var_det=cal_det(M_swap,n)
    if var_det!=0:
        ans[i].append(var_det/det)
    else:
        ans[i].append(0)

output = " ".join(["{:.2f}".format(val[0]) for val in ans])
print(output)
