from corpus_class import Corpus
import argparse
from bigram_class import Bigram
from trigram_class import Trigram
from fourgram_class import Fourgram


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--corpus', type=str,
                        help='path to corpus file (required)')
    parser.add_argument('--n', type=int,
                        help='number of tokens for n-gram model (required), options: 2, 3, 4')


    args = parser.parse_args()
    assert 2 <= args.n <= 4, f"this n-gram model is not supported (N entered: {args.n})"

    file_name = args.corpus

    corpus = Corpus(file_name)
    corpus.read_corpus()

    if args.n == 2:
        model = Bigram(corpus)
        model.generate_text()
        print(model.generated_text)
    elif args.n == 3:
        model = Trigram(corpus)
        model.generate_text()
        print(model.generated_text)
    elif args.n == 4:
        model = Fourgram(corpus)
        model.generate_text()
        print(model.generated_text)
