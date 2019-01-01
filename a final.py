
#Question 1

def Join (strings):
    #return all strings add together as a string
    altogether=""
    for z in range(len(strings)):
        altogether+=strings[z]
    return altogether

#Question 2
def CumulativeSums(numbers) :
    #Add the numbers in the list going through the list from a - z
    newnumbers=[numbers[0]]
    appendno=0
    for i in range (1,len(numbers)) :
       appendno=int(newnumbers[(i-1)])+int(numbers[(i)])
       newnumbers.append(appendno)
    print (newnumbers)
        

#Question 3
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


#Question 4
def CommonAll(strings):
    #Will use the above function to compare two strings
    xloopstring=""
    comparedstring=strings[0]
    for x in range (1, len(strings)):
        xloopstring=strings[x]
        comparedstring=CommonTwo(comparedstring, xloopstring)
    return(comparedstring)
