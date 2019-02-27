import json
from difflib import get_close_matches

words = json.load(open("data.json"))

def display_definition(word):
    word = word.lower()
    if word in words:
        return words[word]
    elif word.title() in words:
        return words[word.title()]
    elif word.upper() in words:
        return words[word.upper()]
    elif get_close_matches(word, words.keys(), cutoff=0.8):
        output = processing_similar_words(word)
        return output
    else:
        return "The word '%s' doesn't exist. Please double check it." % word

def processing_similar_words(word):
    similar_word = get_close_matches(word, words.keys(), cutoff=0.8)[0]
    answer = input("Did you mean %s instead? (y/n): " % similar_word)
    if answer.lower() == 'y':
        return words[similar_word]
    else:
        return "The word '%s' doesn't exist. Please double check it." % word

def run():
    word = input("Enter a word: ")
    output = display_definition(word)
    if type(output) == list:
        print("'%s' definitions:" % word)
        for definition in output:
            print(definition)
    else:
        print(output)

if __name__ == '__main__':
    run()
