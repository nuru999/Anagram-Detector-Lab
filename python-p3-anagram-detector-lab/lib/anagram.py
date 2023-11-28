#BDD
# input: Angel
# output: glean
# behaviour: returns an anagram of the input

# Pseudo Code
# Define a class -Anagram that takes a word(string) on initialization
# Define an instance method- match that takes a  defaults to an empty list
# Have the word initialized in a list and each word in the match list sorted
# Check if they are equal
# If any of the words in the match list  equals the initialized word, return True
# If none of the words in the match list equal the initialized list, return False

class Anagram:
    def __init__(self,word):
        self.word = sorted(word.lower())
    def match(self,listy=[]):
        match = [x for x in listy if self.word == sorted(x.lower()) ]
        return match if match else []

a = Anagram("Angel")
print(a.match(['enlists', 'google', 'inlets', 'banana','glean']))
