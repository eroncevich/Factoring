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

# takes in m which is a matrix counting the powers of primes ex (2^x, 3^y, 5^z, ...)
# and counter is the base 2 counter from rref2 which adds up the matrices to get the square number
# index is needed to add the m[index] element by default.
def addprimes (m, counter, index):
	tempm = m[:]
	sum_arr = [0 for i in range (0,len(counter))]
	sum_arr = map(lambda x,y: x+y, sum_arr, tempm[index])
	del tempm[index]
	for i in range(0, len(counter)):
	    if counter[i]:
	        sum_arr = map(lambda x,y: x+y, sum_arr, tempm[i])
	return sum_arr

# this function will go through, select one of the b+1 rows, xor with other rows, and rref2
# the other rows. Either the rref2 will have:
# 1. a row of all 0's, so linearly dependent ( so subset sum =0)
# 2. all rows have 1's, so independent, (but in this case we repeat with another row which should be dependent)

# input is nonnegative integers, and it will transform to F2

def subsetsum2 ( m, pvals2):
	
    m2 = [] # base 2 matrix version of m
    for i in range (0, len(m)):
        m2.append (map (lambda x: x%2,m[i]))

    #print m2

    for i in range (0,1):
        #print "Using m2", m2
        tempm = []
        temp_pvals = pvals2[:]
        del temp_pvals[i]
        print "set", temp_pvals
        for j in range (0, len(m2)):
            if i==j:
                continue
            tempm.append(map(lambda x,y: x ^ y , m2[i],m2[j]))
        square = rref2 (tempm)
        if square: # if the array is not empty
            print "Found square"
            print "base 2",square

            #print "base primes", m
            square_parr = addprimes (m, square, i)
            print "base primes", square_parr
            print "square", map(lambda x: x/2, square_parr)
            exit()
        #print tempm

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

    for i in range (0, len(m)-1):
    	#print "step m", m
    	#print counterm
        if m[i][c] ==0: #first check if 1 in the correct position
            ii = find_next_row (m,i,c)
            if ii<0:
                c+=1
            else:
                t = m[i]
                countert = counterm[i]
                m[i] = m[ii]
                counterm[i]=counterm[ii]
                m[ii] = t
                counterm[ii]= countert
        for j in range (i+1, len(m)):
            if m[j][c]==1:
                m[j] = map(lambda x,y: x ^ y , m[i],m[j])
                counterm[j] = map(lambda x,y: x+y, counterm[i],counterm[j])
        c+=1
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
    global b
    a0 = int (math.ceil(math.sqrt (n)))
    i=a0
    while len(pvals)<b+1:
        qx = int ((i*i)% n)
        #print qx
        if not bfactorable(qx):
            i+=1
            continue
        #print qx
        parr = bfactor (qx, [0]*b)
        print qx, parr
        pvals.append (qx)
        pmatrix.append (parr)#map (lambda x: x%2,parr))
        i+=1
        #print i, parr
    print "Table", pmatrix
    subsetsum2 ( pmatrix, pvals)


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
#print pvals
#print pmatrix