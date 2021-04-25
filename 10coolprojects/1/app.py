import json
from difflib import get_close_matches
data = json.load(open("./data.json"))

def getMeaning(word):
    if word in data:
        print(data[word])
    else:
        print("Word does not exist in the dictionary ")
        possibilities = get_close_matches(word,data.keys(),1,0.8)
        if possibilities:
            yn = input("Did you mean ?  {0} \n".format(possibilities[0]))
            if yn:
                print(data[possibilities[0]])

word = input("Enter word\n")
getMeaning(word.lower())
