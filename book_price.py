#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import android
#获得操作对象
droid = android.Android()
#运行扫描程序，返回一个元组
code = droid.scanBarcode()
#从扫描程序返回的元组中取得isbn编号
isbn = code[1]['extras']['SCAN_RESULT']
#构造查询书籍的Url
url = 'http://book.douban.com/subject_search?search_text=%s&cat=1001′ % isbn
#打开浏览器，传入构造好的Url，返回查找结果
droid.startActivity('android.intent.action.VIEW',url)