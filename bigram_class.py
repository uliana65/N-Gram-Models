from random import *
from ngram_class import ngramModel
import re


class Bigram:
    """
    Bigram model class.
    Picks a random word from the text corpus and loops to generate 30 words,
    updating context (next_word) and prob.distribution (bi_prob_dist) after each iteration.
    If bi_prob_dist has no samples, generates another random word and the loop continues.
    """
    def __init__(self, corpus):
        self.model = ngramModel(2, corpus)
        self.random_word_index = randint(0, corpus.corpus_size)
        self.generated_text = ''

    def generate_text(self):
        random_word = self.model._corpus.sents[self.random_word_index]
        bi_prob_dist = self.model[(random_word,)]
        bi_generated_text = str(random_word)
        c = 0
        sent_end = [".", "!", "?"]
        while c < 50:
            if c > 30 and next_word in sent_end:
                break
            else:
                if len(bi_prob_dist.samples()) > 0:
                    next_word = bi_prob_dist.generate()
                    bi_prob_dist = self.model[(next_word,)]
                    bi_generated_text += " " + next_word
                    c += 1
                else:
                    random_word_index = randint(0, self.model._corpus.corpus_size)
                    random_word = self.model._corpus.sents[random_word_index]
                    bi_generated_text += " " + random_word
                    bi_prob_dist = self.model[(random_word,)]
                    c += 1

        # remove whitespaces before punctuation
        bi_generated_text = re.sub(r'\s([,?.!"%:;](?:\s|$))', r'\1', bi_generated_text)
        self.generated_text = bi_generated_text
