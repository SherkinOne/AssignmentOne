#!usr/local/bin/python3

# UNIQ -

# compares lines in a file to see if they are equal
# -c, --count 	prefix lines by the number of occurrences
#-d, --repeated  	only print duplicate lines
#-D, --all-repeated[=delimit-method] print all duplicate lines
 #	delimit-method={none(default),prepend,separate} Delimiting is done with blank lines.
#-f, --skip-fields=N  	avoid comparing the first N fields
# -i, --ignore-case 	ignore differences in case when comparing
#-s, --skip-chars=N  	avoid comparing the first N characters
# -u, --unique  	only print unique lines
 #-w, --check-chars=N  	compare no more than N characters in lines

from sys import argv, exit
import os


newLine=""
oldLine=""
options=[]
fileName=""
readLine=" "
count=0
fields=0
number=0
chars=0

def ArgumentsXtra(arguement) :
    try :
        for z in range(len(options)) :
            if options[z]==arguement :
                if options[z+1]!="" :
                    number=int(options[z+1])
        if number==0:
            print (arguement +" : supporting arguement not working")
            sys.exit()
    return (number)


def CheckArguements(newLine, oldLine, count) : 
    oldCount=1
    if oldLine==newLine:
        count+=1
    else:
        if count>1 :
            oldCount=count
            count=1
        else:
            count=1
    if "-d" in options :
        if count>1 :
            count=0
            print (oldLine)
    if "-D" in options :
        if (oldLine==newLine) or (count>1):
            for z in range (count):
                print (newLine)
            count=0
    if "-f" in options:
        fields=ArgumentsXtra("-f")
        old=oldLine.split(" ", fields+1)
        new=newLine.split(" ", fields+1)
        if (len(old)>=fields) and (len(new)>=fields) :
            print (oldLine)
    if "-i" in options :
        if oldLine.Ucase==newLine.Ucase :
            print (oldLine)
    if "-s" in options:
        chars=ArgumentsXtra("-s")
        old =oldLine[:chars-1]
        new =newLine[:chars-1]
        if old==new:
             print (oldLine) 
    if "-u" in options :
        if count==1 and oldLine!=newLine:
            print (oldLine)
    if "-w" in options :
        chars=ArgumentsXtra("-w")
        old =oldLine[:chars-1]
        new =newLine[:chars-1]
        if old==new:
             print (oldLine) 
    if "-c" in options :
        if count==1 and oldLine!=newLine:
            print (str(oldCount)+" "+ oldLine)
    return (count)


if len(argv)>1 :
    for arg in argv:
        if arg[0]=="-" :
            options.append(arg)
        else :
            arg=unicode(arg,"utf-8")
            if not arg.isnumeric() :
                fileName=arg
            else :
                options.append(int(arg))
    if "-d" in options:
        if "-u" in options :
            exit;
else :
    print ("Please enter valid parameters")
    exit;


try:
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
except IOError :
    print ("Error with file!!")
except TypeError :
    print ("Please enter valid arguments :  File name(s), -m, -l, -L, -w")
except EOFError :
    theFile.close

