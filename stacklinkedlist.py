class Node:
    def _init_(self, data):
        self.data=data
        self.next=None


class Linkedlist:
    def _init_(self):
        self.head=None

    def lenght(self):
        temp=self.head
        lenght=0
        while(temp is not None):
            lenght=lenght+1
            temp=temp.next
        return lenght

    def push(self,newdata):
        newnode = Node (newdata)

        if self.head is None:
            self.head=newnode
            print("The Element ",newdata,"is sucessfully pushed")
            print("------------------------------")

        else:
            newnode.next=self.head
            self.head=newnode
            print("The Element ", newdata, "is successfully pushed")
            print("------------------------------")

    def pop(self):
        if self.head is None:
            print("Stack is Underflow! Deletion is not possible")
            print("------------------------------")
        else:
            temp=self.head
            self.head=temp.next
            print("The Element",temp.data,"is successfully poped")
            print("------------------------------")
            del temp

    def display(self):
        temp = self.head
        if self.head is None:
            print("Stack is Empty!! Nothing to display")
            print("------------------------------")

        else:
            while(temp is not None):
                print(temp.data)
                temp=temp.next
            print("------------------------------")

    def topelement(self):
        temp = self.head
        if self.head is None:
            print("Stack is Empty!! There is No top element")
            print("------------------------------")
        else:
            print("The Top Element is :",end=" ")
            print(temp.data)
            print("------------------------------")

    def empty(self):
        if self.head is None:
            print("Stack is Empty")
            print("------------------------------")
        else:
            print("Stack is Not empty and it has ",self.lenght(),"elements")
            print("------------------------------")


stack=Linkedlist()
while True:
    print("Select your choice")
    print("1.PUSH")
    print("2.POP")
    print("3.DISPLAY")
    print("4.TOP ELEMENT")
    print("5.IS EMPTY")
    print("6.EXIT")

    ch=input("Enter your choice :")
    if ch=="1":
        newdata=input("Enter the element :")
        stack.push(newdata)

    elif ch == "2":
        stack.pop()

    elif ch=="3":
        stack.display()

    elif ch =="4":
        stack.topelement()

    elif ch=="5":
        stack.empty()

    elif ch=="6":
        break
    else:
        print("Invalid Choice!!Select any other option")
        print("----------------------")
