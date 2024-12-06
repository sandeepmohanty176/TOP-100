# harshad means num should divisible by sum of the digit eg 21 is divisible by 2+1=3
a=int(input())
temp=a
b=0
while a!=0:
    rem=a%10
    b+=rem
    a=a//10
    
if temp%b==0:
        print("Harshad Number ")
else:
        print("Not...")    