import math
import sys

#difference of squares works by finding n=p*q
#p = (a-b)
#q = (a+b)
c = 100

def isSquare(n):
#    global c
#    c-=1
#    if c==0:
#        exit()
    root = math.sqrt (n)
    return root == int (root)
# takes as input n and returns first found factors
# returns tuple of factors or empty tuple if prime
def factor(n):
    if n% 2 ==0:
        return (2, int (n/2))
    a = int (math.ceil(math.sqrt (n)))
    print "Start a:", a
    b2 = a*a - n
    while not isSquare (b2):
        a = a+1
        b2 = a*a - n
        #print a,b2
    b = int (math.sqrt (b2))
    return (a-b,a+b)

if len(sys.argv) < 2:
    print "error: needs 1 argument "
    print "python bruteforce.py [integer]"
    exit()

#print sys.argv[1]
print factor(float(sys.argv[1]))
