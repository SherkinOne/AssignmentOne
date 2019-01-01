#q1

def FirstCubeAbove (n) :
    #Assuming n isa non-negative integer.
    cubed=0
    z=0
    while n>(cubed-1) :
        z+=1
        cubed=z*z*z 
    return(cubed)

#q2
def IsPalindrome (s):
    # To see if the sequence is a mirror image!!
    looplength=0
    negstring=0
    z=0    
    looplength=len(s)/2
    while z<looplength :
        negstring-=1
        if s[negstring]!=s[z] :
            return
        z+=1
    return("The same")

#q2b
def IsPalindromeWords (s):
    # To see if the sequence is a mirror image!!
    # Yes I know this is using "untaught" functions!!
    looplength=0
    negstring=0
    z=0
    stringno=0
    looplength=len(s)/2
    s=str.lower(s)
    while z<looplength :
        negstring-=1
        stringno=ord(s[negstring])
        if stringno>96 and stringno<118 :
            if s[negstring]!=s[z] :
               return
        else :
            break
        z+=1
    return("The same")

#q3
def Binary(n):
    #Binary numbers, keep dividing by two, add to new list
    Binarylst=[]
    remainder=0
    newnumber=n
    stringnumber=[]
    z=0
    while newnumber>0 :
        remainder=newnumber%2
        newnumber=int(newnumber/2)
        stringnumber.append(remainder)
        z=len(stringnumber)-1
    while z!=-1:
        Binarylst.append(stringnumber[z])
        z-=1
    return (Binarylst)


#q3b
def GCD(a,b) :
    #Take the lowest number find its highest dividing number.
    #Take the higher number and then check upto the last number what is a
    #dividor

    high=0
    low=0
    x=2
    z=0
    dividors=[]
    highest=0
    
    if a<b :
        High=b
        low=a
    else:
        low=b
        high=a
        
    while (low/x)!=1 :
        if low%x==0 :
            dividors.append(x)
        x+=1

    while z<len(dividors)-1 :
        z+=1
        x=dividors[z]
        if high%x==0 :
            highest=x
    return(highest)
