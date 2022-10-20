def mult():
    in1=input("Please Enter a Name: ")
    print("Hello ",in1)
    num1=int(input("Insert a number: "))
    num2=int(input("Insert another number: "))
    print("Multiplying...")
    prd=num1*num2
    print("The product of the given numbers is ",prd)

    new_in=input(("Would you like to try again (Y/N): "))
    if new_in in ["Y","y"]:
        mult()
    elif new_in in ["N","n"]:
        print("Thank you")

    else:
        print("Error")
mult()
