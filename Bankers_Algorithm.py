n_process=int(input("Enter the number of process : "))
n_resource=int(input("Enter the number of resource : "))
allocation_matrix =[]
max_matrix=[]
avialable_resources=[]
for i in range(n_process):
    print(f"\n Enter details for P{i}")
    allocation_matrix.append([int(char)
                              for char in input(f"Enter a allocation : ")])
    max_matrix.append([int(char) for char in input(f"Enter a max : ")])
avialable_resources= [
    int(char) for char in input(f"\n Enter Avialable Resources : ")
]
print("Enter New Request Details")
pid=int(input("Enter Pid: "))
request_for_resources=[int(char)
                       for char in input("Enter a request Resources: ")]

f=[0]*n_process
ans=[0]*n_process
ind=0
for k in range(n_process):
    f[k]=0

need = [[0 for i in range(n_resource)] for i in range(n_process)]
for i in range(n_process):
    for j in range(n_resource):
        need[i][j] = max_matrix[i][j] - allocation_matrix[i][j]
y = 0
for k in range(n_process):
    for i in range(n_process):
        if (f[i] == 0):
            flag = 0
            for j in range(n_resource):
                if (need[i][j] > avialable_resources[j]):
                    flag = 1
                    break

            if (flag == 0):
                ans[ind] = i
                ind += 1
                for y in range(n_resource):
                    avialable_resources[y] += allocation_matrix[i][y]
                f[i] = 1

                print(f"p{ans[ind-1]} is visited ({need[i]}")

print("SYSTEM IS IN SAFE STATE")
safe_sequence="".join(f"p{ans[i]} " for i in range(n_process -1))
print(f"The Safe Sequence is -- ({safe_sequence}p{ans[n_process -1]})")

print("process \t\t Allocation \t\t Max \t\t Need")
for i in range(n_process):
    print(f"p{i}\t\t{allocation_matrix[i]}\t\t{max_matrix[i]}\t\t{need[i]}")