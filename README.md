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

Example output of predict.py with keyword "bare":

```
164755.0 Продал Bareknuckle Nailbomb
234349.0 Продам сэт АКТИВНЫХ звукоснимателей Gibson GEM Active Open Coil pickups
247365.0 Продаю звукосниматель Bareknuckle Nailbomb новый 3500р в Москве
261901.0 Продам/обменяю BareKnuckle Nailbomb 7 strings Питер. 3600руб.
263720.0 Bareknuckle Warpig bridge 6 string
268289.0 BKP warpig pickups продам
279797.0 Продано BKP Aftermath
285476.0 BKP Painkiller - продан
290040.0 Продам сэт Rebel Yell и 57 classic
294677.0 BKP Aftermath (копия от Fokin Pickups)
299241.0 BKP Painkiller 7
300253.0 BKP Aftermath set
303061.0 Продам\обменяю 7миструнные Bkp Aftermath сэт или по одному
303144.0 (ПРОДАНО) Продам звукосниматель BareKnuckle Aftermath (7 string)
322729.0 ПродаН сэт BK Aftermath 7str за 5000 рублей
323783.0 BKP Aftermath Bridge + BKP Cold Sweat Neck (7string)
325895.0 сэт BK Aftermath 7str 7500руб(продано)
333770.0 BKP Aftermath 7-string Battle-worn
334467.0 Продам BKP 6 String Aftermath humbucker - Calibrated Covered Set
336941.0 Продам сет BKP nailbomb ПРОДАНО!
340983.0 Продал BareKnuckle Warpig
345564.0 BKP Warpig Covered Set 7
350063.0 Куплю BKP Painkiller или Aftermath
350798.0 Крутанские хамбы: BKP Rebel Yell Neck + Amalfitano Bridge. продано
```
