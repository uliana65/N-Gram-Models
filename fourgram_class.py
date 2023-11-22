from random import *
from ngram_class import ngramModel
import re


class Fourgram:
    """
    Fourgram model class.
    Picks 3 random words (first_word, previous_word, next_word) from the text corpus and loops to generate 30 words,
    updating context (first_word with previous_word, previous_word with next_word value, next_word with generated word value)
    and prob.distribution (four_prob_dist) after each iteration.
    If four_prob_dist has no samples, updates first_word and previous_word and keeps generating a new random word
    for next_word variable, until four_prob_dist has samples, after that, updates four_generated_text and the loop continues.
    If the number of tries exceeds 100, instead of randomizing only next_word, randomizes previous_word as well,
    updates all appropriate variables and the loop continues
    """
    def __init__(self, corpus):
        self.model = ngramModel(4, corpus)
        self.random_word_index_first = randint(0, corpus.corpus_size)
        self.random_word_index_previous = randint(0, corpus.corpus_size)
        self.random_word_index_next = randint(0, corpus.corpus_size)
        self.generated_text = ''

    def generate_text(self):
        first_word = self.model._corpus.sents[self.random_word_index_first]
        previous_word = self.model._corpus.sents[self.random_word_index_previous]
        next_word = self.model._corpus.sents[self.random_word_index_next]
        four_prob_dist = self.model[(first_word, previous_word, next_word)]
        four_generated_text = first_word + " " + previous_word + " " + next_word
        c = 0
        sent_end = [".", "!", "?"]
        while c < 50:
            if c > 30 and next_word in sent_end:
                break
            else:
                if len(four_prob_dist.samples()) > 0:
                    first_word = previous_word
                    previous_word = next_word
                    next_word = four_prob_dist.generate()
                    four_prob_dist = self.model[(first_word, previous_word, next_word)]
                    four_generated_text += " " + next_word
                    c += 1
                else:
                    first_word = previous_word
                    previous_word = next_word
                    random_word_index_next = 0
                    change = False
                    tries = 0
                    while len(four_prob_dist.samples()) == 0:
                        tries += 1
                        if tries < 100:
                            random_word_index_next = randint(0, self.model._corpus.corpus_size)
                            four_prob_dist = self.model[(first_word, previous_word, self.model._corpus.sents[random_word_index_next])]
                        else:
                            change = True
                            random_word_index_previous = randint(0, self.model._corpus.corpus_size)
                            random_word_index_next = randint(0, self.model._corpus.corpus_size)
                            previous_word = self.model._corpus.sents[random_word_index_previous]
                            four_prob_dist = self.model[(first_word, previous_word, self.model._corpus.sents[random_word_index_next])]
                    if change:
                        four_generated_text += " " + previous_word
                    next_word = self.model._corpus.sents[random_word_index_next]
                    four_generated_text += " " + next_word
                    c += 1

        # remove whitespaces before punctuation
        four_generated_text = re.sub(r'\s([,?.!"%:;](?:\s|$))', r'\1', four_generated_text)
        self.generated_text = four_generated_text
