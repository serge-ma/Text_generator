from nltk import bigrams
from collections import Counter
import random

corpus_file = input()
with open(corpus_file, "r", encoding="utf-8") as corpus:
    tokens = corpus.read().split()
bigram_list = list(bigrams(tokens))

dictionary = {}
for head, tail in bigram_list:
    dictionary.setdefault(head, Counter())
    dictionary[head].update([tail])

for _ in range(10):
    sentence = [random.choice(tokens)]
    while sentence[0][0].islower() or sentence[0][-1] in '.!?-':  # Check the first and last letters
        sentence = [random.choice(tokens)]
    while len(sentence) < 5 or sentence[-1][-1] not in '.!?':  # Check last letter in the last word
        tail_list = list(dictionary[sentence[-1]].keys())
        freq_list = list(dictionary[sentence[-1]].values())
        next_word = random.choices(tail_list, weights=freq_list)[0]
        sentence.append(next_word)
    print(*sentence)
