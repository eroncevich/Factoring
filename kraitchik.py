import math
import sys

b = 4 # number of primes needed.

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
pmatrix = []
pvals = []

def bfactorable (n):
    global b
    if n == 1:
        return True
    for i in range(0,b):
        if (n % primes[i]) ==0:
            return bfactorable (n / primes[i])
    return False

def bfactor (n,arr):
    global b
    if n==1:
        return arr
    for i in range(0,b):
        if (n %primes[i])==0:
            arr[i]+=1
            return bfactor(n / primes[i], arr)
    return None


# this function will go through, select one of the b+1 rows, xor with other rows, and rref2
# the other rows. Either the rref2 will have:
# 1. a row of all 0's, so linearly dependent ( so subset sum =0)
# 2. all rows have 1's, so independent, (but in this case we repeat with another row which should be dependent)

def subsetsum2 ( m):
    for i in range (0,len(m)):
        tempm = []
        for j in range (0, len(m)):
            if i==j:
                continue
            tempm.append(map(lambda x,y: x ^ y , m[i],m[j]))
        print tempm

def rref2(m):
    f

# takes as input n and returns first found factors
# returns tuple of factors or empty tuple if prime
def factor(n):
    global b
    a0 = int (math.ceil(math.sqrt (n)))
    i=a0
    while len(pvals)<b+1:
        qx = int ((i*i)% n)
        #print qx
        if not bfactorable(qx):
            i+=1
            continue
        parr = bfactor (qx, [0]*b)
        pvals.append (qx)
        pmatrix.append (map (lambda x: x%2,parr))
        i+=1
        #print i, parr
    #print "hi", a0
    subsetsum2 ( pmatrix)


if len(sys.argv) < 2:
    print "error: needs 1 argument "
    print "python bruteforce.py [integer]"
    exit()

#print sys.argv[1]
#print bfactorable (75)
#print bfactorable (168)
#print bfactorable (360)
#print bfactorable (560)


print factor(float(sys.argv[1]))
print pvals
print pmatrix