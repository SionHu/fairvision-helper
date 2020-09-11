from sense2vec import Sense2Vec, Sense2VecComponent
import spacy
from spacy.tokens import Span
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from unidecode import unidecode
from collections import Counter
import numpy as np
import string
import itertools
import csv
import json
from spellchecker import SpellChecker

# Load the essential models
nlp = spacy.load("en_core_web_sm") # needs to be replaced with large model
s2vOrg = Sense2Vec().from_disk("./data/s2v_reddit_2015_md")
s2v = Sense2VecComponent(nlp.vocab).from_disk("./data/s2v_reddit_2015_md")
nlp.add_pipe(s2v)

def loadFile(path):
    corpuses = [] # used to store final results
    file = open(path, "rt", encoding="utf-8")
    # data = csv.reader(file, delimiter=",")
    data = csv.DictReader(file)
    removeEntries = ['isFinal', 'category', 'hit', 'mergeParent']
    for row in data:
        dict = list(map(row.pop, removeEntries))
        corpuses.append(row)
    # print(corpuses)
    return corpuses

def pre_process(corpusDict):
    """ Take one dict of the input files, and prcoess the 'text' """
    # print("corpus:", corpus)
    corpus = str(corpusDict.get('text')).lower()
    # remove non-ascii characters
    corpus = unidecode(corpus)
    # lemmatize
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(corpus)

    newCorpus = " "
    for w in words: newCorpus += " " + lemmatizer.lemmatize(w)
    # configure stopwords and punctuations
    addStopwords = ["airplane", "plane", "image", "picture"]
    remStopwords = ["what", "where", "how", "when", "doing", "do"]
    stopset = stopwords.words('english') + list(string.punctuation) + addStopwords
    # stopset = [word for word in stopset if word not in remStopwords]

    # add tags to tokens
    tagList = addTag(newCorpus)
    tokens = []
    for token in tagList:
        if token and token.split('|')[0] not in stopset and "SPACE" not in token:
            tokens.append(token)
    corpusDict['tokens'] = tokens
    # print("newDict:", corpusDict)
    return corpusDict

def addTag(docs):
    # check spelling
    spell = SpellChecker()
    docs = ' '.join([spell.correction(word) for word in docs.split(' ')])
    docs = nlp(docs) # convert the text into SpaCy format
    newDocs = []
    for token in docs:
        if token.pos_ != 'PROPN': # all NOUNs are considered as PROPN by mistake
            newDocs.append(token.text + '|' + token.pos_)
        else: newDocs.append(token.text + '|' + 'NOUN')
    return newDocs

def mergeDocs(docs):
    """ Compare all docs and merged the ones higher than the threshold.
        Threshold: 0.7
    """
    # compare the questions to each other
    mDocs = [] # used to store the final merged docs dict
    for i,j in itertools.combinations(range(len(docs)), 2):
        tokens1, tokens2 = docs[i].get('tokens'), docs[j].get('tokens')
        if not tokens1 or not tokens2:
            pass
        else:
            # print("Curren tokens:", tokens1, tokens2)
            simScore = s2vOrg.similarity(tokens1, tokens2)
            # print("- Comparing:", tokens1, tokens2, '=>', simScore)
        if simScore >= 0.7:
            mDocs.extend([docs[i], docs[j]])
            print("Merging:", docs[i].get('text'), "==", docs[j].get('text'))

if __name__ == '__main__':
    print(" -- Pipeline Information -- \n", nlp.pipe_names)
    # For larger testing
    corpuses = loadFile('./data/airplaneQuestions.csv')

    docs = [d for corpus in corpuses for d in [pre_process(corpus)] if d]
    mergeDocs(docs)

    # testing field
    # doc1 = ['how|ADV', 'many|ADJ', 'land|NOUN']
    # doc2 = ['what|PRON', 'parked|VERB']
    # print(s2vOrg.similarity(doc1, doc2))
