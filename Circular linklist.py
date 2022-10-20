class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def lenght(self):
        temp=self.head
        length=0
        while True:
            length=length+1
            temp=temp.next
            if temp == self.head:
                break
        return length

    def insertbeg(self,newdata):
        newnode=Node(newdata)

        if self.head==None:
            self.head=newnode
            newnode.next=self.head
            print("Node Inserted")
            print("------------------------")
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            newnode.next=self.head
            temp.next=newnode
            self.head=newnode
            print("Node Inserted")
            print("------------------------")


    def insertend(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            newnode.next=self.head
            print("Node Inserted")
            print("------------------------")

        else:
            temp=self.head
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=newnode
            newnode.next=self.head
            print("Node Inserted")
            print("------------------------")

    def insertpos(self,newdata,pos):
        newnode=Node(newdata)
        temp=self.head
        if pos <= 0 or pos > self.lenght():
            print("Invalid position! Please select another position")
        else:
            i=0
            while (i != pos):
                temp = temp.next
                i = i + 1
            newnode.next = temp.next
            temp.next = newnode
            print("Node Inserted")
            print("------------------------")



    def deletebeg(self):
        temp = self.head
        if self.head is None:
            print("List is Empty!! Deletion is not possible!")
        else:
            if temp.next==self.head:
                self.head=None
                del temp
                print("Node Deleted")
                print("------------------------")
            else:
                new=temp.next
                while (temp.next != self.head):
                    temp=temp.next
                temp.next = new
                self.head=new
                del temp
                print("Node Deleted")
                print("------------------------")

    def deletelast(self):
        if self.head is None:
            print("List is Empty!! Deletion is not possible!")
        else:
            t = self.head
            if t.next is self.head:
                del self.head.next
                self.head=None
                print("Node Deleted")
                print("------------------------")

            else:
                temp=self.head
                while(temp.next is not self.head):
                    previousnode=temp
                    temp=temp.next
                del temp.next
                previousnode.next=self.head
                print("Node Deleted")
                print("------------------------")

    def deletepos(self,pos):

        if self.head is None:
            print("List is Empty!! Deletion is not possible!")
        else:
            if pos <= 0 or pos > self.lenght():
                print("Invalid position! Please select another position")
            else:
                temp=self.head
                currentpos=0
                while(currentpos!=pos):
                    previousnode=temp
                    temp=temp.next
                    currentpos+=1
                previousnode.next=temp.next
                print("Node Deleted")
                print("------------------------")

    def search(self):
        temp=self.head
        if self.head is None:
            print("List is Empty!! Search is not possible!")
        else:
            n=input("Enter the Element to be searched : ")
            i=0
            while True:
                if temp.data== n:
                    print("Element Found , Position is ",i)
                    print("-------------------------------")
                    flag=0
                    break
                else:
                    flag=1
                temp=temp.next
                i+=1
                if temp == self.head:
                    break
            if flag==1:
                print("Element not found")
                print("------------------------")

    def printlist(self):
        temp=self.head
        if temp is None:
            print("List is empty!!!")
        else:
            while True:
                print(temp.data)
                temp = temp.next
                if temp==self.head:
                    break
            print("------------------------")

list1=Linkedlist()
while True:
    print("Enter your choice : ")
    print("1.Insert")
    print("2.Delete")
    print("3.Search")
    print("4.Display")
    print("5.Exit")
    ch=int(input("Enter a choice : "))
    if ch==1:
        print("Enter which position you want to Insert")
        print("1.Insert at front")
        print("2.Insert at End")
        print("3.Insert at Deseried position")
        a=int(input("Enter a choice : "))
        if a==1:
            newdata=(input("Enter a element : "))
            list1.insertbeg(newdata)
        elif a==2:
            newdata = (input("Enter a element : "))
            list1.insertend(newdata)
        elif a==3:
            pos = int(input("Enter the position to insert : "))
            newdata = (input("Enter a element : "))
            list1.insertpos(newdata,pos)
        else:
            print("Invalid choice")
    elif ch==2:
        print("Enter at which position you want to delete")
        print("1.Delete at front")
        print("2.Delete at End")
        print("3.Delete at Deseried position")
        b=int(input("Enter a choice : "))
        if b==1:
            list1.deletebeg()
        elif b==2:
            list1.deletelast()
        elif b==3:
            pos = int(input("Enter the position to delete : "))
            list1.deletepos(pos)
        else:
            print("Invalid Choice")
    elif ch==3:
        list1.search()
    elif ch==4:
        list1.printlist()
    elif ch == 5:
        break
    else:
        print("Invalid Choice")

