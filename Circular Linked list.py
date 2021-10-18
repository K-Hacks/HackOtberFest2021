class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CircuarLL:
    def __init__(self):
        self.head=None

    def inatEnd(self,newnode):
        temp=self.head
        if self.head is None:
            self.head=newnode
            temp=self.head
            print("The Element ", temp.data, " is added")
        else:
            while True:
                if temp is None:
                    break
                temp=temp.next
            temp = newnode
            print("The Element ",temp.data," is added")
            del temp
    def display(self):
        temp=self.head
        if self.head is None:
            print("Sorry the Circular linked list is Empty !")
        else:
            while True:
                if temp is None:
                    break
                print(temp.data)
                temp=temp.next
            del temp

circularll=CircuarLL()
while True:
    print("1.Insert at Beg")
    print("2.Insert at End")
    print("3.Insert at Mid")
    print("4.Delete at Beg")
    print("5.Delete at End")
    print("6.Delete at Mid")
    print("7.Display")
    print("8.Exit")
    choice=input("Enter your Choice")
    if choice=="2":
        element=input("Enter the Element")
        n=Node(element)
        circularll.inatEnd(n)
    if choice=="7":
        circularll.display()