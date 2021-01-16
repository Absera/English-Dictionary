import json
import random

file = open("dictionary.json", "r")
data = json.load(file)
words = [i for i in data.keys()]



def generateRandom():
    global random_word, data, words
    random_word = random.choice(words)
    return {
        "word": random_word,
        "definition": data[random_word]
    }


def translate(word):
    global data
    try:
        return {
            "word": word,
            "definition": data[word]
        }
    except:
        return {
            "word": word,
            "definition": "Oww! No definition found!"
        }
