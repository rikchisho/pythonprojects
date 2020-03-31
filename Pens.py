print("--------Welcome to Pens ---------")

#------------------------ get inputs ---------------
penPrice = float( input("enter price of pen   : ") )
penQty   = float( input("enter number of pen  : ") )
fName    = input("enter color you want:    ")

#------------ calc cost ------------
penCost = penPrice * penQty 

#------------ o/p ----------
print()
print("buying Pens")
print("     price: ", penPrice)
print("     quantity:  ", penQty)
print("------------------------")

print("     cost : $", penCost)

