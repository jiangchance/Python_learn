# -*- coding: cp936 -*-
#���ģ��㶮��
'''
�˽ű���������������HSV��ѧ���ԣ�����ɫ���ȵ���Ϣ

#�˽ű���windows����python 2.7+opencv3.2�汾�ģ� ���ü����������
https://github.com/wjb711/Opencv_learning/blob/master/windows_python2.7_opencv3.2%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE%E6%8C%87%E5%AF%BC.txt
#��Ҫ��ǰ��װspeechģ�飬 ��װ����pip install speech
���У���ֵ1��2����Hɫ�ʣ� 3��4����S���ȣ�5��6����V����
����HSV�Ľ��ܣ��뿴����
http://blog.csdn.net/jianjian1992/article/details/51274834
�����Ļ��Ļ�ϵĵ㣬 ���Կ�����Ӧ��X,Y��ֵ��RGB��ֵ�Լ�HSV��ֵ
'''
import cv2
import numpy as np
import sys
def nothing(x):
    pass
def draw_circle(event,x,y,flags,param):
    #if event == cv2.EVENT_LBUTTONDBLCLK:
    if event == cv2.EVENT_LBUTTONDOWN:
        print ('mouse x and y is ')
        print (x,y)
        px = frame[y,x]
        print ('RGB Value:')
        print px
        px_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        H=px_hsv.item(y,x,0)
        S=px_hsv.item(y,x,1)
        V=px_hsv.item(y,x,2)
        print ('HSV Value: H����ɫ��S�Ǵ��ȣ�V������')
        print (H,S,V)


cap = cv2.VideoCapture(0)
try:
        
    ret = cap.set(3,1280)
    ret = cap.set(3,960)

except:
    ret = cap.set(3,640)
    ret = cap.set(3,480)
#������1280x960������ͷ�� ���ʧ�ܣ� ʹ��Ĭ�ϵ�640x480
print ('ʵ�ʷֱ���Ϊ')
print cap.get(3)
print cap.get(4)


cv2.namedWindow('��ɫ��׽',0)
cv2.createTrackbar('ɫ�����', '��ɫ��׽', 0, 180, nothing)
cv2.createTrackbar('ɫ�����', '��ɫ��׽', 180, 180, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 0, 255, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 255, 255, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 0, 255, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 255, 255, nothing)

cv2.setMouseCallback('��ɫ��׽',draw_circle)


while(1):

    # Take each frame
    _, frame = cap.read()
    


    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thrs1 = cv2.getTrackbarPos('ɫ�����', '��ɫ��׽')
    thrs2 = cv2.getTrackbarPos('ɫ�����', '��ɫ��׽')
    thrs3 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    thrs4 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    thrs5 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    thrs6 = cv2.getTrackbarPos('�������', '��ɫ��׽')

    # define range of blue color in HSV
    lower_blue = np.array([thrs1,thrs3,thrs5])
    upper_blue = np.array([thrs2,thrs4,thrs6])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_not(frame,frame, mask= mask)

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('��ɫ��׽',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()


