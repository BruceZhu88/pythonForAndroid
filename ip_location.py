#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import urllib
import json
ip = raw_input()
f = urllib.urlopen('http://ip.taobao.com/service/getIpInfo.php?ip=' + ip)
result = json.loads(f.read())
city = result['data']['city'].encode('utf-8')
import androidhelper
droid = androidhelper.Android()
droid.startActivity('android.intent.action.VIEW', 'geo:0.0?q=' + city)
print city