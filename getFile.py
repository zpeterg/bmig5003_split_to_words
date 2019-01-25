
def getFile(filename):
    file = open(filename, 'r')
    rtn = []
    # append each line with a space
    for line in file:
        for word in line.split(' '):
            rtn.append(word)
    file.close()
    return rtn
