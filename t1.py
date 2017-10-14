# -*- coding: cp936 -*-

'''
    OpenCV Colormap  Example
    
    Copyright 2015 by Satya Mallick <spmallick@learnopencv.com>
    
'''


import cv2
import numpy as np
def nothing(x):
    pass
cv2.namedWindow('��Ƶɫ��',0)
cv2.createTrackbar('ɫ��ѡ��', '��Ƶɫ��', 9, 11, nothing)

cap=cv2.VideoCapture(0)
while(1):
    ret,im=cap.read()
    #im=cv2.imread('3.jpg')
    
    im1 = cv2.detailEnhance(im, sigma_s=10, sigma_r=0.15)
    img_sobel_y = cv2.Sobel(im1, cv2.CV_64F, 0, 1, ksize=3)
    #gray=cv2.cvtColor(img_sobel_y,6)
    #img_canny = cv2.Canny(gray, 100, 200)  
    thrs1 = cv2.getTrackbarPos('ɫ��ѡ��', '��Ƶɫ��')
    print thrs1
    im_color0 = cv2.applyColorMap(im1, thrs1)
    cv2.imshow("��Ƶɫ��", im_color0)
    cv2.imshow("im", im)
    cv2.imshow("img_sobel_y ", img_sobel_y)
    #cv2.imshow("img_canny", gray)
    cv2.waitKey(30);
