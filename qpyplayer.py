#coding=utf-8
#qpy:console
#qpy:2

import os,re,json,time,traceback,thread,androidhelper

#进入当前脚本目录
os.chdir(os.path.dirname(__file__))

d=androidhelper.Android()



#基本设置：路径、音乐格式--------
	
#   * 音乐搜索路径 *
musicpath='/sdcard'

#    * 音乐格式 *
musictype='.mp3'

#--------------------------------

d.mediaPlayClose()



#操作函数开始--------------------


#更新列表    * update *
def update_list():
    print ('正在搜索音乐...')
    dirs=[[],[]]
    f=open('music.list','w')
    '''
    在指定路径搜索指定格式后缀的文件，生成dirs列表
    dirs[0]是音乐文件的文件夹，dirs[1]是音乐文件的文件名
    dirs[0]+'/'+dirs[1]就是每个文件的绝对路径
    '''
    for i in os.walk(musicpath):
        for j in i[2]:
            if j[-4:]==musictype:
                dirs[0].append(i[0])
                dirs[1].append(j)
    dir2=json.dumps(dirs)
    f.write(dir2)
    f.close()
    print'搜索到'+str(len(dirs[1]))+'首音乐'
    print '正在生成播放列表...'


#播放列表     * list *
def music_list():
    f=open('music.list','r')
    h=f.read()
    f.close()
    dirs=json.loads(h)
    for i in range(len(dirs[1])):       
        print str(i)+'. '+dirs[1][i].encode('utf-8')


#播放音乐    * num *
def play(num):
    num=int(num)    
    f=open('music.list','r')
    h=f.read()
    f.close()
    dirs=json.loads(h)
    try:
        mf=dirs[0][num]+'/'+dirs[1][num]
        d.mediaPlay(mf)
        print '\n当前播放:',dirs[1][num].encode('utf-8')
        if num<len(dirs[1])-1:
            num=num+1
        elif num==len(dirs[1])-1:
            num=0
        while True:
            for i in range(num,len(dirs[1])):
                while True:
                    time.sleep(1)
                    if d.mediaIsPlaying().result == False:
                        if i==len(dirs[1])-1:
                            num=0
                        mf=dirs[0][i]+'/'+dirs[1][i]
                        d.mediaPlay(mf)
                        print '\n当前播放:',dirs[1][i].encode('utf-8')
                        break                 
    except Exception,e:
        exc=traceback.format_exc()
        print exc


#下一首
def next():
    d.mediaPlayClose()

#头部
def header():
    print '+'*9+'qpy player'+'*'*9
    
    

#帮助
def help():
	print '首次使用请在文件头修改音乐路径'
	print '首次运行需要先更新列表'
	print 'update-----更新列表'
	print 'list-------显示列表'
	print '直接输入音乐序号播放'
	print 'next-------下一首'
	print 'quit-------停止并退出'
	print '播放音乐后再回车一下可输入命令'





while True:
    header()
    while True:
        m=raw_input('music$ ')
        if m=='list':
            music_list()
        if m=='update':
            update_list()
        if re.search('\d',m):
            thread.start_new_thread(play,(m,))
        if m=='next':
            next()
        if m=='quit':
            d.mediaPlayClose()
            exit()
        if m=='help':
        	help()
            
        

