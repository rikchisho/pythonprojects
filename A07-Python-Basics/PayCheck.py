#============================================================
#   Sho Tanaka                   CMP112-E
#   Due Oct. 1, 2019
#   Assign-07                    pgm: PayCheck
#============================================================

print("-------- Welcome to Pay Check ---------")

#---------------- get inputs --------------------------------
fName    = input("Enter your name: ")
payHours = int( input("Enter the hours you worked : ") )
payRate  = float( input("Enter your hourly rate     : ") )

#---------------- calc cost ---------------------------------
payCheck = payHours * payRate

#------------ o/p -------------------------------------------
print()
print(">>> Pay Summary <<<")
print(fName, "worked ", payHours, "hours")
print("Hourly rate:  ", payRate)
print("Pay check: $", payCheck)

#----------------- pgm ended---------------------------------
print()
print("------------Pgm Ended -------------")
