# this program performs a 2 sample t-test on two lists of numbers
# Two-tailed test
# Assumes equal variances

from scipy.stats import *
from numpy import *

file = input("What is the file name? ")
list1, list2 = loadtxt(file, unpack = True)
print()

alpha = eval(input("what is alpha? "))
print()

t, p = ttest_ind(list1, list2)

print("the t-score is {} and the p-value is {}.".format(t, p))
print()

if p < alpha:
    print("Since the p-value is less than alpha, we reject Ho.")
else:
    print("Since the p-value is greater than alpha, we do not reject Ho.")
    
print()

print("End.")
