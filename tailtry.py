#!usr/local/bin/python3

#TAIL(1) 
#DESCRIPTION
#    if "-n" in options :
        #-n, --lines=K output  the  last  K lines,
# instead of the last 10; or use -n +K to output lines starting with the Kth
# --max-unchanged-stats=N with --follow=name,
#reopen a FILE which has not changed size after N (default 5)
#iterations to see

fileName=""
options=[]
todisplay=[]
readLine=" "
numberToDisplay=10

from sys import argv, exit

if len(argv)>1 :
    # This could be tidied
    for arg in argv:
        if arg[0]=="-" :
            options.append(arg)
        else :
            arg=unicode(arg,"utf-8")
            if not arg.isnumeric() :
                fileName=arg
            else :
                numberToDisplay=int(arg)
else :
    print ("Please enter valid parameters")
    exit;

try:
    print (numberToDisplay)
    theFile=open(fileName,"r")
    while readLine!="" :
        readLine=theFile.readline()
        todisplay.append(readLine)
        if len(todisplay)>numberToDisplay :
            del todisplay[0]
            theFile.close
    for lines in todisplay :
       print (lines.strip())


except FileNotFoundError :
    print (fileName, "not Found - Please enter a valid file name!")

