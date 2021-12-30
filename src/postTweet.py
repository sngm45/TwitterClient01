# https://qiita.com/bakira/items/00743d10ec42993f85eb

import json, config #•W€‚Ìjsonƒ‚ƒWƒ…[ƒ‹‚Æconfig.py‚Ì“Ç‚Ýž‚Ý
from requests_oauthlib import OAuth1Session #OAuth‚Ìƒ‰ƒCƒuƒ‰ƒŠ‚Ì“Ç‚Ýž‚Ý

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #”FØˆ—

url = "https://api.twitter.com/1.1/statuses/update.json" #ƒcƒC[ƒgƒ|ƒXƒgƒGƒ“ƒhƒ|ƒCƒ“ƒg

print("Tweet your latest status:")
tweet = input('>> ') #ƒL[ƒ{[ƒh“ü—Í‚ÌŽæ“¾
print('*******************************************')

params = {"status" : tweet}

res = twitter.post(url, params = params) #post‘—M

if res.status_code == 200: #³í“Šeo—ˆ‚½ê‡
    print("Success.")
else: #³í“Šeo—ˆ‚È‚©‚Á‚½ê‡
    print("Failed. : %d"% res.status_code)
