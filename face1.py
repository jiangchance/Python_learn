# -*- coding: cp936 -*-

#���ģ��㶮��

# import the necessary packages

from imutils import face_utils

import numpy as np

import dlib

import cv2

#�������ɵ�ģ��

detector = dlib.get_frontal_face_detector()

#detector����������������� ��������

predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
#   You can get the shape_predictor_68_face_landmarks.dat file from:
#   http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

#����������ϸ�ڣ��۾���ͣ�üë�ȡ�

image=cv2.imread('2008.jpg')

#��ȡͼƬ

gray=cv2.cvtColor(image,6)

#ת�Ҷ�

rects = detector(gray, 1)

#��ʼ��ͼȡ������

#print (rects)

for (i, rect) in enumerate(rects):

#i������������ rects�Ǽ��ϣ� rect�ǵ��������ķ���

    #print (i,rect)

    shape = predictor(gray, rect)

    #ÿ������ȡϸ��

    #print (shape)

    shape = face_utils.shape_to_np(shape)

    #ת��Ϊopencv��xy����ֵ����68��

    #print (shape)

    for (x, y) in shape:

        cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

        #�ú�ʻ��㣬ÿ������68����

cv2.imshow("Output", image)

#���ͼ��

cv2.waitKey(0)
