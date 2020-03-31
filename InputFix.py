print("--------Welcome to input ---------")

#------------------------ get inputs ---------------
fName    = input("enter name         : ")
phoneMin = float( input("enter num of min   : ") )
minPrice = float( input("enter price per min: ") )

#------------ calc cost ------------
cost = phoneMin * minPrice 

#------------ o/p ----------
print()
print("cost : $", cost)

