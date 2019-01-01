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
        return((s[0]+s[z]) for z in Groups(s[1:],k-1)+Groups(s[1:],k))



def Groupss(s,k):
    for z in range (len(s)):
        print()
    return(s[0]+s[z])
