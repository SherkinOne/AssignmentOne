def Occurrences(inputFileNames, words, outputFileName):
    #Where inputfilenames is a list
    #Words is s list
    #output file is a new file
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
        
            
# Occurrences(["new1.txt"],[ "one"], "output.txt")
