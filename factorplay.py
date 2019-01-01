#!usr/local/bin/python3

# Returns factors of a number

# So take a number and then try and divide by a number
# a prime number is a number that can be divided by any other number

# should be only one arguement and this is the number inputs
# returnsno : factors
from sys import argv, exit

number=0
numlist=[]
output=[]
z=1

def getargue (argv) :
    for numbers in argv :
        numlist.append(numbers)
    del numlist[0]
    return (numlist)

# need to make a list of lists with the [no [ factors]]


def addtolist(numlist):
    z=1
    output=[]

    for number in numlist:
        number=int(number)
        while number!=1 :
            z+=1
            if (number%z)==0 :
                number=(number/z)
                output.append(z)
                z=1
    outputtext=""
    for z in output:
        outputtext+=" "+str(z)
    return(outputtext)

numlist=getargue(argv)

if len(numlist)>0 :
    addtolist(numlist)
    print (output)
else:
    inputnos=""
    while input :
        try :
            numlist=[]
            inputnos=input()
            numlist.append(inputnos)
            output=addtolist(numlist)
            output=str(inputnos)+ ":"+output
           
            print (output)
        except EOFError:
            print (inputnos)
            if len(inputnos)>0 :
                numlist=getargue(inputnos)
                addtolist()
        except ValueError :
            print ("Value incorrect - please enter integers")


            
        
    
