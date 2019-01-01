
def CheckTeams (theList, theRacers, teamList):
    # Check each team has at least 3 members
    # If not they are eliminated
    noOfRacers=0
    toDelete=[]
    
    for team in teamList:
        noOfRacers=0
        toDelete=[]
        for racer in theList:
            data=(theRacers[racer])
            if data[1]==team :
                noOfRacers+=1
                toDelete.append(racer)
        if noOfRacers<3 :
            print("Not enough racers for team : ", team)
            for racer in toDelete:
                print("Racer ", racer," eliminated")
                del theList[racer]
                del theRacers[racer]
    print()        
    return(theList, theRacers, teamList)




def LoadFile(filename) :
# Load the races into a dictionary based on their team name
# File uses , as a seperater between data, assuming data stored (number,name,team)
# Returning three dictionaries - one with just race numbers (theList) and the other
# is all the data (theRacers), and one is the list of teams (teamList)
    theRacers={}
    theList={}
    teamList={} 
    readLine=" "
    try:
        theFile=open(filename, "r")
        while readLine!="":
            readLine=theFile.readline()
            try:
                number,name,team=readLine.split(",")
                team=team.strip()
                theRacers[number]=name, team
                theList[number]=0
                teamList[team]=0
            except ValueError:
                print()
            theFile.close
    except IOError:
        print("Error with the file, ", filename)

    theList, theRacers, teamList=CheckTeams (theList, theRacers, teamList)
    return (theRacers, theList, teamList)


def SortList(listToSort):
    # This inverts the list and returns
    return (sorted([(value,key) for (key,value) in listToSort.items()]))
    

def WinnersList(numberList, racersList, finishersList, theirTeam):
    # check if score is zero and if is do not add to the output
    score=0
    output=""
    no=0
    
    for z in numberList:
        data=racersList[z]
        if data[1]==theirTeam:
            if z in finishersList :
                no+=1
                if no<4 :
                    output+=data[0]
                    if no!=3 :
                        output+=", "
                    score+=numberList[z]
    return (score,output)



def RaceResults(entries) :
        # Take a list of racers - Name, Team, Number (Number is unique)
        # And calculate points relative to finishing position.
        # But only first three winners of the teams will score
        # Output a table relative to the winners (those with lesser scores)
            
    printList=[]
    racersList={}
    numberList={}
    teamlist={}
    raceInput=""
    finishersList=[]
    racers=1
    lastscore=0
    place=0

    racersList, numberList, teamList=LoadFile(entries)
    
    print("Please use 0 at any time to quit")
    
    while racers<(len(racersList)+1) :
        print()
        print ("Racers :")
        for item in racersList:
            if item not in finishersList:
                print (item+" ,", end="")
        print()
        try:
            raceInput=input("Please input the number of the racer who finished in position "+ str(racers)+" : ")
            if int(raceInput)==0 :
                break
            print()
            if raceInput not in finishersList:
                print ("Finished in place : ", racers, " : ", raceInput, ",",racersList[raceInput][0], " of ", racersList[raceInput][1])
                score=0
                if raceInput in racersList:
                    finishersList.append(raceInput)
                    theirTeam=racersList[raceInput]
                    teamList[theirTeam[1]]+=1
                    if teamList[theirTeam[1]] <4 :
                        numberList[raceInput]=racers
                    if teamList[theirTeam[1]] ==3:             
                        score, output=WinnersList(numberList, racersList, finishersList, theirTeam[1])
                        output=theirTeam[1]+"  : "+output
                        print()
                        print("Score : %s    : %s" % (score,output))                                                      
                    racers+=1
                else:
                    print("Racer doesnt exist")
            else :
                print(raceInput," has already been entered")
        except ValueError:
            print("Please input a race number from the list given.")
       

    print("Results : ")
    
    for z in sorted(teamList):
        if teamList[z]!=0:
            teamList[z]=0
        else:
            del teamList[z]
        
    for z in numberList:
        theirTeam=racersList[z]
        score=int(numberList[z])
        teamList[theirTeam[1]]+=score
  
    printList=SortList(teamList)
    print("%-5s:%-7s:%-15s - Members" % ("Place", "Score", "Team"))

    score=0
    x=0
    for z in printList:
        x+=1
        if z[0]!=score :
            place=x
        score, output=WinnersList(numberList, racersList, finishersList,z[1])
        print("%5s:%7s:%-15s:%-30s" % (place,z[0], z[1], output))  
    return


