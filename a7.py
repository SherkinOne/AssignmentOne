def Join(Strings):
    return [item for lst in strings for item in lat]

def Flatten( lsts ) :

    # The list of all items in all lists in the list-of-lists 'lsts'

    return [ item for lst in lsts for item in lst ]
def flatten (lsts):
    return[item for sublist in lsts for item in sublist]
