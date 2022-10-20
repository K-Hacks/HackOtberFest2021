n = int(input("Please enter the number of terms:"))
fsum = 0; tsum = 0; term = 1
for i in range(1, n + 1):
    if (i % 5 == 0):
        fsum = fsum + tsum
        print ("At i= ",i," Adding tsum =", tsum)
        tsum = 0
    else:
        fsum = fsum + term
        tsum = tsum + term
        print ("At i=",i,"Adding ordinary term =", term)
        term = term + 1

print ("So the final sum of the series is", fsum)
print ("End of the program...")
