#means number should multiple of a same nuber e.g 25 is the multiple of 5 and 5
n=int(input("enter a nuber: "))
i=1
j=1
while i<n and j<n:
    if i*j==n:
        print("perfect square")
        exit()
    i+=1
    j+=1
else :
    print("not.....")