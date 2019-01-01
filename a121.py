def PrintLongLines (FileName,limit) :
    # Display each line of a file, which is greater than limit, and
    # its position in the file
    lineno=0
    inputline=""
    
    TheFile = open(FileName,"r")
    inputline=TheFile.readline()
    while inputline!="":
        lineno+=1
        inputline=TheFile.readline()
        if len(inputline)>limit :
            print("%4i : %s" % (lineno, inputline),end="")
    TheFile.close


def Stats (FileNames) :
    # Display the name of file, number of lines, and number of characters
    FileName=""
    
    print ("File Name        Lines   Chars")
    for FileName in FileNames :
        totalchar=0
        lineno=0
        TheFile=open(FileName,"r")
        inputline=TheFile.readline()
        while inputline!="" :
            totalchar+=(len(inputline)-1)
            lineno+=1
            inputline=TheFile.readline()
        print ("%-15s : %4i : %6i" % (FileName, lineno, totalchar))
                

def EqualFiles (fileName1, fileName2) :
    #Are the contents of a files equal
    FileOne=open(fileName1, "r")
    FileTwo=open(fileName2,"r")

    inputone=FileOne.readline()
    inputtwo=FileTwo.readline()
    
    while inputone!="" :
        inputone=FileOne.readline()
        inputtwo=FileTwo.readline()
        if inputone!=inputtwo:
            FileOne.close
            FileTwo.close
            return False

    FileOne.close
    FileTwo.close
    return True



def CommonLines(fileName1,fileName2):
    #Output any line from fileName1 that is present in fileName2
    FileOne=open(fileName1, "r")
    inputone="Begin"
    
    while inputone!="" :
        inputtwo ="Begin"
        inputone=FileOne.readline()
        FileTwo=open(fileName2,"r")
        while inputtwo!="":
            inputtwo=FileTwo.readline()
            if inputtwo==inputone :
                print (inputone, end="")
        FileTwo.close

    FileOne.close


def Casear (fileName):
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
            if (lettervalue>67 and lettervalue<91):
                print (chr(lettervalue-3),end="")
            elif (lettervalue>100 and lettervalue<122) :
                print (chr(lettervalue-3),end="")
            elif (lettervalue>64 and lettervalue<68) :
                print (chr(lettervalue+23),end="")
            elif (lettervalue>96 and lettervalue<100):
                print (chr(lettervalue+23),end="")
            else :
                print(letter[z],end="")    
        z+=1         
    TheFile.close
