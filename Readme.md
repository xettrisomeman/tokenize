# Tokenizing Nepali Text Sentences 


## Installation Guide

```python
pip install nepali_tokenizer
```

## Usage


```python
from nepali_tokenizer import NepaliTokenizer

tokenize = NepaliTokenizer()
print(tokenize.tokenizer('के छ खबर तिम्रो ? '))

# output--> ['खबर','तिम्रो']
```

## We can use it with pandas dataframe too

```python

#for example

df.head()

#---> List of nepali corpora with 100 rows

tokenize=NepaliTokenizer()

df = df[0].apply(tokenize.tokenizer)

#output--> All the text in tokenized forms

```

Feel Free to Contribute.