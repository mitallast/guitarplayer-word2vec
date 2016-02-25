# -*- coding: utf-8 -*-
from grab import Grab
import plyvel
from urlparse import urlparse, parse_qs

db = plyvel.DB('guitarplayer.db', create_if_missing=True)

g = Grab()
for i in range(0, 13160, 40):
    g.go("http://forum.guitarplayer.ru/index.php?board=18.%s" % i)
    for i in g.doc.select('//div/span[@id]/a'):
        url = i.attr('href')
        title = i.text()
        topic = parse_qs(urlparse(url).query)['topic'][0]
        if db.get(topic.encode('utf8')) is None:
            db.put(topic.encode('utf8'), title.encode('utf8'))

db.close()
