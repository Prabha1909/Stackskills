import json

data = json.load(open("C:\\Users\\pselvam\\Desktop\\Python_Tutorial\\data.json"))

def meaning(word):
    return data[word]

print(meaning("rain"))
