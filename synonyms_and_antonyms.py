import nltk
from nltk.corpus import wordnet


nltk.download('wordnet')


# Antonyms for the word "increase"
antonyms = []
for syn in wordnet.synsets("increase"):
    for lm in syn.lemmas():
        if lm.antonyms():
            antonyms.append(lm.antonyms()[0].name())
print(set(antonyms))
"""
answer: {'decrease', 'decrement'}
"""

# To find the meaning of the word
syn = wordnet.synsets("teaching")
print(syn)
print('Word and Type : ' + syn[0].name())
print('Synonym of teaching is: ' + syn[0].lemmas()[0].name())
print('The meaning of the teaching: ' + syn[0].definition())
print('Example of teaching : ' + str(syn[0].examples()))

"""
answer: 
    [Synset('teaching.n.01'), Synset('teaching.n.02'), Synset('education.n.01'), Synset('teach.v.01'), Synset('teach.v.02')]
    Word and Type : teaching.n.01
    Synonym of teaching is: teaching
    The meaning of the teaching: the profession of a teacher
    Example of teaching : ['he prepared for teaching while still in college', 'pedagogy is recognized as an important profession']
"""

# Synonym for the word "travel"
synonyms = []
for syn in wordnet.synsets("travel"):
    for lm in syn.lemmas():
        synonyms.append(lm.name())
print(set(synonyms))
"""
answer: 
    {'travelling', 'locomotion', 'locomote', 'journey', 'move_around', 'trip', 
    'change_of_location', 'go', 'traveling', 'move', 'jaunt', 'travel'}

"""

