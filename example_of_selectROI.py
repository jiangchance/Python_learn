# -*- coding: cp936 -*-
#���ģ��㶮��
'''
selectROI��contribģ���е�һ�����ݣ� ���������opencv
������ΰ�װ����contribģ�飬 ��μ��ҵİ�װ����ָ��
'''
import cv2
#import numpy as np
cap=cv2.VideoCapture(0)
#ret=cap.set(3,1280)
#ret=cap.set(4,720)
cv2.namedWindow('frame',0)

while cv2.waitKey(1)!=27:
    ret, frame=cap.read()
    
    #���ո����ͼ����ͼ�󻭿��ͼ
    if cv2.waitKey(1)==ord(' '):
        (x1,y1,x2,y2)=cv2.selectROI('frame',frame,0,0)
        #selectROI���4��ֵ�������϶��ǵģ�x��yֵ�� �Լ�֮���w, hֵ�� ��ע����float��Ҫת��Ϊint
        x1=int(x1)
        x2=int(x2)
        y1=int(y1)
        y2=int(y2)
        src=frame[y1:y1+y2,x1:x1+x2]
        #���س���ո�����ѽس�����ͼ�Ŵ����640x480����Ļ
        im=cv2.resize(src, (640, 480), interpolation = cv2.INTER_CUBIC)
        cv2.imshow('im',im)
        cv2.waitKey(1000)
    cv2.imshow('frame',frame)
cap.release()
cv2.destroyAllWindows()
