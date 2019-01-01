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
