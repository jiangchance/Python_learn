# -*- coding: cp936 -*-   #����ע�����
#�˳����Ŀ���Ǵ���һ��webservice��ҳ����ҳ�Ͽ����ϴ��ļ��� �����ϴ���Ƭ
#���ͬʱ�� ���ļ����ڣ� ������Ӧ��׺���ļ�������jpg, �ѵ�֮���͵���ӡ����ӡ�� ���ɾ����Ƭ��
#Ҳ����˵�ֻ����ʴ���ҳ�ϴ���Ƭ�� ���ԴӺ�̨��ӡ��Ƭ
#Ҳ��������΢�Ŵ�ӡ���Ĺ��ܡ�ͬ��˽ű�Ҳ���Ը���Ϊ΢�Ŵ�ӡword, excel,pdf�ĳ��� �ԼӸ��켴�ɡ�
#�������⣬������ϵ����10054053@qq.com
#Ҳ������github������


#ע�⣬���ű��Ļ�����python2.7��������python3�� �ɹ���Ĭ�ϵĵ�ַ��http://127.0.0.1:8000��������windows,�����ҵ�����win7���ܵġ�

#��Ҫ��װpywin32, ����λ�� https://sourceforge.net/projects/pywin32/





import os
import posixpath
import BaseHTTPServer
import urllib
import cgi
import shutil
import mimetypes
import re
import thread
import os,time,win32print,sys,win32ui
import cv2
import numpy as np
if sys.version_info >= (3,):
    print ('Error, you should run it in python 2.7, not 3.0+')
    input("press any key to continue")

#���ظ���ģ�飬���ű����������ģ�飬 һ����http�ϴ��� һ���������ϴ��ļ�����ӡ�� 

class Printer_:
    def printer(self,img):
        print ('C:/temp/i_view32.exe '+img+' /print')
        os.system('C:/temp/i_view32.exe '+img+' /print')
        print ('end')
    def yicun(self,end):
        for i in os.listdir('C:/Printer/net/WWW/1cun/php/files/'):
            print (i)
            if i.endswith(end) or i.endswith('.JPG'):
                all = np.ones((800, 1350,3), np.uint8)*255
                image=cv2.imread('C:/Printer/net/WWW/1cun/php/files/'+i)
                res=cv2.resize(image,(200,250),interpolation=cv2.INTER_CUBIC)
                all[50:300,100:300]=res
                all[50:300,300:500]=res
                all[50:300,500:700]=res
                all[50:300,700:900]=res
                all[50:300,900:1100]=res
                all[50:300,1100:1300]=res
                all[350:600,100:300]=res
                all[350:600,300:500]=res
                all[350:600,500:700]=res
                all[350:600,700:900]=res
                all[350:600,900:1100]=res
                all[350:600,1100:1300]=res

                #cv2.imshow('iker',res)
                #cv2.imshow('image',image)
                #cv2.imshow('image1',all)
                cv2.imwrite('1cun.jpg',all)
                #cv2.waitKey(0)
                #cv2.destoryAllWindows()
                os.remove('C:/Printer/net/WWW/1cun/php/files/'+i)
    
    def img(self,end):
        print ('start img')
        for i in os.listdir('./'):
            if i.endswith(end) or i.endswith('.JPG'):
                print (i)
                #os.system('print')
                print (i)
                self.printer(i)
                time.sleep(30)
                os.remove(i)
    def __init__(self): #��ʼ����������������׺������Ĭ����jpg
        print ('this is in Printer_')
        while 1>0:
            time.sleep(5)
            self.yicun('.jpg')
            self.img('.jpg')

def test(a1,a2):
    print ('ok')
    Printer_()
##������Ҫ�� �ǽ���һ���������� ���������http�ϴ�webservice��ͬʱ�� �����������ӡ��ģ��
if __name__ == '__main__':
    print ('start')
    Printer_()
    
    #thread.start_new_thread(test,(1,2))
    time.sleep(3) 
