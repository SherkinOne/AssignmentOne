#Q1
def Sset(s,i,c):
    #Where s is a string
    #i is the positon of the character
    #c is character in the string
    if i<0 or i>len(s) :
        return
    newlist=""
    x=0
    z=0
    count=0
    secondcount=0
    for x in s :
        if count==i :
            newlist+=c
            for z in s:
                secondcount+=1
                if count<secondcount-1 :
                    newlist+=z
                    if secondcount==len(s) :
                        return (newlist)       
        newlist+=x
        count=count+1


#Q2
def AllDifferent(s) :
    # Check to see if all different
    check=""
    z=0
    while z<len(s):
        check=s[z]
        z+=1
        if  len(Positions(check,s))>1 :
            return (False)
    return(True)


#Q3
def Positions(x,s) :
    #Check and return a list where things occur in the list
    #Where x is a character and s is a sequence
    return [f for f in range (len(s)) if s[f]==x]

#Q4
def Extract (s,positions):
    #Extract the letters from the string s
    #Using positions
    Extracted=[]
    Position=0
    for z in range(len(positions)):
       position=positions[z]
       if position < len(s) :
           Extracted.append(s[position])
    return (Extracted)

#Q5
def Extractsecond (s,positions):
    #Extract the letters from the string s
    #Using positions
    #Firstly return index as positive if negative
    #The check for duplicates in list
    pstlst=[]
    checklist=[]
    position=0
    check=0
    z=0
    x=0
    there=False
    for z in range (len(positions)) :
        check=positions[z]
        if check<0 :
            check=len(s)+check
        pstlst.append(check)
    for z in range (len(positions)) :
        check=pstlst[z]
        for x in range (z, len(positions)):
            if check==pstlst[x] and there!=True:
                there=False
        if there==True:
            checklist.append(check)
        else :
            there=True
    return (Extract(s,checklist))
