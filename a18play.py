def createlist (high,low=0):
    lst=[]
    for z in range (low, high):
        lst.append(z)
    return(lst)

def FindNumber ():
        # Find the number chosen by the user between 1-1000
        #dont reaaly neeed the list
        # Using a series of questions to guess whether number is <>=
    highno=1000
    lowno=0
    guess=0
    noguess=0
    guesses=[]
    guesslist=[]
    inputsign="="
    from random import randint  
    while inputsign:
        guesslist=createlist(highno, lowno)
        noguess+=1
        if len(guesslist) >2 :
            pivot=guesslist[int(len(guesslist)/2)]
        else :
            if pivot==guesslist[0]:
                pivot=guesslist[1]
            else:
                pivot=guesslist[0]

        print (pivot)
        inputsign=input("Is the guess greater than (>) less than (<) or equal (=) too???")
        if inputsign==">" :
            if pivot-2>=lowno :
                lowno=pivot
        elif inputsign=="<" :
            if pivot+2<=highno :
                highno=pivot
        elif inputsign=="=" :
            print ("It took : ", noguess, "no of guesses")
            break
        else :
            print("Please enter a correct sign")

    print ("Correct the number was ", guess)

    return



def MinPos (lst):
    lowest=0;
    # take the length of the list split it
    # this doesnt return position but just the value
    # so break down lists as far as can go until smallest no found
    if len(lst) >=2 :
        mid=int(len(lst)/2)
        pivot=lst[mid-1]
        lowest=MinPos(lst[:mid])
        if lowest>pivot :
            lowest=pivot
        lowest=MinPos(lst[mid:])
        if lowest>pivot:
            lowest=pivot
    elif len(lst)==1:
        if lowest<lst[0] :
            lowest=lst[0]
        #check both values
    return (lowest)
