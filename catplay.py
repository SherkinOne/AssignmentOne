#!usr/local/bin/python3

# CAT 

#DESCRIPTION

     #  -E, --show-ends display $ at end of each line
      # -n, --number              number all output lines
       #-s, --squeeze-blank   suppress repeated empty output lines
    #   With no FILE, or when FILE is -, read standard input.

from sys import argv
files=[]
oldLine=""
readLine=""
options=[]
noOfLines=0
    
for arg in argv:
    if arg[0]!="-":
        files.append(arg)
    else :
        options.append(arg)
del files[0]
    
try :
    noOfLines=0
    for fileName in files:
        theFile=open(fileName,"r")
        readLine=theFile.readline()
        while readLine!="" :
            oldLine=readLine
            readLine=theFile.readline()
            if oldLine!="" and readLine!="":
                noOfLines+=1
                if "-n" in options :
                    output=str(noOfLines)+" "
                if "-E" in options :
                    output="$ "+output
                output+=readLine.strip()
                print (output)
              
    theFile.Close

except FileNotFoundError :
    print (fileName, "not Found - Please enter a valid file name!")
except IOError :
    print ("Error with file!!")
except TypeError :
    print ("Please enter valid arguments :  File name(s), -m, -l, -L, -w")
except EOFError :
    theFile.close
    print ("")
            
