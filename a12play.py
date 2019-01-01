def PrintLongLines (FileName,limit) :
    # Display each line of a file, which is greater than limit, and
    # its position in the file
    lineno=0
    inputline=[""]
    TheFile = open(FileName,"r")
    inputfile=TheFile.read()
    TheFile.close
    inputlines=inputfile.splitlines()
    for line in inputlines :
        lineno+=1
        if len(line) > limit :
            print("%4i : %s" % (lineno, line))

def Stats (FileNames) :
    # Display the name of file (assuming 8 chars + ext), number of lines, and number of characters
    FileName="" 
    print ("%-15s   %6s   %6s" % ("File Name","Lines","Chars"))
    completechar =0
    completeline=0
    for FileName in FileNames :
        totalchar=0
        lineno=0
        TheFile=open(FileName,"r")
        inputline=TheFile.readline()
        while inputline!="" :
            totalchar+=(len(inputline)-1)
            lineno+=1
            inputline=TheFile.readline()
        print ("%-15s : %6i : %6i" % (FileName, lineno, totalchar))
        completechar+=totalchar
        completeline+=lineno
    print ("%-15s : %6i : %6i" % ("TOTALS ",completeline, completechar))


def EqualFiles (fileName1, fileName2) :
    #Are the contents of a files equal
    FileOne=open(fileName1, "r")
    FileTwo=open(fileName2,"r")
    inputone=FileOne.readline()
    inputtwo=FileTwo.readline()
    
    while inputone!="" or inputtwo!="" :
        if inputone!=inputtwo:
            FileOne.close
            FileTwo.close
            return False
        inputone=FileOne.readline()
        inputtwo=FileTwo.readline()

    FileOne.close
    FileTwo.close
    return True


def CommonLines(fileName1,fileName2):
    #Output any line from fileName1 that is present in fileName2
    inputfile=[]
    inputfile2=[]
    line=""
    line2=""
    
    FileOne=open(fileName1, "r")
    FileTwo=open(fileName2, "r")

    inputone=FileOne.read()
    inputtwo=FileTwo.read()

    FileOne.close
    FileTwo.close
    
    inputfile=inputone.splitlines()
    inputfile2=inputtwo.splitlines()

    for line in inputfile:
        for line2 in inputfile2:
            if line==line2 :
                print (line)
        
   
def Caeser (fileName):
    #Display the contents of a file encoded using Ceaser
    #Caeser Cipher is a shift 3 letters back - Only encoding characters
    inputfile="!"
    lettervalue=0
    TheFile=open(fileName,"r")
    
    while inputfile!="":
        inputfile=TheFile.readline()
        z=0
        for letter in inputfile :
            lettervalue=ord(letter[z])
            if (lettervalue>67 and lettervalue<91) or (lettervalue>100 and lettervalue<122):
                print (chr(lettervalue-3),end="")
            elif (lettervalue>64 and lettervalue<68) or (lettervalue>96 and lettervalue<100):
                print (chr(lettervalue+23),end="")
            else :
                print(letter[z],end="")    
        z+=1         
    TheFile.close
