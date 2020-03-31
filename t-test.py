# this program performs a t-test on a list of numbers
# Two-tailed test

from scipy.stats import *
from numpy import *

file = input("What is the file name? ")
list = loadtxt(file)
print()

avg = eval(input("what is the assumed mean? "))
print()

alpha = eval(input("what is alpha? "))
print()

t, p = ttest_1samp(list, avg)

print("the t-score is {} and the p-value is {}.".format(t, p))
print()

if p < alpha:
    print("Since the p-value is less than alpha, we reject Ho.")
else:
    print("Since the p-value is greater than alpha, we do not reject Ho.")
    
print()

print("End.")
