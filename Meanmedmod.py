set=[]

print("Enter the numbers one by one : ")
print("Press ENTER when done")
while True:
    num=input()

    if (num==""): #To stop input
        break
    set.append(num)
l=len(set)


def mean(int):
    sum=0
    i=0
    for i in range(0,l):
        sum=sum+eval(set[i])
    mean.meann=sum/l
    print("The mean is: ",mean.meann)

def median(int):
    rem=l%2
    pos=int(l/2)
    if(rem==0):
        med=int(set[pos-1])+int(set[pos])
        mediann=med/2
    if(rem==1):
        pos=int(l/2)
        mediann=set[pos]

    print("The median is :",mediann)


def mode(int):
    smv=0
    i=0
    while(i<l):
        smv=smv+int(set[i])**2
        i=i+1
    t=smv/l
    variance=t-mean.meann**2

    print("The variance is :",variance)



mean(int)
median(int)
mode(int)
