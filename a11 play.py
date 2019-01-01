def Percent(part,whole):
    #The INTEGER percentage of which part is of whole
    if whole< part or part==0 or  whole==0 :
        print ("Please enter correct values!!")
        whole =int(input ("Firstly the whole number :  "))
        part = int(input ("Then the part number to be calculated:  "))
        Percent(part,whole)
    return(int(((whole-part)/whole)*100))
        
def TotalScore (dice):
        global score
        from random import randint
        score=score+Randint(1,6)
        TotalScore(dice-1)
        return(score)

