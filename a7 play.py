def CommonTwo (string1, string2):
    #Uses the items from two strings and check them
    newstring=""
    if string1=="":
        return(string2)
    if string2=="":
        return(string1)      
    for z in string1:
        for x in string2:
            if z==x :
                newstring+=z
    return (newstring)       


def CommonAll(strings):
    #Make a string from the duplicate items in each list item
    returnstring=""
    nowstring=""
    oldstring=""
    #Would make sense to start a loop for first list group and then compare
    #each list group to that
        # what it needs to do is go through n number of items in
        # list and compare them
    for nowstring in (strings):
        print ("First loop", nowstring)
        #x is every item in the list as we go through a loop
        print ("Nowstring", nowstring)
        print ("oldstring", oldstring)
        returnstring+=CommonTwo(nowstring,oldstring)
        print ("Returnstring :", returnstring)


        oldstring=nowstring

    return (returnstring)
           
