pin=(input("Enter ur pin: "))
bal=1000
i=1
    
# if len(pin)!=4 or pin.isdigit():
#         print("Pin should be a 4 digit number")
#         exit()

pin=int(pin)
if pin==7373:
        print("Enter 1 for Check bank balance: ")
        print("Enter 2 for Deposite: ")
        print("Enter 3 for Withdraw: ")

else:
        while i<=2:
                print("Wrong password!!!!")
                pin=int(input("Enter ur pin: "))
                if pin==7373:
                        print("Enter 1 for Check bank balance: ")
                        print("Enter 2 for Deposite: ")
                        print("Enter 3 for Withdraw: ")
                        break
                i+=1
        print("atm card blocked ")
        exit()





choice=int(input("Enter here:"))
if choice==1:
        print("Bank balance is : ",bal)

if choice==2:
        depos=float(input("Enter deposite amount: "))
        if depos>=600 and depos%50==0:
                bal+=depos
                print("new balance is:",bal)
        

if choice==3:
        withd=int(input("Enter withdraw ammount: "))
        if withd>=100 and withd%100==0:
                bal-=withd
                print("new balance is:",bal)
                

        