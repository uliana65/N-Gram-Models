from nltk.probability import (ConditionalFreqDist, ConditionalProbDist, MLEProbDist, SimpleGoodTuringProbDist)
from nltk.util import ngrams


class ngramModel(ConditionalProbDist):
    """
    Define and train an Ngram Model over the corpus represented by the list of words.
    Given a BasicNgram instance ngram and a (n-1)-gram context (i.e., a tuple of n-1 strings),
    a call to ngram[context] returns a nltk.probability.ProbDistI object representing the Probability distribution P(.|context) over possible values for the next word. 
    Be aware that context has to be a tuple, even if context is a unigram (see example below)
    
    >>> corpus=['a','b','b','a']
    >>> bigram=ngramModel(2,corpus)
    >>> bigram.contexts()
    [('<$>',), ('a',), ('b',)]
    >>> p_b=bigram[('b',)] #not bigram['b']!!!
    >>> p_b.prob('a')
    0.5
    >>> p_b.prob('b')
    0.5
    
    :param n: the dimension of the n-grams (i.e. the size of the context+1).
    :type n: int
    :param corpus: 
    :type corpus: list(Str)
    
    other parameters are optional and may be omitted. They define whether to add artificial symbols before or after the word list, 
    and whether to use another estimation methods than maximum likelihood.
    """
    def __init__(self, n, corpus):
        self._n = n
        self._corpus = corpus
        self._start_symbol = "<$>"
        self._end_symbol = "</$>"
        self._pad_left = True
        self._pad_right = False

        self._counter = ConditionalFreqDist()
        self._train()
        super().__init__(self._counter, self.ml_estimator)

    def _train(self):
        _ngrams = self.generate_ngrams()
        for ngram in _ngrams:
            context = ngram[0:-1]
            outcome = ngram[-1]
            self._counter[context][outcome] += 1

    def generate_ngrams(self):
        """
        returns an iterable over the ngrams of the corpus
        """
        return ngrams(self._corpus.sents, self._n, pad_left=self._pad_left, pad_right=self._pad_right,
                      left_pad_symbol=self._start_symbol,
                      right_pad_symbol=self._end_symbol)

    def contexts(self):
        """
        Return the list of contexts
        """
        return list(self.conditions())

    def ml_estimator(self, freqdist):
        return MLEProbDist(freqdist)

    def goodturing_estimator(self, freqdist):
        return SimpleGoodTuringProbDist(freqdist)

