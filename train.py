# -*- coding: utf-8 -*-
import logging

from gensim.models.word2vec import Word2Vec, Text8Corpus

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def pprint(result):
    for word, score in result:
        print "%s\t%f" % (word, score)

def generate_model(filename, **kwag):
    sentences = Text8Corpus(filename)
    model = Word2Vec(sentences, **kwag)
    model.save("w2v-%s-%s.model" % (filename, kwag.__repr__()))
    return model

for window in [1, 3, 5, 7, 10]:
    model = generate_model("prettified.txt",
            window=window, size=150,
            workers=4, min_count=10)

    print window
    print "-" * 10
    for word in ["初音ミク", "炎上", "フォロー"]:
        print "---"
        pprint(model.most_similar([word]))

for size in [10, 50, 100, 150]: # 200はsegment faultが起きたのでパス
    generate_model("prettified.txt",
            window=5, size=size,
            workers=4, min_count=10)

    print size
    print "-" * 10
    for word in ["初音ミク", "炎上", "フォロー"]:
        print "---"
        pprint(model.most_similar([word]))
