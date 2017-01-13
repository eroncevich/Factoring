# takes in a number n and prime p and produces r such that r^2 = n mod p
# Assuming legendre (n/p) =1 
def ressol(n, p):
    
    # Step 1 
    p_minus_one = p-1
    s = 0
    while p_minus_one % 2 ==0:
        s+=1
        p_minus_one=p_minus_one/2
    q = (p-1)/(2**s)
    print q,s

    # Step 2 find z st (z/p) = -1
    z=2
    while pow(z,(p-1)/2, p) !=p-1:
        #print pow(z,(p-1)/2, p)
        z+=1
    c = pow(z,q,p)

    print z,c

    # Step 3
    r = pow(n,(q+1)/2, p)
    t = pow(n,q,p)
    m = s
    print r,t,m

    # Step 4
    while True:
        if t == 1:
            return (r, p-r)
        t2 = t
        for i in range(0,m):
            if t2 ==1:
                break
            t2 = int((t2*t2) % p)
        print i
        y = 2**(m-i-1)
        b = pow(c,y,p)
        r=int((r*b)%p)
        t=int((t*b*b)%p)
        c=int((b*b)%p)
        m=i
        #break



print ressol(10,13)