import json
from difflib import get_close_matches

data = json.load(open("C:\\Users\\pselvam\\Desktop\\Python_Tutorial\\data.json"))

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        user_input = input("Did you mean {} instead? Enter Y if Yes and N if No".format(get_close_matches(w, data.keys(), cutoff=0.8)[0]))
        user_input = user_input.upper()
        if user_input == 'Y':
            return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
        elif user_input == 'N':
            return "The word is not in the dictionary"
        else:
            return "Check the input"
    else:
        return "The word is not in the dictionary"

word = input("Enter the word: ")

output = meaning(word)
if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)