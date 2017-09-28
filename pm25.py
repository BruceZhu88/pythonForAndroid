# -*- coding: utf8 -*-
#qpy:console
#qpy:2
import urllib
import urllib2
import json
import androidhelper
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
droid = androidhelper.Android()

city = 'guangzhou'
token = 'x' 
#url = u'http://www.pm25.in/api/querys/pm2_5.json?city=%s&token=%s'
url = u'http://www.pm25.in/shenzhen'
u2 = urllib2.urlopen(url)
#u2 = urllib2.urlopen( url % (city, token))
data = u2.read()
u2.close()

print type(data)
print data
print '-'*60
alist = []
i = 0
n = len(data)
while i < n:
    begin = data.find('{',i)
    end = data.find('}',begin)
    if begin < end:
        alist.append(data[begin:end+1])
    else:
        break
    i = end+2

blist = []
if len(alist) >2:
    for d in alist:
        j = json.JSONDecoder().decode(d)
        #print type(j)
        line = str(j["position_name"])+' '+str(j["pm2_5"])+' '+ str(j["quality"])
        print line
        blist.append(line)
    #
    droid.dialogCreateAlert(u'ว๋ักตุตใ')
    droid.dialogSetItems(blist)
    droid.dialogShow()
    # Get the selected item
    result = droid.dialogGetResponse().result
    droid.dialogDismiss()
    if 'item' in result:
        target = alist[result['item']]
        print target