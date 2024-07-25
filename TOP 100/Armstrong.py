#here we have to find out the length of the input number because we have to find out the power of that every digit where power will be the length of the given number.suppose a=1123432 here length of number is 7, we have to calculate every digit's to the power 7.
a=int(input("Entre a number: "))
temp=a
x=len(str(a))  
i=0
while a>0:
    rem=a%10
    i=i+(rem**x)
    a=a//10
if temp==i:
    print("Armstrong")
else:
    print("not Armstrong")