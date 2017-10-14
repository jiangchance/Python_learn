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
����ʾ���´���:
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
import datetime
from common import Sketcher
from color_transfer import color_transfer
#import win32com
#import speech

#��������ģ��
def nothing(x):
    pass
def draw_circle(event,x,y,flags,param):
    #if event == cv2.EVENT_LBUTTONDBLCLK:
    if event == cv2.EVENT_LBUTTONDOWN:
        print ('mouse x and y is ')
        print (x,y)
        px = im1[y,x]
        print ('RGB Value:')
        print px
        px_hsv = cv2.cvtColor(im1, cv2.COLOR_BGR2HSV)
        H=px_hsv.item(y,x,0)
        S=px_hsv.item(y,x,1)
        V=px_hsv.item(y,x,2)
        print ('HSV Value: H����ɫ��S�Ǵ��ȣ�V������')
        print (H,S,V)


print(__doc__)
#��ʾǰ����ɫ������������
print ('��ǰopencv�汾Ϊ'+cv2.__version__)
#��ʾopencv�汾
print ('���python�汾��ϢΪ')
print (sys.version_info)
#speech.say("�Ƽ�ʹ��720p��1080p��������ͷ")

#cv2.namedWindow('mix',0)
#print sys.argv[0],sys.argv[1]

cap=cv2.VideoCapture(0)
ret = cap.set(3,960)
ret = cap.set(4,720)
try:
    fn = sys.argv[1]
    
    #���Ի������ĵ�һ�������� Ҳ����ͼƬ������
except:
    fn = 'images/lufugong.jpg'
#fn = cv2.resize(fn,(640, 480), interpolation = cv2.INTER_CUBIC)
print ('��һ��������')
#print   sys.argv[1]   
print fn
    #����Ҳ�������ָ����ͼƬ���ƣ� Ĭ������Ϊlufugong.jpg
#������1280x960������ͷ�� ���ʧ�ܣ� ʹ��Ĭ�ϵ�640x480

print ('start here')
print ('ʵ�ʷֱ���Ϊ')
y1=cap.get(3)
x1=cap.get(4)
print y1,x1
#ret = cap.set(3,1280)
#ret = cap.set(4,720)
c=1
d=0

#im = cv2.imread(fn)

#im_white= cv2.imread('images/white.jpg')
im = cv2.imread(fn)
if x1==480.0:
    print ('480')
    im = cv2.resize(im,(640, 480), interpolation = cv2.INTER_CUBIC)
else:
    im = cv2.resize(im,(960, 720), interpolation = cv2.INTER_CUBIC)
cv2.namedWindow('��ɫ��׽')
cv2.namedWindow('123',0)

cv2.setMouseCallback('��ɫ��׽',draw_circle)
cv2.createTrackbar('ɫ�����', '��ɫ��׽', 74, 255, nothing)
cv2.createTrackbar('ɫ�����', '��ɫ��׽', 122, 255, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 9, 255, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 56, 255, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 133, 255, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 255, 255, nothing)
cv2.createTrackbar('ģ����', '��ɫ��׽', 4, 100, nothing)


while (True):

    ret,im1=cap.read()
        
    #cv2.imshow('ԭͼ',frame)
    #ԭͼ
    #gray = cv2.cvtColor(frame, 6)
    #cv2.imshow('ԭͼ�Ҷ�',gray)
    #�Ҷ�ͼ
    # Convert BGR to HSV
    hsv = cv2.cvtColor(im1, cv2.COLOR_BGR2HSV)

    thrs1 = cv2.getTrackbarPos('ɫ�����', '��ɫ��׽')
    thrs2 = cv2.getTrackbarPos('ɫ�����', '��ɫ��׽')
    thrs3 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    thrs4 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    thrs5 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    thrs6 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    thrs7 = cv2.getTrackbarPos('ģ����', '��ɫ��׽')
    thrs7=thrs7+1
    #print mode
    #print thrs1

#im1=cv2.imread('ren.jpg')
    #cv2.imshow('1',im1)
#ǰ��ͼƬ
    #gray1=cv2.cvtColor(im1,6)
#�Ҷȴ���
    lower_blue = np.array([thrs1,thrs3,thrs5])
    upper_blue = np.array([thrs2,thrs4,thrs6])

    # Threshold the HSV image to get only blue colors
    thresh1 = cv2.inRange(hsv, lower_blue, upper_blue)
    blur = cv2.blur(thresh1,(thrs7,thrs7),0)
    ret3,thresh1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    kernel = np.ones((5,5),np.uint8)
    #thresh1 = cv2.erosion(thresh1,kernel,iterations = 1)

    #thresh1_INV=cv2.bitwise_not(mask)

    #ret,thresh1=cv2.threshold(gray1,thrs1,thrs2,cv2.THRESH_BINARY)
    #cv2.imshow('thresh1',thresh1)
#��ֵ��
    thresh1a=cv2.cvtColor(thresh1,cv2.COLOR_GRAY2BGR)
#ת��ͨ��
    thresh1_INV=cv2.bitwise_not(thresh1)
#��ֵȡ��
    thresh1_INVa=cv2.cvtColor(thresh1_INV,cv2.COLOR_GRAY2BGR)
#ת��ͨ��
    im2=cv2.imread(fn)
    im2=im
#����ͼ

    im1_FG=color_transfer(im2,im1)
    #�ѱ���ͼ��ɫ
    im_FG=cv2.add(im1_FG,thresh1a)
    #cv2.imshow('1',im_FG)
    #im_FG=color_transfer(im2,im_FG)
    #cv2.imshow('2',im_FG)
#ǰ��ͼ������ٳ���

    im_BG=cv2.add(im2,thresh1_INVa)
#����ͼ��������Ӱȥ��
    im_all=cv2.bitwise_and(im_FG,im_BG)
    #center = (0, 0)
    #mixed_clone = cv2.seamlessClone(im_FG, im2, thresh1, center, cv2.MIXED_CLONE)
#�ϲ�����ͱ���
#cv2.imshow('s1',im1)
#cv2.imshow('s2',im2)
#cv2.imshow('im3',im3)
#cv2.imshow('im_BG',im_BG)
#cv2.imshow('im_FG',im_FG)
    cv2.imshow('��ɫ��׽',im_all)
    cv2.imshow('123',im_all)
    #cv2.imshow('456',mixed_clone)
    cn=cv2.waitKey(50)
    if cn==ord(' '):
        d=c+1
    if c==d:
        print ('0')
        cn=cv2.waitKey(30)
        now = datetime.datetime.now()
            #print ("yes")
        im_name1=(now.strftime('%Y-%m-%d_%H%M%S')+'.jpg')
        img_mark = im_all.copy()
        mark = np.zeros(im_all.shape[:2], np.uint8)
        sketch = Sketcher('�ɱ༭', [img_mark, mark], lambda : ((255, 255, 255), 255))
        while(cn!=27):
            cn=cv2.waitKey(10)

            
            res = cv2.inpaint(img_mark, mark, 3, cv2.INPAINT_TELEA)
            cv2.imshow('�ɱ༭',res)
            print cn
            print 'yes'
        #
        
        cv2.imwrite('images/'+im_name1,res)
        cv2.imshow('�ɱ༭',res)
        cv2.waitKey(2000)
        cv2.destroyWindow('�ɱ༭')
        print ('done')
    c=c+1
        

############################################################
    

