
bid = {}
finish = False
while not finish: 
    name= input("enter your name :")
    price = input("enter the price : $")
    bid[name] = price
    repeat = input("enter yes to continue no to end :").lower
    if repeat == "no":
        finish = True
    elif repeat == "yes":
        os.environ("clear")

