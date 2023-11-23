# N-Gram-Models 
## Computational Linguistics Course 
### Assignment 1 

My solution of the assignment on N-gram language models. The models include bigram, trigram, and 4-gram models. The discussion of the models' performance is provided in the [report](https://github.com/uliana65/N-Gram-Models/blob/main/discussion.pdf).  

### Usage 

`python3 train_ngram_model.py --corpus file_name.txt --n N`

where N is a number of tokens for an N-gram model (can be 2, 3, 4). Sample corpus is povided ("biden_speeches.txt") 

### Expected behaviour

After training on the provided discourse, the model picks a random N-gram and generates a 30-50 word text piece. 
