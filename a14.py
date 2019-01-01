def ReadDictionary(fileName):
    #read filename, should contain two words per line
    # return a dictionary with the first word as key
    # second word is the value
    wordDict={}
    try :
        theFile=open(fileName)
        readLine=theFile.readline()
        while readLine!="":
            key,value=readLine.split()
            readLine=theFile.readline()
            wordDict[key]=value
    except IOError :
        print ("File :", fileName," doesn't exist!")
    except ValueError:
        print("File :", fileName," wrong format!")
    theFile.close
    return(wordDict)

def PrintDictionary(d):
    # Output dictionary 'd', sorted alphabetically
    # Formatting with one key value per line
    dlist=(sorted(d.keys()))
    for key in dlist:
        print("%-10s : %-10s" % (key, d[key]))
    return
    
def Inverse (d):
    # Inverse dictionary d
    inversed={}
    for z in d :
        inversed[d[z]]=z
    return (inversed)

def Translate(d, inputFileNames):
    # Take input file : Output file - with -translated addition
    # So check the words and replace with corresponding
    # ie. if dict value for smile is sun replace all smiles with sun
    try:
        for fileName in inputFileNames :
            try:
                openFile=open(fileName, "r")
                output=fileName.split(".")
                outputFileName=output[0]+"-Translated."+output[1]
                outputFile=open(outputFileName, "w")
                readLine=" "
                while readLine :
                    readLine=openFile.readline()
                    outLine=""
                    for words in readLine:
                        if words in d:
                                thetrans=d[words]
                                outLine+=thetrans
                        else:
                            outLine+=words         
                    outputFile.write(outLine)
                openFile.close
                outputFile.close
            except FileNotFoundError :
                print (fileName,"not Found - continuing with other files!")
    except IOError :
        print ("Error with file!!")
    except TypeError :
        print ("Please enter valid parameters : Translate (Dictionary, LIST of Files)")
    except EOFError :
       openFile.close
       outputFile.close
