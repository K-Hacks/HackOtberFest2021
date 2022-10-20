#!/usr/bin/env python3

#This is a program to togle cases in a String

original = input("Enter a String : ")
new_string = ""

#toggle loop
for x in range (len(original)):
    if (original[x]>='a' and original[x] <= 'z'):
        new_string = new_string + chr((ord(original[x])-32))
    elif (original[x]>='A' and original[x] <= 'Z'):
        new_string = new_string + chr((ord(original[x])+32))
    else:
        new_string = new_string +original[x]

print("The original String is : " + original)
print("The new String is      : " + new_string)
