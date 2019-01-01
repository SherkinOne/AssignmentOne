def Print (data) :
    # Print the formatted table of data
    formatting="%-7s %3s"
    print (formatting %("Name", "Age"))
    print (formatting %(("-"*7), ("-"*3)))
    for z in range(len(data)):
        print (formatting % (data[z][0], data[z][1]))
    return

def GetField (field):
    # this returns the field that the list if being sorted on
    if field.lower()=="age" :
        fieldno=1
        other=0
    else :
        fieldno=0
        other=1
    return (fieldno, other)

def InsertionSort (data, field):
    # Print the data after being sorted with the insertion sort relative to the field!!
    # Also just for data list with TWO fields
    fieldno, other=GetField(field)
    for z in range(len(data)) :
        tosort=data[z][fieldno]
        pointer=z
        while pointer>0 and tosort<data[pointer-1][fieldno]:
            data[pointer], data[pointer-1]=data[pointer-1], data[pointer]
            pointer-=1        
    for z in range(1,len(data)) :
        pointer=z
        while pointer>0 :
            if data[pointer-1][fieldno]==data[pointer][fieldno] :
                if data[pointer-1][other]>data[pointer][other] :
                    data[pointer], data[pointer-1]=data[pointer-1], data[pointer]
            pointer-=1
        
    Print(data)    
    return


def SelectionSort(data, field):
    # Print the data after sorting with selection sort
    # Also just writing this for data list with TWO fields so second sort is other column
    fieldno, other=GetField(field)
    minplace=0
    for z in range (len(data)):
        minplace=z
        for x in range (z+1, len(data)) :
            if data[x][fieldno]<data[minplace][fieldno] :              
                minplace=x
                
        data[z], data[minplace]=data[minplace],data[z]
    for z in range(1,len(data)) :
        pointer=z
        while pointer>0 :
            if data[pointer-1][fieldno]==data[pointer][fieldno] :
                if data[pointer-1][other]>data[pointer][other] :
                    data[pointer], data[pointer-1]=data[pointer-1], data[pointer]
            pointer-=1
    Print(data)
    return
