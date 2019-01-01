try:
    print (options)
    theFile=open(fileName,"r")
    while readLine!="" :
        oldLine=readLine
        readLine=theFile.readline()      
        if len(options)>0 :
            
            count=CheckArguements(readLine.strip(), oldLine.strip(), count)
        else :
            if readLine!=oldLine :
                print (readLine.strip())
    theFile.close


except FileNotFoundError :
    print (fileName, "not Found - Please enter a valid file name!")
