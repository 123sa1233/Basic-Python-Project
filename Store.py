#General store
print("       Genral Store          ")
print()
print("         welcome               ")
print()

#List
print("1.Vegetables")
print("2.Choclates")
print("3.Pen")


a=int(input("Enter Code No. From above List:"))
b=int(input("enter quantity:"))

class Store():
        def __init__(self,Vegetables,Choclates,Pen):
                self.Vegetables=Vegetables
                self.Choclates=Choclates
                self.Pen=Pen
available=Store(45,86,25)
k=available.Vegetables
l=available.Choclates
m=available.Pen


if a==1:
        if b<=45 and b>=1:
                print("Do online payement of Rs ",35*b)
                print("Thank You, Payment Sucessfull")
                print("collect your vegetable of quantity",b, "from counter 1")
        elif b>45:
                print("Unavailable only 45 quantity available")
        elif b<0:
                print("Invalid Quantity ")
elif a==2:
        if b<=86 and b>=1:
                        print("Do online payement of Rs ",50*b)
                        print("Thank You, Payment Sucessfull")
                        print("collect your Choclates of quantity",b, "from counter 2")
        elif b>86:
                print("Unavailable only 86 quantity available")
        elif b<0:
                print("Invalid Quantity ")
elif a==3:
        if b<=25 and b>=1:
                                print("Do online payement of Rs ",10*b)
                                print("Thank You, Payment Sucessfull")
                                print("collect your pen of quantity",b, "from counter 3")
        elif b>25:
                print("Unavailable only 45 quantity available")
        elif b<0:
                print("Invalid Quantity ")