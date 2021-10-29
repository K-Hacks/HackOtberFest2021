class Node:
    def __init__(self, data):
        self.data=data
        self.next=None


class Linkedlist:
    def __init__(self):
        self.front=None
        self.rear=None

    def lenght(self):
        temp=self.front
        lenght=0
        while(temp is not None):
            lenght=lenght+1
            temp=temp.next
        return lenght


    def enqueue(self,newdata):
        newnode=Node(newdata)
        if(self.front==None):
            self.front=self.rear=newnode
            print("The Element ", newdata, "is sucessfully Enqueued")
            print("------------------------------")
        else:
            self.rear.next=newnode
            self.rear=newnode
            print("The Element ", newdata, "is sucessfully Enqueued")
            print("------------------------------")

    def dequeue(self):
        if(self.front is None):
            self.rear=None
            print("Queue is Underflow!Deletion is not possible")
            print("------------------------")
        else:
            temp=self.front
            self.front=temp.next
            print("The Element ", temp.data, "is sucessfully Dequeued")
            print("------------------------------")
            del temp



    def display(self):
        if(self.front is None):
            print("Queue is Empty!Nothing to Display")
            print("------------------------")

        else:
            temp=self.front
            while(temp is not None):
                print(temp.data)
                temp=temp.next
            print("------------------------")


    def frontelement(self):
        if(self.front is None):
            print("Queue is Underflow!Front Element is Not Found")
            print("------------------------")
        else:
            temp=self.front
            print("The Front Element is: ",temp.data)
            print("------------------------")

    def rearelement(self):
        if self.front is None:
            self.rear=None
        if(self.rear is None):
            print("Queue is Underflow!Rear Element is Not Found")
            print("------------------------")

        else:
            temp=self.rear
            print("The Rear Element is: ",temp.data)
            print("------------------------")

    def isempty(self):
        if(self.front is None):
            print("Queue is Empty")
            print("------------------------")
        else:
            print("Queue is Not Empty with",self.lenght(),"Elements")
            print("------------------------")

queue=Linkedlist()
while True:
    print("Select your choice")
    print("1.ENQUEUE")
    print("2.DEQUEUE")
    print("3.DISPLAY")
    print("4.FRONT ELEMENT")
    print("5.REAR ELEMENT")
    print("6.IS EMPTY")
    print("7.EXIT")
    ch = input("Enter your choice :")
    if ch == "1":
        newdata = input("Enter the element :")
        queue.enqueue(newdata)

    elif ch == "2":
        queue.dequeue()

    elif ch == "3":
        queue.display()

    elif ch == "4":
        queue.frontelement()

    elif ch == "5":
        queue.rearelement()

    elif ch == "6":
        queue.isempty()

    elif ch=="7":
        break
    else:
        print("Invalid Choice!!Select any other option")
        print("----------------------")

