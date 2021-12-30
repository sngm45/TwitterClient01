# https://qiita.com/bakira/items/00743d10ec42993f85eb

import json, config #•W€‚Ìjsonƒ‚ƒWƒ…[ƒ‹‚Æconfig.py‚Ì“Ç‚Ýž‚Ý
from requests_oauthlib import OAuth1Session #OAuth‚Ìƒ‰ƒCƒuƒ‰ƒŠ‚Ì“Ç‚Ýž‚Ý

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #”FØˆ—

url = "https://api.twitter.com/1.1/statuses/user_timeline.json" #ƒ^ƒCƒ€ƒ‰ƒCƒ“Žæ“¾ƒGƒ“ƒhƒ|ƒCƒ“ƒg

params ={'count' : 5} #Žæ“¾”
res = twitter.get(url, params = params)

if res.status_code == 200: #³í’ÊMo—ˆ‚½ê‡
    timelines = json.loads(res.text) #ƒŒƒXƒ|ƒ“ƒX‚©‚çƒ^ƒCƒ€ƒ‰ƒCƒ“ƒŠƒXƒg‚ðŽæ“¾
    for line in timelines: #ƒ^ƒCƒ€ƒ‰ƒCƒ“ƒŠƒXƒg‚ðƒ‹[ƒvˆ—
        print(line['user']['name']+'::'+line['text'])
        print(line['created_at'])
        print('*******************************************')
else: #³í’ÊMo—ˆ‚È‚©‚Á‚½ê‡
    print("Failed: %d" % res.status_code)

