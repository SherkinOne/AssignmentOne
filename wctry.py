#!/usr/local/bin/python3


#Print  newline,  word,  and byte counts for each FILE, and a total line if more than one FILE is
#  specified.  With no FILE, or when FILE is -, read standard input.  A word is  a  non-zero-length
# sequence  of characters delimited by white space.  The options below may be used to select which
# counts are printed, always in the following order: newline, word, character, byte, maximum  line
# length.
#       -m, --chars -   print the character counts
#       -l, --lines     print the newline counts
#      --files0-from=F  -  read  input  from  the  files specified by NUL-terminated names in file F; If F is - then
              #read names from standard input
#       -L, --max-line-length -    print the length of the longest line
#       -w, --words -   print the word counts
#       --help display this help and exit


# We will assume that all arguments taken in are beginning with -
# First argument is the file name that is running


from sys import argv

options=[]
z=""
x=""
files=[]
readLine=[]
longestLine=0
wordCount={"words":0, "chars":0,"lines":0}
totalCount={"words":0, "chars":0,"lines":0}

def printOut(fileDetails, file) :
    formatting=""
    arguements=""
    if options==[] :
        formatting="%5i%5i%5i%16s"
        print(formatting % (fileDetails["lines"], fileDetails["words"], fileDetails["chars"], file))
        return
    if "-l" in options :
        formatting+="%5s"
        arguements=str(fileDetails["lines"])
    if "-w" in options :
        formatting+="%5s"
        arguements=str(fileDetails["words"])
    if "-m" in options :
        formatting+="%5s"
        arguements=str(fileDetails["chars"])
    if "-L" in options :
        formatting+="%5s"
        arguements+=str(longestLine)
    if formatting !="" :
        arguements+=" "+fileName
        print(formatting % (arguements))
    else :
         print("Please enter valid arguments :  File name(s), -m, -l, -L, -w")
    return


if len (argv)==1 :
    print("Please enter valid arguments :  File name(s), -m, -l, -L, -w")
    exit

    
for arg in argv:
    if arg[0]!="-":
        files.append(arg)
    else :
        options.append(arg)
del files[0]
    
try :
    for fileName in files:
        theFile=open(fileName,"r")
        while readLine!="" :
            readLine=theFile.readline()
            wordCount["lines"]+=1
            for words in readLine.split() :
                wordCount["words"]+=1
                wordCount["chars"]+=len(words)                
                if longestLine<len(words) :
                    longestLine=len(words)
        printOut(wordCount, fileName)
        for items in wordCount :
            totalCount[items]+=wordCount[items]
            wordCount[items]=0
        theFile.close
    if len(files)>1 :
        printOut(totalCount, "total")
        


# Here is the files list is greater than one print the total library
        
    
except FileNotFoundError :
    print (fileName, "not Found - Please enter a valid file name!")
except IOError :
    print ("Error with file!!")
except TypeError :
    print ("Please enter valid arguments :  File name(s), -m, -l, -L, -w")
except EOFError :
    theFile.close


