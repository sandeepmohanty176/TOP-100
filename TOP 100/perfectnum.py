#sumof its divisor should equals to the num
a=int(input("Enter a number: "))
i=1
j=0
while a>0 and i<a:
    if a%i==0:
        j+=i
    i+=1
if j==a:
    print("perfect")
else:
    print("not")
