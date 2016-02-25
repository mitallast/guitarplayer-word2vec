# -*- coding: utf-8 -*-
import plyvel
import re, string
import sys, locale


reload(sys)
sys.setdefaultencoding(locale.getdefaultlocale()[1])

db = plyvel.DB('guitarplayer.db', create_if_missing=False)

f = open('text.txt', 'w')

for key, value in db:
    print key, value
    value = value.decode('utf8')
    words = re.findall(u'[a-zA-Zа-яА-Я0-9-]+', value.lower(), flags=re.UNICODE)
    if len(words) > 0:
        line = string.join(words, ' ') + '\n'
        f.write(line.encode('utf8'))

db.close()
f.close()

