# -*- coding: cp936 -*-

"""
#���ű���Ŀ���ǵ��򵥴�ͬ��
����ķ������ȶ�ȡ�����ļ�
��ԴĿ¼���ļ���һ��������ǰһ��Ŀ¼�ļ������Ա�
�Բ��첿�ֲ�ȡ�ж�������ͬ�������ϴ����ء�
"""

import sys,os,codecs
print ('start')
#sys.setdefaultencoding('utf-8')
def freefilesync_mask(item):
    #s =item
    #print (s)
    #if isinstance(item, unicode):
    #    item = item.encode('utf-8')
    #item=item.encode().decode()
    print (item)
    f=codecs.open('BatchRun.ffs_batch','r+',encoding='utf-8')
    flist=f.readlines()
    #flist[24]='                <Item>'+item+'</Item>\n'
    flist[40]='                <Left>\\PC-201704171154\Users</Left>'
    print (flist[40])
    print (flist)
    f=codecs.open('BatchRun.ffs_batch','w+',encoding='utf-8')
    f.writelines(flist)
    f.close()
    

#��ȡ�����ļ�
with open('config.ini', 'r') as f:
    #�����ļ��ԵȺ�Ϊ�ָ���
    config = dict(line.strip().split('=') for line in f if line)

#Ŀ��ԴΪ�����ļ��е�souce��
source=config['source']
#�ȶ��������յļ���֮ǰ��֮��
set_before=set()
set_after=set()
#�ж��б��ļ��Ƿ���ڣ����û�У��½�һ����

if os.path.isfile('filelist.txt'):
    pass
else:
    file1 = open("filelist.txt","w")
    file1.close()
#��ȡ�б��ļ�������1,set_before
file1 = open("filelist.txt","r")
for line in file1.readlines():
    line=line[0:-1]
    set_before.add(line)
#print ("set_before",set_before)
file1.close()
#�ѵ�ǰĿ¼�ļ���������2��set_after��д���б��ļ���
file1 = open("filelist.txt","w")
#print ("done")
for i in os.listdir(source):
    #print (i)
    set_after.add(i)
    file1.writelines(i+"\n")

file1.close() 
#��ǰ�ļ��ϼ�ȥ֮ǰ�ļ��ϣ� ����Ҫ�����ļ���  
set_fi=set_after-set_before
print (type(set_fi))
print(set_fi)
for d in set_fi:
    print (d)
    freefilesync_mask(d)
    os.system('BatchRun.ffs_batch')
    print ('done')

 
 

