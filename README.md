# N-Gram-Models

My implementation of N-gram language models for random text generation based on probabilities. The scripts include bigram, trigram, and 4-gram models. The discussion of the models' performance is provided in this [file](https://github.com/uliana65/N-Gram-Models/blob/main/discussion.pdf).  

### Usage 

`python3 train_ngram_model.py --corpus file_name.txt --n N`

where N is a number of tokens for an N-gram model (can be 2, 3, 4). Sample corpus is povided ("biden_speeches.txt") 

### Expected behaviour

After training on the provided discourse, the model picks a random N-gram and generates a 30-50 word text piece. 
