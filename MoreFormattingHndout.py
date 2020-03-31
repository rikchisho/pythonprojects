# --------------------------------------------------------
#  pgm Demos:  (a) tabs   and (b) rounding  (c) int vs float
#   rounding:  round( varName, numOfDecimals)
#   i/p:   243mi   11.4 gal
# ---------------------------------------------------------

print( "-------- Car Efficiency --------------") 
print()
miles = float( input("enter miles driven: ") )
gals  = float( input("enter gals of gas : ") )

#----------- calcuations ---------------------
mpg = miles / gals

#------------ summary report----------------------
print()
print( "\t - - - - summary - - - -")
print( "\t Miles :", miles)
print( "\t Gas   :", gals)
print()
print( "\t MPG   :", mpg)
print( "\t MPG   :", round(mpg, 4))
print( "\t MPG   :", round(mpg, 1))

print()
print( "....  END .......")
print()

