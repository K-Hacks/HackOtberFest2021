num=int(input('Enter a number: '))
def sum_nat_num(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    print('Sum of natural number till',n,'is',sum)
sum_nat_num(num)