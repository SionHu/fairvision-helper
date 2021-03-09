# Welcome to NLP Server for fairvision.net!

This repo is used to accomplish all the NLP post-processing tasks from the [fairvision project](http://fairvision.net/).


## Installation
You should always check the nice documentation of [Sense2Vec](https://github.com/explosion/sense2vec) if you run into problems. 

#### Create and activate conda virtual environment: 
`conda create --name fvhelper python=3.8`

`conda activate fvhelper`

#### Install dependencies: 
`pip install -r requirements`

(If you run in to problems of nltk, check [this post](https://stackoverflow.com/questions/4867197/failed-loading-english-pickle-with-nltk-data-load))

#### Download pre-trained models: 
Follow the [Sense2Vec instruction](https://github.com/explosion/sense2vec#pretrained-vectors). Use `tar -xvf name_of_model` to unzip the downloaded file. Remember to update the path to your model in `main.py`. 
