def CommonTwo (string1, string2):
    #Uses the items from two strings and check them
    newstring=""
    if string1=="":
        return(string2)
    if string2=="":
        return(string1)      
    for z in string1:
        for x in string2:
            if z==x and z!=",":
                newstring+=z
    return (newstring)

           
def CommonAll(strings):
    #Will use the abouve function to compare two strings
    xloopstring=""
    comparedstring=strings[0]
    for x in range (1, len(strings)):
        xloopstring=strings[x]
        comparedstring=CommonTwo(comparedstring, xloopstring)
    return(comparedstring)
            
    
