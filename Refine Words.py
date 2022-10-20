def refinewords(myword):
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")
    outputwords = []
    for eachword in mywords:
        eachletter = set(eachword.lower())
        #print (eachletter)
        if (eachletter.issubset(row1) or eachletter.issubset(row2) or eachletter.issubset(row3)):
            outputwords.append(eachword)
    return outputwords
mywords = ["Alaska", "Dad", "peace", "School"]
print (refinewords(mywords))
