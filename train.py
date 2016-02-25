# -*- coding: utf-8 -*-
import plyvel
import re, string
import sys, locale
import word2vec
import os

reload(sys)
sys.setdefaultencoding(locale.getdefaultlocale()[1])


model_path = os.path.abspath('model.bin')
text_path = os.path.abspath('text.txt')
phrase_path = os.path.abspath('phrases.txt')

word2vec.word2phrase(text_path, phrase_path, verbose=True)
word2vec.word2vec(phrase_path, model_path, binary=1, verbose=True)
model = word2vec.load(model_path)

indexes, metrics = model.cosine('seymour')
print (string.join(model.vocab[indexes], ' '))

