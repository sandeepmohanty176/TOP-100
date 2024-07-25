a=int(input("Enter a Number: "))
temp=a  #here we store the value of a in a temp variable because in last step of while loop the value of n becomes 0.so the the value of n in the if statement will be cosidered as 0.in this case code will not work properly. 
x=0
while a>0:
    b=a%10
    x=(x*10)+b
    a=a//10
if temp==x:
    print("palindrome")
else:
    print("not palindrome")