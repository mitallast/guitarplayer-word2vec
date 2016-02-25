# -*- coding: utf-8 -*-
import plyvel
import re, string
import sys, locale
import word2vec
import os

reload(sys)
sys.setdefaultencoding(locale.getdefaultlocale()[1])

model_path = os.path.abspath('phrases.bin')

model = word2vec.load(model_path)

tests = ['seymour', 'bkp', 'bare']

for w in tests:
    indexes, metrics = model.cosine(w, 20)
    print 'cosine for [%s]' % w
    for i in range(0, len(indexes)):
        print ' - %s %f' % (model.vocab[indexes[i]], metrics[i])

