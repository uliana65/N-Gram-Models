from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.lm.preprocessing import flatten


class Corpus:
    """
    This class handles data file with text and stores preprocessed data.

    :param file_name: file name with text data
    :param corpus: list of tokenized corpus data
    :param corpus_size: number of tokens in the corpus
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.sents = []
        self.corpus_size = 0

    def read_corpus(self):
        """
        Reads in txt file, split into sent and tokens, appends tokens to corpus
        :return: none
        """
        sent_end_char = ".!?;"
        with open(self.file_name, "r", encoding="utf-8") as f:
            text = " ".join(f.readlines())
            # tokenize words in sents -> list of lists
            text = [word_tokenize(t) for t in sent_tokenize(text)]
            self.sents = list(flatten(sent for sent in text))
        self.corpus_size = len(self.sents)

