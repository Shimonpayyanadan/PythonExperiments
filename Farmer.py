legs = eval(input("Enter the number of legs : "))
heads = eval(input("Enter the number of heads : "))
h = 0
p = 0
while (h < 100):
    while (p < 100):
        if ((h + p == heads) & ((4 * p) + (2 * h) == legs)):
            print("There are "+ str(h) + " hens and " + str(p) + " pigs")
            exit()
        p = p + 1
    h = h + 1
    if(h==100):
        print("Invalid Data. Please Retry")
    p=0

