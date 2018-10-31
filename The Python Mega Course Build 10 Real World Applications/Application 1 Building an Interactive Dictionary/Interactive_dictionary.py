import json

data = json.load(open("C:\\Users\\pselvam\\Desktop\\Python_Tutorial\\data.json"))

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word is not in the dictionary"


word = input("Enter the word: ")


print(meaning(word))
