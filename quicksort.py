def Quicksort(data, field):
    # using quick sort to sort a list
    # needs to take the list split it in the middle, again and again
    fieldno, other=GetField(field)
    x=0
    #take a pivot, move it while its smaller or equal to the other numbers then
    # take the list from to the left of that pivot repeat and same with right.
    while x<len(data):
        pivot=data[int(len(data)/2)][fieldno]
        for z in range (pivot):
            print (pivot, data[z][fieldno])
            if pivot < data[z][fieldno] :
                data[int(len(data)/2)] , data[z] = data[z],data[int(len(data)/2)]
                Print(data)
        x+=1
            
        
       
    return



data=[ ('Ann',23),('Tim',18),('Bob',37),('Ned',51),('Sue',18), ("Joe",19),('Sam',18), ("Jay",19), ("Ali", 18) , ('Ann',21)]

data2=[ 'Ann','Tim','Bob','Ned','Sue' ]



def Sort( lst, field ) :
    fieldno, other=GetField(field)
    for i in range( len( lst ) ) :
        imin = i
        for j in range( i + 1, len( lst ) ) :
            if lst[ j ][fieldno] < lst[ imin ][fieldno] :
                imin = j
 
        lst[ i ], lst[ imin ] =  lst[ imin ],lst[ i ] 
    print( i, ":", lst )
    return
