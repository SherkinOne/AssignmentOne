def TotalScore(dice): # Sum of the score of the number of dice rolled
    from random import randint
    totalanswer=0
    for z in range(0, dice) :
        totalanswer=totalanswer+randint(1,6)
    return(totalanswer)
    
def Percent(part,whole):
    #The INTEGER percentage of which part (less than 100%) is of whole 100%
    if whole< part or part==0 or  whole==0 :
        print ("Please enter correct values!!")
        whole =int(input ("Firstly the whole number :  "))
        part = int(input ("Then the part number to be calculated:  "))
        percent(part,whole)
    return(round(((part/whole)*100)))


def DiceRolls():
    # Return a histogram relative to the number of dice rolled and the score
    # The 'game' loops until the user exits.  Data can reset each time or it can be carried over
    score=0
    howmanydice=1
    howmanytimes=1
    totaltimes=0
    largestscore=0
    scorelist=[]
    percentlist=[]
    
    print ("Hello")
    while True :
        howmanydice=int(input("How many of dice would you like to roll today?  (0 will quit) :" ))
        if howmanydice==0 :
            break
        howmanytimes=int(input("And how many times would you like to roll the dice?  : "))
        print()
  
        for z in range (0,howmanytimes) :
            score=TotalScore(howmanydice)
            if score>largestscore :
                largestscore=score
            totaltimes+=1
            there=False
            for x in range (0,len(scorelist)) :
                if score==scorelist[x] :
                    percentlist[x]+=1
                    there=True
            if there==False :
                scorelist.append(score)
                percentlist.append(1)


        for n in range (howmanydice,largestscore+1) :
            for y in range(0, len(scorelist)) :
                if n==scorelist[y] :
                    percentage=(Percent(percentlist[y],totaltimes))
                    print( "%2i : %3s : %-2s" % (scorelist[y],str(percentage)+"%", percentage*"*"))
        print()
        print ("NB : 0% shows occurance, but with a large number of dice it can occur when percentage value below 1%")
        print()
 
        cont=input("Would you like to quit (0 or q) or try again (t)")
        cont=cont.upper()
        if cont=="0" or cont=="Q" :
            break
        else :
                score=0
                totaltimes=0
                largestscore=0
                scorelist=[]
                percentlist=[]
    return()


