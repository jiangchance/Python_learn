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
im1=cv2.imread('ren.jpg')
#ǰ��ͼƬ
gray1=cv2.cvtColor(im1,6)
#�Ҷȴ���
ret,thresh1=cv2.threshold(gray1,127,255,cv2.THRESH_BINARY)
#��ֵ��
thresh1a=cv2.cvtColor(thresh1,cv2.COLOR_GRAY2BGR)
#ת��ͨ��
thresh1_INV=cv2.bitwise_not(thresh1)
#��ֵȡ��
thresh1_INVa=cv2.cvtColor(thresh1_INV,cv2.COLOR_GRAY2BGR)
#ת��ͨ��
im2=cv2.imread('lufugong.jpg')
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
cv2.imshow('im_all',im_all)
cv2.waitKey(0)

