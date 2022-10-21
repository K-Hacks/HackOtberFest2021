def pairsum(List1, target):
    i = 0
    j = len(List1)-1
    while(i<j):
        sum_pair =List1[i]+List1[j]
        if(sum_pair==target):
            return True
        elif sum_pair<target:
            i+=1
        else:
            j-=1
    return False


List1 = [1,2,3,4,5]
target = 9
print(pairsum(List1,target))
