import io

def initials():
    print('asdf')

def startsWith(option):
    print('asdf')

def startsEndsWith(option):
    totalCount = 0
    trueCount = 0
    names = ''
    fileName = ''
    if option == 'f2':
        fileName = 'first_names.all.txt'
        print('Find first names that start and end with a certain character')
    elif option == 'l2':
        fileName = 'last_names.all.txt'
        print('Find last names that start and end with a certain character')
    f = io.open(fileName, encoding="utf8")
    startChar = input('Starts with: ').lower()
    endChar = input('Ends with: ').lower()
    for line in f:
        try:
            line.replace('/n','')
            if line[0] == startChar and line[len(line)-2] == endChar:
                names += line
                trueCount = trueCount + 1
        finally:
            totalCount = totalCount + 1
    f.close()
    result = {
        'names': names,
        'totalCount': totalCount,
        'trueCount': trueCount,
        'newFileName': option + startChar + endChar + '.txt'
    }
    return result


def endsWith():
    print('asdf')

def containsStr():
    print('asdf')
     
def startDialog():
    result = {}
    print('''
    i # intials first and last
    f or l # starts with
    f2 or l2 # starts and ends with
    f3 or l3 # ends with
    fc or lc # contains set of characters
    q # stop the script
    ''')
    option = input('Enter one of these options to begin: ').lower()
    print()
    if option == 'i': 
        result = initials()
    elif option == 'f' or option == 'l':
        result = startsWith(option)
    elif option == 'f2' or option == 'l2':
        result = startsEndsWith(option)
    elif option == 'f3' or option == 'l3':
        result = endsWith(option)
    elif option == 'fc' or option == 'lc':
        result = containsStr(option)
    elif option == 'q':
        exit()
    else:
        print('Invalid option entry')
        startDialog()
    print()
    print('Found '+str(result["trueCount"])+' matches from '+str(result["totalCount"])+' names')
    printSave = input('Print the matches, save them to a text file, or both? (p/s/b): ').lower()
    if printSave == 'p' or printSave == 'b':
        print()
        print(result["names"])
    if printSave == 's' or printSave == 'b':
        f = io.open(result["newFileName"], 'w')
        f.write(result["names"])
        f.close()
    print('########################################################')
    startDialog()
    
print('############################')
print('# Name Finder has started! #')
print('############################')
startDialog()