num1=0
num2=0
num3=0
avg=0
set=[1,2,3,4,5,6,7,8,9,10]
l=len(set)
i=0
while(i<=l-3):
    num1=set[i]
    num2=set[i+1]
    num3=set[i+2]
    avg=(num1+num2+num3)/3
    print(avg, end='  ')
    i=i+1





