
def PrintTable(t,width=2):
   # Prints a table, using width (which default is 1 space)
    for row in t:
        formatting=""
        for x in row :
           formatting+=(width-1)*" "+str(x)
        print (formatting)
    return

def VFlip(t):
    #Vertically flip a table
    table=[]
    for z in range(len(t),0,-1) :
        table.append(t[z-1])     
    return (table)

def HFlip(t):
    # Horizontally flip a table
    table=[]
    for row in t :
        col=[]
        for x in range (len(row),0,-1):
            col.append(row[x-1])
        table.append(col) 
    return (table)

def Transpose (t):
    # Take the columns and make them into the rows of the tables
    table=[]  
    for col in range(len(t[0])):
        line=[]
        for row in t:
            line.append(row[col])
        table.append(line)
    return(table)

