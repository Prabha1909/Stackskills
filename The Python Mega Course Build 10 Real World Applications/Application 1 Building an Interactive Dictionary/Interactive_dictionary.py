import json

data = json.load(open("C:\\Users\\pselvam\\Desktop\\Python_Tutorial\\data.json"))

def meaning():
    word = input("Enter the word: ")
    if word in data:
        return data[word.lower()]
    else:
        return "The word is not in the dictionary"

print(meaning())
