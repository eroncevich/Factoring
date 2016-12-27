import math
import sys
# takes as input n and returns first found factors
# returns tuple of factors or empty tuple if prime
def factor(n):
    max_steps = int (math.floor(math.sqrt (n)))
    print "Max steps:", max_steps
    for i in range(2,max_steps):
        if (n % i) == 0:
            return (i,int (n / i))
    return (0,0)

if len(sys.argv) < 2:
    print "error: needs 1 argument "
    print "python bruteforce.py [integer]"
    exit()

#print sys.argv[1]
print factor(float(sys.argv[1]))
