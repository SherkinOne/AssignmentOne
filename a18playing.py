def createNewList (low, high):
    newlist=[]
    print (low, high)
    for z in range (low,high):
        newlist.append(z)
    return (newlist)

def searchList(theList):
    #sdfdsf
    return

def sortlist(theList) :
    
    return 

from random import randint

def FindNumber ():
    # Find the number chosen by the user
    # Using a series of questions to guess whether number is <>=
    # Store the input into a list
    highno=20
    lowno=1
    guess=0
    guesslist=[]
    inputsign="="
    while inputsign ==">" or inputsign=="=" or inputsign=="<" :
            
            print (guessList)
            guess= guessList[randint (0, len(guessList)-1)]
            print (guess)
            inputsign=input("""Is the guess greater than (>)
                        less than (<) or equal (=) too???""")
            
            #should check that the input is small than highest in list
            #and higher than in smallest list
            if inputsign==">" :
                lowno=guess
                if guess+2>highno :
                    highno+=20
                    guessList=createNewList(lowno, highno)
            elif inputsign=="<" :
                highno=guess
                if guess-5<lowno :
                    guessList=createNewList(lowno, highno)
                    lowno-=20
            elif inputsign=="=" :
                break
            else :
                print ("Please enter a valid number")
    print ("Correct the number was ", guess)
    print ("My guesses were : " ,guesslist)
    return
