#!/usr/bin/env python3


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

from sys import argv

options=[]
z=0

for x in range (len (argv)):
    z+=1
    options[z]=x
    print (x)


try :
    theFile=open(fileName,"r")
    
except FileNotFoundError :
    print (fileName, "not Found - Please enter a valid file name!")
except IOError :
    print ("Error with file!!")
except TypeError :
    print ("Please enter valid parameters : SearchFile(Name of the File, [Items to find]")
except EOFError :
    theFile.close 
