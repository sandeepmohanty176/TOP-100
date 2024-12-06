# abundant means sum of factors of a number should greater than the given nuber
a=int(input("enter a number: "))
for j in range(1,a):
    i=0
    for m in range(1,j):
        if j%m==0:
            i+=m
    if i>j:
        print(j,end=" ")
        