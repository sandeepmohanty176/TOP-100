# automorphic nmber means suppose numb=5 square is 25 ends with 5 which is number it self so its a automorphic number
m=int(input("Enter a number: "))
n=str(m)
o=m**2
p=str(o)
if p.endswith(n):
    print("yes")
else:
    print("no....")