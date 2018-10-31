import json
from difflib import get_close_matches

data = json.load(open("C:\\Users\\pselvam\\Desktop\\Python_Tutorial\\data.json"))

def meaning(w):
    w = w.lower()
    w = input("Did you mean {}? enter y for yes and n for No".format(get_close_matches(w, data.keys())[0]))
    if w in data:
        return data[w]
    else:
        return "The word is not in the dictionary"

word = input("Enter the word: ")

print(meaning(word))