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

#this doesnt work but it's the base of the equation
        

def Group (s,k):
    #Take string s and return all valid combinations of value k
    original=s
    print ("Begin:",s)
    newlist=[]
    tobeadded=s[0]
    print (len(s),k)
    z=0
    if len(s)<=k :
        return
    for x in range (z,len(s)):
        while len(original)>=k:
            z=z+1
            print("X:",x, "Add: ",[original[0]+original[x:(x+(k-1))]], "Len s :",len(s) )
            newlist.append([original[0]+original[x:(x+(k-1))]])
            #newlist.append([s[0]+s[x:x+(k-1)]])  
           # print (s,k,original)
            #print(newlist)
            Group (original[1:len(original)],k)
    return(newlist)


def NewGroup (s,k):
    newlist=[]
    x=0
    ADD=s[0]
    if len(s)<=k :
        return
    for x in range (len(s)-1):
        for z in range (x,x+k):
            ADD=ADD+s[z]
        print (ADD)
        newlist.append([ADD])
        ADD=s[0]
        NewGroup(s[1:len(s)],k)
    return (newlist)













    
