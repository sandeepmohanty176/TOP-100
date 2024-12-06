# automorphic 25 625
a=int(input("Enetr any number: "))
b=int(input("Enetr any number: "))
for i in range(a,b):
    c=i**2
    d=str(c)
    e=str(i)
    if d.endswith(e):
        print(i,"square is",i**2)
