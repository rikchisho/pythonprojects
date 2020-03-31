#-------------------------------------------------------
# This program computes descriptive stats
#     (it is the "starting" pgm that only provides the
#       lines that print the information)
#--------------------------------------------------------

#----- 1.  Bring into this pgm the Python number library ------
from numpy import *

#---- 2. Ask user for the file they would like to process --------
dataSet=input("Enter name of file: ")

#--- 3.  Alter the users I/P so this pgm can process it ---
list=loadtxt(dataSet)


#----4. (a) Display back to user the data set being processed---
#----   (b) display the Stats

print( "\n======== Descriptive Stats =============\n")
print( "For FILE:  ")        #display fileName
print()
print("   Count:  ", len(list) ) 
print("   Sum:    ", sum(list) )
print("   Mean:   ", mean(list) )
print("   Mean:   ", round(mean(list), 2))
print("   Median: ", median(list))  
print()
 
print("   Population: std dev : ", std(list))         #population std dev
print("                         ", round(std(list), 4) )  
print("              variance : ", var(list) )         #populaton  variance
print("                         ", var(round(var(list), 4)) )  
 

print()
print("   Sample:     std dev : ", std(list, ddof=1) )        #sample std dev 
print("              variance : ", var(list, ddof=1) )        #sample  variance
print()


print("------- 5-Number  Summary ----------------")
print("\t Min           : ", min(list) )
print("\t Max           : ", max(list) )
print("\t 1st quartile  : ", percentile(list, 25) )
print("\t median        : ", percentile(list, 50) )
print("\t 3rd quartile  : ", percentile(list, 75) )


print()
print("....  END ......." )
print()

