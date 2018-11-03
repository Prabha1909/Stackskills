#step 1: loading the data - json file
#Step 2: returning the definition of the word - creating a function
#Step 3: Counting for non-existing words.
#step 4: Implementing the case sensitivity
#Step 5: Similarity ratio between two words. For this we must use difflib library and get_close_matches module
#Step 6: Confirmation from the user
#Step 7: Optimizing the final output
import json
from difflib import get_close_matches

data = json.load(open("C:\\Users\\pselvam\\Desktop\\Python_Tutorial\\data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data)) > 0:
        user_input = input("Did you mean {} instead? If yes type 'Y' for no type 'N'".format(get_close_matches(w, data)[0]))
        user_input = user_input.upper()
        if user_input == 'Y':
            return data[get_close_matches(w, data)[0]]
        elif user_input == 'N':
            return "The word does not exist. please try some other word"
        else:
            return "illegal entry"
    else:
        return "The word does not exist. please try some other word"


word = input("Enter the word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)