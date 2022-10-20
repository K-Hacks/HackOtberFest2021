num_one = int(input("Enter 1st number: "))

op = input("Enter operator: ")

num_two = int(input("Enter 2nd number: "))

if op == "+":
    print(num_one + num_two)
elif op == "-":
    print(num_one - num_two)
elif op == "*" or op == "x":
    print(num_one * num_two)
elif op == "/":
    print(num_one / num_two)