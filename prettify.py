# -*- coding: utf-8 -*-
import codecs
import unicodedata

import MeCab

min_words = 10
originate=False
reject = [u"w", u"ｗ", u"(", u"「", u"（", u"【", u"#"]
debug = False

tagger = MeCab.Tagger()
parse = tagger.parse

f = codecs.open("corpus.txt", encoding="utf-8")
out = codecs.open("prettified.txt", "w", encoding="utf-8")
for line in f:
    line = unicodedata.normalize('NFKC', line)
    rejected = False
    for reject_word in reject:
        if reject_word in line:
            rejected = True
            break
    if rejected:
        continue

    sentence = line.strip()

    result = parse(sentence.encode("utf-8"))
    words = []
    for word in result.split("\n"):
        if word == "EOS":
            break
        word, features = word.split("\t")
        if originate:
            features = features.split(",")
            if features[6] != "*":
                word = features[6]
        words.append(word.decode("utf-8").lower())

    if len(words) >= min_words:
        if debug:
            print " ".join(words)
        out.write("%s\n" % " ".join(words))
