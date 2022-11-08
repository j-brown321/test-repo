with open('testdoc.txt') as line:

    charac = line.read()

    print(charac)

def wordfreq(string):

    list = string.split()
    
    newlist =  []

    for x in list :
        
        if x not in newlist :
            
            newlist.append(x)
    
    for x in range (0, len(newlist)) :
        
        print("The frequncy of the word", newlist[x], "is", list.count(newlist[x]))

        wordfreq(charac)