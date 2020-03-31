#============================================================
#   Sho Tanaka                   CMP112-E
#   Due Oct. 1, 2019
#   Assign-07                    pgm: TestAvg
#============================================================

print("-------- Welcome to Test Average ---------")

#---------------- get inputs --------------------------------
print()
fName    = input("Enter your name: ")
testScore1 = int( input("Enter your score for test-1 : ") )
testScore2 = int( input("Enter your score for test-2 : ") )
testScore3 = int( input("Enter your score for test-3 : ") )

#---------------- calc cost ---------------------------------
testAvg =(testScore1 + testScore2 + testScore3)/3

#------------ o/p -------------------------------------------
print()
print("       >>> Test Summary <<<")
print("    Student name : ", fName)
print("    Test scores  : ", testScore1, testScore2, testScore3)
print("    Test average : ", testAvg)

#----------------- pgm ended---------------------------------
print()
print("------------Pgm Ended -------------")
