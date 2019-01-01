def CommonAll(strings):
    #Will use the abouve function to compare two strings
    #so take the loop of the amount of items in the string list
    #take two and compare
    #Need to take only the first string 
    zloopstring=""
    xloopstring=""
    comparedstring=""
    returnstring=""
    firststring=strings[0]
    for x in range (1, len(strings)):
        xloopstring=strings[x]
        comparedstring+=CommonTwo(firststring, xloopstring)
        comparedstring+=","
        print(comparedstring);
    #Take the compared string and see any factors that appear less one than
    #the length of string
    print (returnstring)
    return(returnstring)
