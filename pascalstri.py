row = int(input("Enter number of rows: "))

space = 36

# empty list containg all 0s
a = [0] * 20


print("\n\t\t\t\t*** PASCAL TRIANGLE ***\n")
for i in range(row):

    for spi in range(1,space+1):
        print(" ", end="")

    a[i] = 1

    for j in range(i+1):
        print('%6d' %(a[j]), end = "")

    for j in range(i,0,-1):
        a[j] = a[j] + a[j-1]

    space = space - 3

    print()
