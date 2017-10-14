# -*- coding: cp936 -*-
import cv2
import numpy as np
import time
import sys
import datetime
def nothing(x):
    pass

cap=cv2.VideoCapture(0)
im1=cv2.imread('1.jpg')
im2=cv2.imread('2.jpg')
#cv2.namedWindow('mix',0)
cv2.namedWindow('��ɫ��׽',0)
cv2.createTrackbar('ɫ�����', '��ɫ��׽', 0, 255, nothing)
cv2.createTrackbar('ɫ�����', '��ɫ��׽', 139, 255, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 0, 255, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 61, 255, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 120, 255, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 248, 255, nothing)
while(True):
    ret,img=cap.read()


    
    cn=cv2.waitKey(5)
    if cn==ord("1"):
        im1=img
    if cn==ord("2"):
        im2=img
    diff = cv2.absdiff(im1, img)
    subtracted=cv2.bitwise_xor(img,im1)
    blur = cv2.GaussianBlur(diff,(5,5),0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    thrs1 = cv2.getTrackbarPos('ɫ�����', '��ɫ��׽')
    thrs2 = cv2.getTrackbarPos('ɫ�����', '��ɫ��׽')
    thrs3 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    thrs4 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    thrs5 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    thrs6 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    lower_blue = np.array([thrs1,thrs3,thrs5])
    upper_blue = np.array([thrs2,thrs4,thrs6])

    # Threshold the HSV image to get only blue colors
    thresh1 = cv2.inRange(hsv, lower_blue, upper_blue)
    thresh1a=cv2.cvtColor(thresh1,cv2.COLOR_GRAY2BGR)
#ת��ͨ��
    thresh1_INV=cv2.bitwise_not(thresh1)
#��ֵȡ��
    thresh1_INVa=cv2.cvtColor(thresh1_INV,cv2.COLOR_GRAY2BGR)
    #gray=cv2.cvtColor(diff,6)
    #blur = cv2.GaussianBlur(gray,(5,5),0)
    #ret2,th2 = cv2.threshold(blur,thrs1,thrs2,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #ret2,th2 = cv2.threshold(blur,thrs1,thrs2,cv2.THRESH_BINARY)
    #cv2.imshow('1',im1)
    #cv2.imshow('2',im2)
    #cv2.imshow('gray',gray)
    #cv2.imshow('gray',gray)
    #cv2.imshow('blur',blur)
    cv2.imshow('diff',diff)
    cv2.imshow('subtracted',subtracted)
    cv2.imshow('��ɫ��׽',thresh1)
    cv2.imshow('1',thresh1)
    cv2.imshow('2',thresh1_INV)
    
