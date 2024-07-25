#palindrome
a=int(input("Entre a number: "))
tem=a
x=len(str(a))
y=0
while a!=0:
    rem=a%10
    arm=rem**x
    y+=arm
    a=a//10
if tem==y:
    print("armstrong")
else:
    print("not.....")