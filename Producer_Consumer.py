global mutex,empty,full
def wait(find):
    if find == "empty":
        global empty
        empty-=1
    elif find == "mutex":
        global mutex
        mutex-=1
    elif find == "full":
        global full
        full-=1
def signal(find):
    if find == "empty":
        global empty
        empty += 1
    elif find == "mutex":
        global mutex
        mutex += 1

    elif find == "full":
            global full
            full += 1
n = int(input("Enter buffer size: "))
buffer = []
mutex=1
empty=n
full=0
while(1):
    print("1. Produce\t\t2.Consume\t\t3.Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        if(mutex==1 and empty!=0):
            print("Enter the value: ") 
            wait("empty")
            wait("mutex")
            buffer.append(input())
            signal("mutex")
            signal("full")
        else:
            print("BUFFER IS FULL")
    elif(choice == 2):
        if(full>0 and mutex==1):
            wait("full")
            wait("mutex")
            print("THE CONSUMED VALUE IS "+str(buffer.pop(len(buffer)-1))) 
            signal("mutex")
            signal("empty")
        else:
            print("BUFFER IS EMPTY")
    elif(choice == 3):
        break
    else:
        print("**Invalid input**")
