import nltk
import numpy as np

nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)



def stem(word):
    return stemmer.stem(word.lower())



def bag_of_word(tokenize_sentence, all_words):
    """
    sentence = ["hello","how","are","you"]
    words  = ["hi","hello","I","you","bye","thank","cool"]
    bag  = [0,1,0,1,0,0,0]
    """
    tokenize_sentence = [stem(w) for w in tokenize_sentence]
    bag  = np.zeros(len(all_words),dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenize_sentence:
            bag[idx] = 1.0
    return bag








# a = "how long does shipping take ?"
# print(a)

# a = tokenize(a)
# print(a)

# words = ['Organize','organizes','organizing']
# stemed_words = [stem(w) for w in words]
# print(stemed_words) 




