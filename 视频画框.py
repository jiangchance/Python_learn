# -*- coding: cp936 -*-
import cv2
import numpy as np
def nothing(x):
    pass
cap=cv2.VideoCapture(0)
cv2.namedWindow('�����',0)
#����һ�����ֽ�edge���´��ڣ�������ʾ�ӹ����Ч��ͼ�� 0����˼�ǣ� ���ڿ�����
cv2.createTrackbar('ģ����', '�����', 1, 255, nothing)
cv2.createTrackbar('��ֵ', '�����', 1, 255, nothing)
while(1):
  ret,img=cap.read()
  cv2.imshow("raw", img)
  gray=cv2.cvtColor(img,6)
  
  thrs1 = cv2.getTrackbarPos('ģ����', '�����')
  thrs2 = cv2.getTrackbarPos('��ֵ', '�����')
  thrs1=thrs1+1
  blur=cv2.blur(gray,(thrs1,thrs1))

#img = cv2.pyrDown(cv2.imread("hammer.jpg", cv2.IMREAD_UNCHANGED))
#cv2.imshow("raw", img)
#cv2.imshow('0',cv2.imread("hammer.jpg"))

  ret, thresh = cv2.threshold(blur, thrs2, 255, cv2.THRESH_BINARY)
  image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#������������

  for c in contours: 
  # find bounding box coordinates,��c����������ʱ��
    x,y,w,h = cv2.boundingRect(c) #x,y w,h�ֱ����������꣬ ����Լ��߶�
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2) #����ɫ�����

  # find minimum area
    rect = cv2.minAreaRect(c)
    #������С������
  # calculate coordinates of the minimum area rectangle
    box = cv2.boxPoints(rect)
  # normalize coordinates to integers
    box = np.int0(box)
    # draw contours
    cv2.drawContours(img, [box], 0, (0,0, 255), 3)
  
    # calculate center and radius of minimum enclosing circle
    (x,y),radius = cv2.minEnclosingCircle(c)
    #������СԲ�Σ�����Բ
    # cast to integers
    center = (int(x),int(y))
    radius = int(radius)
    # draw the circle
    img = cv2.circle(img,center,radius,(0,255,0),2)

  cv2.drawContours(img, contours, -1, (255, 255, 255), 1)
  cv2.imshow("contours", img)
  cv2.imshow('�����',thresh)

  cv2.waitKey(30)
  #cv2.destroyAllWindows()
