#!usr/local/bin/python3

# GREP 

# so basically looking for a string in a list of words
#    if "-c" in options -n, --line-number Prefix each line of output with the 1-based line number within its input file.
    
 #   if "-v" in options -invert-match Invert the sense of matching, to select non-matching lines.  (-v is specified by POSIX.)



from sys import argv

todisplay=[]
searchWord=""
fileName=""
options=[]
readLine=" "
counter=0
totalLines=0
files=[]
output=""


if len(argv)>1 :
    for arg in argv:
        if arg[0]=="-" :
            options.append(arg)
        else :
            arg=unicode(arg,"utf-8")
            if not arg.isnumeric() :
                if "." in arg :
                    files.append(arg)
                else:
                    searchWord=arg
            else :
                options.append(int(arg))
else :
    print ("Please enter valid parameters")
    exit;

if len(files)>1 :
    del files [0]

try:
    for fileName in files :
        totalLines=0
        counter=0
        readLine=" "
        if len(files)>1 :
            output=fileName+":"
        theFile=open(fileName,"r")

        while readLine!="" :
            readLine=theFile.readline()
            totalLines+=1
            if searchWord in readLine :
                counter+=1
                if ("-c" not in options) and( "-v" not in options):
                    print (readLine.strip())
            else :
                if ("-v" in options) and ("-c" not in options) :
                    print (readLine.strip())

        if ("-c" in options) and (not "-v" in options):
            print (output+ str(counter))
        if ("-c" in options) and ("-v" in options) :
            print (output+str( totalLines-counter))
        theFile.close

except FileNotFoundError :
    print (fileName, "not Found - Please enter a valid file name!")
except IOError :
    print ("Error with file!!")
except TypeError :
    print ("Please enter valid arguments :  File name(s), -m, -l, -L, -w")
except EOFError :
    theFile.close
