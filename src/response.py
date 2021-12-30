# https://qiita.com/bakira/items/00743d10ec42993f85eb

import config
from requests_oauthlib import OAuth1Session
import datetime, time

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #”FØˆ—

url = "https://api.twitter.com/1.1/statuses/user_timeline.json" #ƒ^ƒCƒ€ƒ‰ƒCƒ“Žæ“¾ƒGƒ“ƒhƒ|ƒCƒ“ƒg

res = twitter.get(url)

limit = res.headers['x-rate-limit-remaining'] #ƒŠƒNƒGƒXƒg‰Â”\Žc”‚ÌŽæ“¾
reset = res.headers['x-rate-limit-reset'] #ƒŠƒNƒGƒXƒgŠŽc”ƒŠƒZƒbƒg‚Ü‚Å‚ÌŽžŠÔ(UTC)
sec = int(res.headers['X-Rate-Limit-Reset']) - time.mktime(datetime.datetime.now().timetuple()) #UTC‚ð•b”‚É•ÏŠ·

print ("limit: " + limit)
print ("reset: " +  reset)
print ('reset sec:  %s' % sec)

