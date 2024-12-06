# abundant means sum of factors of a number should greater than the given nuber
a=int(input("enter a number: "))
i=0
for j in range(1,a):
    if a%j==0:
        i+=j
if i>a:
    print("abundant")
else:
    print("not......") 