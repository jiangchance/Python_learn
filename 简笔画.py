# -*- coding: cp936 -*-
#���ģ��㶮��
'''
#��Ů��ϲ����С����Ҳϲ������ʻ�Ϳɫ��
#������ű����Ǹ���д�ģ� �������Ŷ���Ƭ��Ļ��ͼ�� �Ϳ����Ƴɼ�ʻ���
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
#����cv2���moduleģ��
import numpy as np
#����numpy��������õ�ģ��
#import argparse
#�������ģ��
import sys
#import speech
#��������ģ��

def draw_circle(event,x,y,flags,param):
    #global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if mode==True:
                
            print (x,y)
        else:
            print (y,x)
def nothing(x):
    pass
#�Զ���һ��nothing��ģ�飬 �����trackbar�������õ�

import datetime

if __name__ == '__main__':
#����������ű����ã���ִ�����������
    print(__doc__)
    #��ʾǰ����ɫ������������

    try:
        fn = sys.argv[1]
        #���Ի������ĵ�һ�������� Ҳ����ͼƬ������
    except:
        fn = 'images/time.jpg'
        print (fn)
        #����Ҳ�������ָ����ͼƬ���ƣ� Ĭ������Ϊtime.jpg
    mode=1
    #�Զ���һ��ģʽ,��m���л�ԭͼ,Ч��ͼ


#speech.say("���ڿ�ʼ")
#˵���� ����ʼ
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,help="path to the input image")
#��ʾ��Ҫ����ͼƬ����ʾ
#args = vars(ap.parse_args())
#������ǻ��������ͼƬ���Ʋ���ֵ

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
    im = cv2.imread(fn)
#��ȡ�����д����ͼƬ����
    kernel = np.ones((5,5),np.uint8)
#im=cv2.imread('time.jpg',0)
    res = cv2.resize(im,(1280, 960), interpolation = cv2.INTER_CUBIC)
#��ԭͼ�������ʺ���Ļ��1280x960
#cv2.imshow('ԭͼ',im)

    gray=cv2.cvtColor(res,6)
#�Ѳ�ɫͼƬ�ڰ�=�׻ҶȻ�
    res1=cv2.resize(gray,(256, 192), interpolation = cv2.INTER_CUBIC)
#�Ѻڰ׺��ԭͼ��С�ߴ磬 �ŵ���Ļ���Ͻǣ� ��ԭͼ��ʾ��

    cv2.namedWindow('��ʻ�',0)
#����һ�����ֽ�edge���´��ڣ�������ʾ�ӹ����Ч��ͼ�� 0����˼�ǣ� ���ڿ�����
    cv2.createTrackbar('��ֵ', '��ʻ�', 203, 255, nothing)
    cv2.createTrackbar('��ת', '��ʻ�', 2, 2, nothing)
    cv2.createTrackbar('�Ƕ�', '��ʻ�', 0, 360, nothing)
#����һ������thrs1�Ļ�������Ĭ��ֵ��127�� ��0-255�ķ�Χ�ڣ� �ֶ�������ֵ��Χ�� ���������nothingģ�飬��ʵ�൱��ʲô��û�������Ǹ�ʽҪ��ġ�
    while(True):
#ѭ����ΪʲôҪѭ������Ϊ�ֶ�������ֵ��Ч�����ű䣬��ͣ�ص�������ͣ�ı䣬����Ҫѭ��
        thrs1 = cv2.getTrackbarPos('��ֵ', '��ʻ�')
        thrs2 = cv2.getTrackbarPos('��ת', '��ʻ�')
        thrs3 = cv2.getTrackbarPos('�Ƕ�', '��ʻ�')
    #print thrs1
    #��ֵthrs1����edge������thrs1��ֵ
        ret, thresh=cv2.threshold(gray,thrs1,255,cv2.THRESH_BINARY_INV)
    #
    #�ڰײ�ֵ��,��׼ȡ�Ի������ϵķ�ֵ
    #cv2.imshow('thresh',thresh)
    #��ʾ�ڰײ�ֵͼ
        edges = cv2.Canny(thresh,0,255,3)
    #����Ǳ�Եͼ���ڵף�����
        edges_INV =cv2.bitwise_not(edges)
    #ȡ���� �׵ף�����
    #erosion = cv2.erode(edges1,kernel,iterations = 1)
    #dilation = cv2.dilate(edges1,kernel,iterations = 1)
    #cv2.imwrite(sys.argv[1]+'.jpg',edges_INV)
    #д��Դ�ļ��� �滻��ԭͼ
        edges_INV[0:192,0:256]=res1
    #���Ͻ�256x192���ֵ����������С�ĻҶ�ԭͼ
        flipped = cv2.flip(edges_INV,thrs2) #ˮƽ����ֱ���Լ�ˮƽ��ֱ��ת
        M = cv2.getRotationMatrix2D((640,480),thrs3,1)#��ת���ž���(��ת���ģ���ת�Ƕȣ���������)
        rotated = cv2.warpAffine(flipped ,M,(1280,960))#��ԭͼ�� �շ�ָ���� ���ϣ� ���մ�С��

        cv2.imshow('��ʻ�',rotated )

    #��ʾ��ͼ
        cn=cv2.waitKey(5)
        if cn==27:
            break

        if cn==ord('m'):
            print ('m')
            mode = not mode
            print (mode)
            if mode==True:
                edges_INV=res
                cv2.imshow('��ʻ�1',res)
            

        if cn==ord(' '):
            #cv2.imwrite('time1.jpg',edges_INV)
            now = datetime.datetime.now()
            #print ("yes")
            im_name1=(now.strftime('%Y-%m-%d_%H%M%S')+'.jpg')
            cv2.imwrite(im_name1,edges_INV)

    cv2.destroyAllWindows()
#cv2.imshow('erosion',erosion)
#cv2.imshow('dilation',dilation)
#speech.say("ת������")
#������ʾ�� ��ʾ�������
#cv2.waitKey(0)
#��������˳�

