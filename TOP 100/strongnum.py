#strong number means if we give a number the the sum of the factorial should equalsto that given nmber
from math import factorial
a=int(input("enter a number: "))
temp=a
b=0
while a!=0:
    rem=a%10
    fact=factorial(rem)
    b=b+fact
    a=a//10
if temp==b:
    print("strong")
else:
    print("not strong")