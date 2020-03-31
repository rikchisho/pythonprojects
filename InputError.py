print("--------Welcome to input Error---------")

#------------------------ get inputs ---------------
fName    = input("enter name         : ")
phoneMin = input("enter num of min   : ")
minPrice = input("enter price per min: ")

#------------ calc cost ------------
#cost = phoneMin + minPrice    # Error Concat
cost = phoneMin * minPrice

#------------ o/p ----------
print()
print("cost :", cost)

