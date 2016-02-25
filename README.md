Example script for word2vec model with data from forum.guitarplayer.ru

 - `load.py` collect commerce post titles from forum
 - `extract.py` extract keywords from raw data and prepare it for training
 - `train.py` train word2vec model from prepared training data
 - `test.py` load trained word2vec model and run some cosine similarity tests
 - `predict.py` search posts with word2vec model for related for search keyword


Example output of test.py:

```
cosine for [seymour]
59 jb sh-4 sh-1n blackouts sh-2n sh-1 ahb-1 little tb-4
cosine for [bkp]
бутиковый covered bareknuckle cold holydiver 6000 хамбакеры сета sweat the
cosine for [bare]
warpig nailbomb rebel yell calibrated open aftermath painkiller hawk knuckle
```

Example output of predict.py:

```
101389.0 Bare Knuckle, Lundgren + Schaller и Floyd
106282.0 Продаю Bare Knuckle Nailbomb
137694.0 Bare Knuckle Nailbomb. Продан
157910.0 Cэт Bare Knuckle pickups "Rebel Yell"
164774.0 Продано Bare Knuckle Holydiver 7
168589.0 Обмен Bare Knukle PAinkiller, DiMarzio Fast Track 2
172148.0 Продан Bare Knuckle Nailbomb (bridge)
174214.0 Продано Bare Knuckle Holydiver
180655.0 Bare Knuckle Pig-90 (горячие P90)
182311.0 Предложение СНЯТО. Меняю 1:1 Bare Knuckle NailBomb на Gibson 57+
182610.0 Bare Knuckle Rebel Yell (продан)
186031.0 Продам звукосниматели Bare Knuckle Warpig, Dimarzio Super Distortion, EMG-58
187009.0 Продаю комплект Bare Knuckle Cold Sweat - Москва
189119.0 ОБМЕН Bare Knukle WARPIG (сет) на Bare Knukle серии Vintage или 8000р
190952.0 Сет Bare Knukle COLD SWEAT.7.500.Отправлю ЕМС.
193249.0 Bare Knucke Nailbomb Bridge (ПРОДАН)
193750.0 [Москва] Bare Knuсkle Nailbomb Calibrated Set - ПРОДАНО.
194915.0 Bare Knuckle Cold Sweat set ПРОДАМ!
196024.0 Звукосниматель Bare Knuckle - War Pig для семиструнки 4000р
198755.0 куплю bare knuckle black dog сет
199310.0 Bare Knuckle,Lollar,Gibson
204518.0 ПРОДАН BARE KNUCKLE WARPIG
204560.0 7миструные Seymour Duncan SH8 Invader 7, SH6 7, Bare Knuckle pain killer 7
205461.0 ПРОДАМ\ОБМЕНЯЮ Bare Knuckle Miracle Man 7 струн!
208028.0 Bare Knuckle Cold Sweat calibrated covered set - ПРОДАМ !!!
213707.0 Обменяю Bare Knuckle Warpig
214950.0 Продал: Bare Knukle humbuckers: Holydiver neck.
216727.0 ПРОДАЮ ДАТЧИКИ BARE KNUCKLE VH-II humbucker
```
