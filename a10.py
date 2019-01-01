# Check that the variables are all defined
# That all print statements are removed.
# Syntax is tidied

#q1
def Power (x,n) :
    #Return x to the power of n
    original=x
    while n>1:
        n=n-1
        x=x*original
        Power(x,n-1)
    return (x)

#q2
def Range (lo,hi) :
    #print list from low to high
    newlist=[]
    if lo>hi :
        return
    while lo!=hi:
        newlist.append(lo)
        lo=lo+1
        print (lo, newlist)
        Range(lo,hi)
    return (newlist)


#q3
def DigitCount(n):
    # This returns the number of digits, ie. 10's, 100's ,1000's
    # We could turn it to a string and return the len!!!???
    digitnumbers=0
    x=0
    z=n/10
    if z>1:
        digitnumbers+=DigitCount(z)
    digitnumbers=digitnumbers+1
    return(digitnumbers)


#q4
def Groups(s,k):
    #Like Choose??
    #Take string s and return all valid combinations of length k
    newlist=[]
    if k==0:
        return
    elif k==len(s) :
        return(s)
    else:
        return([s[0]+z for z in Groups(s[1:],k-1)+Groups(s[1:],k)
