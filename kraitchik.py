import math
import sys
import fractions
import random

b = 4 # number of primes needed. This can be anything

#just a list of the first couple of primes
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#sample primes for testing
p1 = 132241
p2 = 670177
p3 = 437867
p4 = 7231210439
p5 = 1691080409
p6 = 1906398731
p7 = 131
p8 = 89
p9 = 29


#sample of semiprimes for testing
n1 = 88624876657 #p1*p2
n2 = 3799 # p7*p9


# given n and array, recursively produce array counting the prime factors
# or return None if not bsmooth.
def bfactor (n,arr):
    global b
    if n==1:
        return arr
    for i in range(0,b):
        if (n %primes[i])==0:
            arr[i]+=1
            return bfactor(n / primes[i], arr)
    return None

# takes in m which is a matrix counting the powers of primes ex (2^x, 3^y, 5^z, ...)
# and counter is the base 2 counter from rref2 which adds up the matrices to get the squared number
# and returns the square root
def addprimes (m, counter):
	#tempm = m[:]
	sum_arr = [0 for i in range (0,len(m[0]))]
	#print m,counter
	for i in range(0, len(counter)):
	    if counter[i]:
	 #       print m[i]
	        sum_arr = map(lambda x,y: x+y, sum_arr, m[i])
	return map(lambda x:x/2, sum_arr)

# this function will go through, select one of the b+1 rows, xor with other rows, and rref2
# the other rows. Either the rref2 will have:
# 1. a row of all 0's, so linearly dependent ( so subset sum =0)
# 2. all rows have 1's, so independent, (but in this case we repeat with another row which should be dependent)

# input is nonnegative integers, and it will transform to F2
def subsetsum2 ( m):
	
    m2 = [] # base 2 matrix version of m
    for i in range (0, len(m)):
        m2.append (map (lambda x: x%2,m[i]))
    print "M2", m2

    for i in range (0,len(m)):
    	print i
        cur_m2 = []
        for j in range (0, len(m2)):
            if i==j:
                continue
            cur_m2.append(map(lambda x,y: x ^ y , m2[i],m2[j]))
        square = rref2 (cur_m2)
        if square: # if the array is not empty, return the counter of m
            print "Found square"
            print "base 2",square
            square.insert(i, int(reduce(lambda x,y: x+y, square, 0) % 2))
            print square
            return square
        
    print "error no root found"
    exit()

# takes in a b*b matrix and returns the subset if 0 found or [] otherwise
# this is just using a type of rref in base 2 which then adds up which rows were used to create
# the final row. If the final row is all 0's, return which rows were used.
def rref2(m):
    c=0
    #print "curr m", m
    
    # create a counter which counts which elements were added to the row when turning to rref
    # This is not the LU decomposition! It simply counts which lines need to be added to make rref
    # should be populated with identity matrix
    counterm = [[0 for i in xrange (len(m))] for j in range (len(m))]
    #print counterm
    for i in range (0, len(m)):
        counterm[i][i] =1
    i=0
    while i < len(m)-1:
    	#print "step m", m
    	#print counterm
    	#print c, i
    	if c == len(m)-1:
            return counterm[len(m)-1]
        if m[i][c] ==0: #first check if 1 in the correct position
            ii = find_next_row (m,i,c)
            if ii<0:
                c+=1
                continue
            else:
                #print "switching", i, ii
                t = m[i]
                countert = counterm[i]
                m[i] = m[ii]
                counterm[i]=counterm[ii]
                m[ii] = t
                counterm[ii]= countert
        if c == len(m)-1:
            return counterm[len(m)-1]
        for j in range (i+1, len(m)):
            if m[j][c]==1:
                m[j] = map(lambda x,y: x ^ y , m[i],m[j])
                counterm[j] = map(lambda x,y: int((x+y)%2), counterm[i],counterm[j])
        c+=1
        i+=1
    #print m
    #print counterm
    if reduce(lambda x,y: x+y,m[len(m)-1],0) ==0:
        return counterm[len(m)-1]
    else:
        return []

#finds row in m where 1 at position i
def find_next_row (m,i,c):
    for ii in range (i+1, len(m)):
        if m[ii][c] ==1:
            return ii
    return -1

# takes as input n and returns first found factors
# returns tuple of factors or empty tuple if prime
def factor(n):
    pmatrix = []
    pvals = []
    global b
    avals = []
    a0 = int (math.ceil(math.sqrt (n)))
    i=a0
    while len(pvals)<b+1:
        i = random.randint(a0,n-1)
        if i in avals:
            continue

        qx = int ((i*i)% n)
        #print i, qx

        parr = bfactor (qx, [0]*b)
        if not parr:
            #i+=1
            continue
        #print qx
        avals.append (i)
        
        print i, "->", qx, parr
        pvals.append (qx)
        pmatrix.append (parr)#map (lambda x: x%2,parr))
        #i+=1
        #print i, parr
    print "Table", pmatrix
    square_parr = subsetsum2 ( pmatrix)
    print avals
    print square_parr
    left = 1
    for i in range(0, len(avals)):
        left *= avals[i] if square_parr[i] else 1
        left = int(left % n)
    #for j in range(0, len(avals)):
    square_root = addprimes(pmatrix, square_parr)
    right =1
    for i in range(0, len(square_root)):
        right *= primes[i]** square_root[i]
        right = int(right % n)
    print left, right

    r1 = int(fractions.gcd(int((left-right)% n), n))
    return (r1, int(n/r1))

if len(sys.argv) < 2:
    print "error: needs 1 argument "
    print "python bruteforce.py [integer]"
    exit()

#random.seed(1232)
for i in range(0,100):
    roots =factor(float(sys.argv[1]))
    if roots[0] != 1 and roots[1] != 1:
        print roots
        exit()
print "Couldn't find roots, giving up"
#print pvals
#print pmatrix