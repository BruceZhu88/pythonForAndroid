#coding=utf-8
#qpy:console
#qpy:2

import site
from sl4a import Android
import re,time,json
from urllib.request import urlopen
import urllib
d=Android()



while True:
    while True:
        if d.ttsIsSpeaking().result==False:
            speech=d.recognizeSpeech().result
            speech=re.sub('.','',speech)
            #speech=input('>')
            if speech=='over' or speech=='Over':
                d.ttsSpeak('Good bye')
                exit()
            if re.search('open',speech):
                speech=re.sub('open','',speech)
                app=d.getLaunchableApplications().result
                try:
                    d.launch(app[speech]) 
                    cmd='opened'+speech
                    d.ttsSpeak(cmd)    
                except:
                    d.ttsSpeak('No such application')
                    break
                exit()
                
            if speech=='time' or speech=='Time':
                ctime=time.ctime()[11:19].split(':')
                if ctime[1]=='00':
                    ctime='now time is ',+ctime[0]
                    d.ttsSpeak(ctime)
                    break
                else:
                    ctime='now time is '+str(ctime[0])+str(ctime[1])
                    d.ttsSpeak(ctime)
                    break
					
			