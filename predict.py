# -*- coding: utf-8 -*-
import plyvel
import re, string
import sys, locale
import word2vec
import os
import numpy as np

reload(sys)
sys.setdefaultencoding(locale.getdefaultlocale()[1])

model_path = os.path.abspath('phrases.bin')
model = word2vec.load(model_path)

db = plyvel.DB('guitarplayer.db', create_if_missing=False)

search = model['bare']

for key, value in db:
    value = value.decode('utf8')
    words = re.findall(u'[a-zA-Zа-яА-Я0-9-]+', value.lower(), flags=re.UNICODE)
    words = filter(lambda w: w in model, words)
    if len(words) > 0:
	vectors = map(lambda w: model.get_vector(w), words)
	metrics = np.dot(vectors, search.T)
	best = metrics[metrics.argmax()]
	# filter full matched docs
        if best > 0.8 and best < 1:
	    print key, value
	
	
db.close()
