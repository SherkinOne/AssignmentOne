def Head (count, fileName): 
    #Display to the screen the first lines of a file till count or whole file otherwise
    # Catch any errors and display appropriately

    try :
        theFile=open(fileName, "r")
        for z in range (count) :
            lineRead=theFile.readline()
            print(lineRead.strip("\n"))
        theFile.close
    except FileNotFoundError :
        print (fileName, "not Found - Please enter a valid file name!")
    except IOError :
        print ("Error with file!!")
    except TypeError :
        print ("Please enter valid parameters : Head(Number of lines to display, Name of File)")


        
def SearchFile (fileName, items):
    # Display each line that contains ANY OF ITEMS inside them
    # Along with it's line no.
    lineNo=1
    try :
        theFile=open(fileName, "r")
        lineRead=theFile.readline()
        while lineRead :
            for item in items:
                if item in lineRead :
                    print ("%-6i %s" % (lineNo, lineRead.strip("\n")))
            lineNo+=1
            lineRead=theFile.readline()
            theFile.close 
    except FileNotFoundError :
        print (fileName, "not Found - Please enter a valid file name!")
    except IOError :
        print ("Error with file!!")
    except TypeError :
        print ("Please enter valid parameters : SearchFile(Name of the File, [Items to find]")
    except EOFError :
        theFile.close 


def JoinFiles(inputFileNames, outputFileName) :
    #Copy all the files in the LIST of inputfiles to the FILE outputFileName
    try:
        outputFile=open(outputFileName, "w")
        for fileName in inputFileNames :
            openFile=open(fileName, "r")
            readLine=" "
            while readLine :
                readLine=openFile.readline()
                outputFile.write(readLine)
            openFile.close
        outputFile.close
    except FileNotFoundError :
        print (fileName,"not Found - Please enter a valid file name!")
    except IOError :
        print ("Error with file!!")
    except TypeError :
        print ("Please enter valid parameters : JoinFiles([Name of the Files for input], File to output too")
    except EOFError :
       openFile.close
       outputFile.close


def Occurences (inputFileNames, words, outputFileName):
    # For each file in the LIST inputFileNames take the words, check the number of
    # occurances and then output this too the file

    try:

        wordsThere=[]

        for z in range (len(words)):
            wordsThere.append(0)
        
        output="File Name  :"
        for items in words:
            output+=items+"     "
        theOutput=open(outputFileName,"w")
        theOutput.write(output+"\n")
        theOutput.close


        for fileName in inputFileNames:
            openFile=open(fileName, "r")
            lineRead=" "
            while lineRead:
                lineRead=openFile.readline()
                z=0
                for items in words:
                    if items in lineRead:
                        wordsThere[z]+=1
                    z+=1
            openFile.close
            theOutput=open(outputFileName,"a")
            there=""
            for z in range(0,len(wordsThere)) :
                there=there+str(wordsThere[z])
                there=there.lstrip("[")
                there=there.rstrip("]")
                there=there+((" "*(len(words[z])+2)))
            theOutput.write("%-12s %s" % (fileName, there+"\n"))
            theOutput.close

    except FileNotFoundError :
        print (fileName,"not Found - Please enter a valid file name!")
    except IOError :
        print ("Error with file!!")
    except TypeError :
        print ("Please enter valid parameters")
    except EOFError :
       openFile.close
       outputFile.close

