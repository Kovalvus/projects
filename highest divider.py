a = 0
x = 0

while (a == 0):
    i = 1
    if (x!="end"):
        x = input('Write "end" to stop, \nEnter a number: ')
    try:
        if x == "end":
            exit()
        else:
            x = int(x)
        while (i != x):
            if (x % i == 0):
                print("Number",x,"is dividable by:",int(x/i), "Quotient:", i)
                i = i+1
            else:
                i=i+1
    except:
        Exception
    