def tryPos (lst):

    
    pivot=int(len(lst)/2)
    if lowest>lst[pivot] :
        lowest=lst[pivot]
    lst=lst[pivot:]
    print(lst, pivot)
    if len(lst)==1 :
        if lowest<lst[pivot-1]:
            lowest=lst[pivot-1]
            print("returning",lowest)
            return(lowest) 
    

    if len(lst)>1 :
        if lst[pivot]<lowest :
            lowest=lst[pivot-1]
            print("returning", lowest)
            return(lowest)

        print ("returned, lowest", lowest)
        lowest=tryPos(lst)



    print ("returned, lowest", lowest)

    lst=lst[:pivot]
    print(lst, pivot)

    return (lowest)
#tryPos([1,2,3,4,5])
