from collections import OrderedDict

def countvowels(thestring):

    vowels = ['a','e','i','o','u']

    stringlist = list(thestring)
    newlist = [char for char in stringlist if char in vowels]
    listtuple = tuple(newlist)
    removeduplicates = "".join(OrderedDict.fromkeys(listtuple))
    vowelstuple = (removeduplicates,)
    thestringduplicates = [letter for letter in thestring if thestring.count(letter) > 1]
    uniquecharacters = "".join(OrderedDict.fromkeys(thestringduplicates))
    tuple_uniquecharacters = tuple(uniquecharacters)
    totalvowels = len(tuple_uniquecharacters)
    totalvowelstuple = (totalvowels,)
    finaltuple = vowelstuple + totalvowelstuple

    print(finaltuple)

countvowels("dahdah")
countvowels("drink water")