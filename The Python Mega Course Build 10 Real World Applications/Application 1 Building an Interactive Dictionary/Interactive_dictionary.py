import json

data = json.load(open("C:\\Users\\pselvam\\Desktop\\Python_Tutorial\\data.json"))

def meaning(word):
    if word in data:
        return data[word]
    else:
        return "The word is not in the dictionary"


word = input("Enter the word: ")

print(meaning(word))
