import json
from difflib import get_close_matches

data = json.load(open("C:\\Users\\pselvam\\Desktop\\Python_Tutorial\\data.json"))

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        return "Did you mean {} instead?".format(get_close_matches(w, data.keys(), cutoff=0.8)[0])
    else:
        return "The word is not in the dictionary"

word = input("Enter the word: ")

print(meaning(word))