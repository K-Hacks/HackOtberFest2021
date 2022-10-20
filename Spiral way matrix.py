n=int(input("Kindly Enter the dimensions of the matrix:"))
row=0;col=0
rr=1;cc=0
arr = [[0 for row in range(n)]for col in range(n)]
print(arr)
for i in range(1,n*n+1):
    arr[row][col]=i
    tr=row+rr; tc=col+cc
    if(tr==n or tr==-1 or tc==n or arr[tr][tc]!=0):
        temp=cc
        cc=rr
        rr=-temp
    row=row+rr;col=col+cc
print(arr)
for row in range(n):
    for col in range(n):
        print("%4d"%arr[row][col],end=" ")
    print()
print("End Of the Program")

