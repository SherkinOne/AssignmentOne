

def Extractsecond (s,positions):
    #Extract the letters from the string s
    #Using positions
    #Firstly return index as positive if negative
    #The check for duplicates in list
    Extracted=[]
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
        for x in range (z+1, len(positions)):
            if check==pstlst[x] and there!=True:
                there=False
        if there==True:
            checklist.append(check)
        else :
            there=True
    for z in range(len(checklist)):
       position=checklist[z]
       if position < len(s) :
           Extracted.append(s[position])
    return (Extracted)




