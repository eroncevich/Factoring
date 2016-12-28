import math
import sys

b = 4 # number of primes needed.

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def bfactorable (n):
    global b
    if n == 1:
        return True
    for i in range(0,b):
        if (n % primes[i]) ==0:
            return bfactorable (n / primes[i])
    return False

# takes as input n and returns first found factors
# returns tuple of factors or empty tuple if prime
def factor(n):
    print "hi"


if len(sys.argv) < 2:
    print "error: needs 1 argument "
    print "python bruteforce.py [integer]"
    exit()

#print sys.argv[1]
print bfactorable (75)
print bfactorable (168)
print bfactorable (360)
print bfactorable (560)


print factor(float(sys.argv[1]))
