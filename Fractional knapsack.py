class Itemofknapsack:
    def __init__(self,wt,val,ind):
        self.wt=wt
        self.val=val
        self.ind=ind
        self.cost=val/wt

    def __lt__(self, other):
        return self.cost < other.cost

class Fractionalknapsack:
    def highprofit(wt,val,capacity):
        ratio=[]
        for i in range(len(wt)):
            temp=Itemofknapsack(wt[i],val[i],i)
            ratio.append(temp)

        ratio.sort(reverse=True)

        totalprofit=0
        for i in ratio:
            currentwt=int (i.wt)
            currentval=int (i.val)
            if capacity-currentwt>=0:
                capacity-=currentwt
                totalprofit+=currentval
            else:
               fraction = capacity / currentwt
               totalprofit += currentval * fraction
               capacity = int(capacity - (currentwt * fraction))
               break
        return totalprofit



wt=list(map(int,input("Enter the Weight\n").split()))
value=list(map(int,input("Enter the Value of the Weight\n").split()))
cap=int(input("Enter the Capacity of the Knapsack:"))
profit=Fractionalknapsack.highprofit(wt,value,cap)
print("The Maximum Profit is: ",profit)

