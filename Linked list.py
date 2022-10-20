class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def lenght(self):
        curnode=self.head
        lenght=0
        while curnode is not None:
            lenght=lenght+1
            curnode=curnode.next
        return lenght
    def insertbeg(self,data):
        temp=self.head
        self.head=data
        self.head.next=temp
        del temp
    def insertat(self,data,position):
        temp_data=data
        if position < 1 or position > self.lenght():
            print("Invalid position")

        else:
            startnode = self.head
            tempvalue=0
            while True:
                if tempvalue==position:
                    previousnode.next=data
                    data.next=startnode
                    break
                previousnode=startnode
                startnode=startnode.next
                tempvalue+=1
    def insertend(self,newnode):
        if self.head is None:
            self.head=newnode
            
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode =lastnode.next
            lastnode.next=newnode  

    def delfirst(self):
        if self.head is None:
            print("List is Already empty")
        else:
            temphead=self.head
            self.head=self.head.next    
    def delat(self,position):
        #1->3
        if position==0:
            self.delfirst()
        else:
            currentnode=self.head
            cp=0
            while True:
                if cp==position:
                    previousnode.next=currentnode.next
                    break  
                previousnode=currentnode
                currentnode=currentnode.next
                cp=cp+1
    def delend(self):
        if self.head is None:
            print("List is Already empty")
        elif self.head.next is None:
            self.head=None
        else:
            last_node=self.head
            while last_node.next is not None:
                pre_node=last_node                  
                last_node=last_node.next
            pre_node.next = None
    def display(self):
        
        if self.head is None:
            print("list is empty")
        else:
            print("--------")  
            cn=self.head
            while True:
                if cn is None:
                    break
                
                print(cn.data)
                cn=cn.next
            print("--------")
    def search(self):
        element=input("Enter the element : ")
        count=0
        cur_node=self.head
        tempc=0
        for i in range(0,self.lenght()):
            if element==cur_node.data:
                print("The element ",element," found at the position ",count)
                tempc+=1
                break
            count+=1
            cur_node=cur_node.next
        if tempc==0:
            print("The Element Not found")



linkedlist=Linkedlist()
while True:
    
    print("1.Insert \n2.Delete \n3.Search \n4.Display \n5.Exit")
    get=input("Enter your Choice : ")
    if get=="1":
        print("1.Insert First \n2.Insert at mid \n3.Insert End")
        get1=input("Enter the Insert choice : ")
        if get1=="1":
            i1=input("Enter the element : ")
            n=Node(i1)
            linkedlist.insertbeg(n)
        elif get1=="2":
            i2=input("Enter the element : ")
            i3=int(input("Enter the position : "))
            n1=Node(i2)
            linkedlist.insertat(n1,i3)
        elif get1=="3":
            i4=input("Enter the element : ")
            n2=Node(i4)
            linkedlist.insertend(n2)
        else:
            print("Wrong Choice")
    elif get=="2":
        print("1.Delete First \n2.Delete at mid \n3.Delete End")
        get2=input("Enter yout choice : ")
        if get2=="1":
            linkedlist.delfirst()
        elif get2=="2":
            i5=int(input("Enter the position Want to Be Deleted \n"))
            linkedlist.delat(i5)
        elif get2=="3":
            linkedlist.delend()
        else:
            print("Wrong Choice")
    elif get=="3":
        linkedlist.search()
    elif get=="4":
       linkedlist.display()
    elif get=="5":
        print("thank you")
        break
    else:
        print("Entered Wroung choice")