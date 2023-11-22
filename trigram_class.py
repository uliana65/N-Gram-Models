from random import *
from ngram_class import ngramModel
import re



class Trigram:
    """
    Trigram model class.
    Picks 2 random words (previous_word, next_word) from the text corpus and loops to generate 30 words,
    updating context (previous_word with next_word value, next_word with generated word value)
    and prob.distribution (tri_prob_dist) after each iteration.
    If tri_prob_dist has no samples, updates previous_word and keeps generating a new random word for next_word variable,
    until tri_prob_dist has samples, after that, updates tri_generated_text and the loop continues.
    """
    def __init__(self, corpus):
        self.model = ngramModel(3, corpus)
        self.random_word_index_previous = randint(0, corpus.corpus_size)
        self.random_word_index_next = randint(0, corpus.corpus_size)
        self.generated_text = ''

    def generate_text(self):
        previous_word = self.model._corpus.sents[self.random_word_index_previous]
        next_word = self.model._corpus.sents[self.random_word_index_next]
        tri_prob_dist = self.model[(previous_word, next_word)]
        tri_generated_text = previous_word + " " + next_word

        c = 0
        sent_end = [".", "!", "?"]
        while c < 50:
            if c > 30 and next_word in sent_end:
                break
            else:
                if len(tri_prob_dist.samples()) > 0:
                    previous_word = next_word
                    next_word = tri_prob_dist.generate()
                    tri_prob_dist = self.model[(previous_word, next_word)]
                    tri_generated_text += " " + next_word
                    c += 1
                else:
                    previous_word = next_word
                    random_word_index_next = 0
                    while len(tri_prob_dist.samples()) == 0:
                        random_word_index_next = randint(0, self.model._corpus.corpus_size)
                        tri_prob_dist = self.model[(previous_word, self.model._corpus.sents[random_word_index_next])]

                    next_word = self.model._corpus.sents[random_word_index_next]
                    tri_generated_text += " " + next_word
                    tri_prob_dist = self.model[(previous_word, next_word)]
                    c += 1

        # remove whitespaces before punctuation
        tri_generated_text = re.sub(r'\s([,?.!"%:;](?:\s|$))', r'\1', tri_generated_text)
        self.generated_text = tri_generated_text
