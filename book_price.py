#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import android
#��ò�������
droid = android.Android()
#����ɨ����򣬷���һ��Ԫ��
code = droid.scanBarcode()
#��ɨ����򷵻ص�Ԫ����ȡ��isbn���
isbn = code[1]['extras']['SCAN_RESULT']
#�����ѯ�鼮��Url
url = 'http://book.douban.com/subject_search?search_text=%s&cat=1001�� % isbn
#������������빹��õ�Url�����ز��ҽ��
droid.startActivity('android.intent.action.VIEW',url)