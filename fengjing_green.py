# -*- coding: cp936 -*-
#���ģ��㶮��
#!/usr/bin/python
'''
���ڼ��У� �������磬 ��������ط羰��ʤ��Ӱ
�÷�����
#�÷�python pan_painting.py  ���ͼƬ ���� python pan_painting.py  time.jpg
#�˽ű���windows����python 2.7+opencv3.2�汾�ģ� ���ü����������
https://github.com/wjb711/Opencv_learning/blob/master/windows_python2.7_opencv3.2%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE%E6%8C%87%E5%AF%BC.txt
#��Ҫ��ǰ��װspeechģ�飬 ��װ����pip install speech
����ʾ���´���
no module named win32com.client������
�����ض�Ӧpywin32���
https://sourceforge.net/projects/pywin32/files/pywin32/
����������΢��tts
http://www.microsoft.com/en-us/download/confirmation.aspx?id=27224
'''


import cv2
import numpy as np
import time
import sys
#import win32com
#import speech

#��������ģ��
def nothing(x):
    pass


print(__doc__)
#��ʾǰ����ɫ������������
print ('��ǰopencv�汾Ϊ'+cv2.__version__)
#��ʾopencv�汾
print ('���python�汾��ϢΪ')
print (sys.version_info)
#speech.say("�Ƽ�ʹ��720p��1080p��������ͷ")

cv2.namedWindow('mix',0)

cap=cv2.VideoCapture(0)
try:
        
    ret = cap.set(3,1280)
    ret = cap.set(3,960)
    y1=1280
    x1=960

except:
    ret = cap.set(3,640)
    ret = cap.set(3,480)
    y1=640
    x1=480
try:
    fn = sys.argv[1]
    #���Ի������ĵ�һ�������� Ҳ����ͼƬ������
except:
    fn = 'images/lufugong.jpg'
    print fn
    #����Ҳ�������ָ����ͼƬ���ƣ� Ĭ������Ϊlufugong.jpg
#������1280x960������ͷ�� ���ʧ�ܣ� ʹ��Ĭ�ϵ�640x480
print ('ʵ�ʷֱ���Ϊ')
print cap.get(3)
print cap.get(4)
#ret = cap.set(3,1280)
#ret = cap.set(4,720)
c=1
d=0
im = cv2.imread(fn)

im_white= cv2.imread('images/white.jpg')
im = cv2.imread(fn)
cv2.namedWindow('��ɫ��׽',0)
cv2.createTrackbar('��ֵ���', '��ɫ��׽', 0, 255, nothing)
cv2.createTrackbar('��ֵ���', '��ɫ��׽', 255, 255, nothing)
#cv2.createTrackbar('�������', '��ɫ��׽', 0, 255, nothing)
#cv2.createTrackbar('�������', '��ɫ��׽', 255, 255, nothing)
#cv2.createTrackbar('�������', '��ɫ��׽', 0, 255, nothing)
#cv2.createTrackbar('�������', '��ɫ��׽', 255, 255, nothing)

while (True):

    ret,im1=cap.read()
        
    #cv2.imshow('ԭͼ',frame)
    #ԭͼ
    #gray = cv2.cvtColor(frame, 6)
    #cv2.imshow('ԭͼ�Ҷ�',gray)
    #�Ҷ�ͼ
    # Convert BGR to HSV
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thrs1 = cv2.getTrackbarPos('��ֵ���', '��ɫ��׽')
    thrs2 = cv2.getTrackbarPos('��ֵ���', '��ɫ��׽')
    #thrs3 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    #thrs4 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    #thrs5 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    #thrs6 = cv2.getTrackbarPos('�������', '��ɫ��׽')

#im1=cv2.imread('ren.jpg')
    cv2.imshow('1',im1)
#ǰ��ͼƬ
    b,g,r = cv2.split(im1)
    #gray1=cv2.cvtColor(im1,6)
#�Ҷȴ���
    ret,thresh1=cv2.threshold(g,thrs1,thrs2,cv2.THRESH_BINARY)
    cv2.imshow('thresh1',thresh1)
#��ֵ��
    thresh1a=cv2.cvtColor(thresh1,cv2.COLOR_GRAY2BGR)
#ת��ͨ��
    thresh1_INV=cv2.bitwise_not(thresh1)
#��ֵȡ��
    thresh1_INVa=cv2.cvtColor(thresh1_INV,cv2.COLOR_GRAY2BGR)
#ת��ͨ��
    im2=cv2.imread(fn)
#����ͼ


    im_FG=cv2.add(im1,thresh1a)
#ǰ��ͼ������ٳ���

    im_BG=cv2.add(im2,thresh1_INVa)
#����ͼ��������Ӱȥ��
    im_all=cv2.bitwise_and(im_FG,im_BG)
#�ϲ�����ͱ���
#cv2.imshow('s1',im1)
#cv2.imshow('s2',im2)
#cv2.imshow('im3',im3)
#cv2.imshow('im_BG',im_BG)
#cv2.imshow('im_FG',im_FG)
    cv2.imshow('��ɫ��׽',im_all)
    cv2.waitKey(50)

############################################################
    

