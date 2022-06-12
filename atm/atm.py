def auth():
    global cardNumber
    global pin
    cardNumber = input("Please enter your card number: ")
    pin = input("Please enter your pin: ")

auth()    
a=len(cardNumber)
b=len(pin)
def services():
    print("please enter-")
    print("b = BalanceEnquiry")
    print("c = change pin")
    print("e = exit")
    global si
    si=input("here: ")    
    if(si=="b"):
        print("your current balance is ₹1200.00")
    if(si=="c"):
        oldPin=input("Please enter your old pin: ")    
        if(oldPin==pin):
            input("enter your new pin: ")
            print("the pin changed sucessfullly :)")       
        else:
            print("wrong card number or pin")     
    if(si=="e"):
        print("thank you :)")
        auth()      
if(int(a)>10):
    print("wrong card number or pin")
    r=input("enter e to exit: ")
    if(r=="e"):
        auth()
if(int(a)<10):
    print("wrong card number or pin")    
    r=input("enter e to exit: ")
    if(r=="e"):
         auth()
if(int(b)>4):
    print("wrong card number or pin")
    r=input("enter e to exit: ")
    if(r=="e"):
        auth()
if(int(b)<4):
    print("wrong card number or pin")      
    r=input("enter e to exit: ")
    if(r=="e"):
        auth()
else:
    services()


