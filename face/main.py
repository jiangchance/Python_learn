# -*- coding: cp936 -*-

#���ģ��㶮��
import cv2
import datetime
import easygui
from easygui import msgbox, multenterbox

#�������ģ��
def pressESC(img,rect):
#�Զ��尴��esc���������¼����˴�������easybox
    cv2.imwrite('pic.jpg',img)
    image = 'pic.jpg'
        
    msg = "�Ƿ���뵽����ʶ�����?"
    choices = ["Yes","No","�˳�����"]
    reply = easygui.buttonbox(msg, image=image, choices=choices)
    if reply=="Yes" or reply=='pic.jpg':
        print (reply)
        if len(rect)==1:
        
            flavor = easygui.enterbox("���������֣�������Ӣ�ģ�ƴ�����������пո��������ţ�") 
            easygui.msgbox ("�������ˣ� " + flavor)
            folder='raw'
            name=folder+"/"+flavor+'.jpg'
            #easygui.msgbox (name)
            cv2.imwrite(name,img)
            for x1, y1, x2, y2 in rects:
            
            #cv2.rectangle(copy0, (x1, int(y1*0.7)), (x1+x2, y1+int(y2*1.3)), (127, 255, 0), 2)
                roi=img[int(y1*0.7):y1+int(y2*1.3), x1:x1+x2]
                folder1='faces'
                name1=folder1+"/"+flavor+'.jpg'
                cv2.imwrite(name1,roi)
            #print (roi)
        else:
            easygui.msgbox ('û��������ֹһ��������ȷ����������')

    elif reply=="No" or reply==None:
        print (reply)
        pass
    #elif reply=='pic.jpg':
    #    flavor = easygui.enterbox("���������֣�������Ӣ�ģ�ƴ�����������пո��������ţ�") 
    #    easygui.msgbox ("�������ˣ� " + flavor)
    else:
        print ('reply is ',reply)
        cap.release()
        cv2.destroyAllWindows()
        
if __name__ == "__main__":
#������

    logo='GD'
    #���Ͻǵ�ͼ��
    promotion='press ESC'
    #���½ǵ���ʾ

    cap=cv2.VideoCapture(0)
    cv2.namedWindow('output',0)
    print ('hello')
    #faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faceCascade = cv2.CascadeClassifier('cars.xml')
    #�������ֵ�xml·���� �����Ƿ�����û�������� ʶ����ʶ������������һ����
    print ('hello1')
    while cv2.waitKey(1)!=ord('q'):
        time=datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
        #����ʱ����ʾ�����Ͻ�
        _,frame=cap.read()
        
        copy0=frame.copy()
        


        rects = faceCascade.detectMultiScale(copy0, 1.3, 4, cv2.CASCADE_SCALE_IMAGE, (20,20))
        #print (len(rects))
  
        for x1, y1, x2, y2 in rects:
            
            cv2.rectangle(copy0, (x1, int(y1*0.7)), (x1+x2, y1+int(y2*1.3)), (127, 255, 0), 2)
            #roi=copy0[int(y1*0.7):y1+int(y2*1.3), x1:x1+x2]
            #cv2.imshow('roi',roi)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(copy0, logo, (600, 10), font, 0.5, (0, 0, 0), 1)
        cv2.putText(copy0, time, (0, 10), font, 0.5, (255, 255, 255), 1)
        cv2.putText(copy0, promotion, (0, 470), font, 0.5, (0, 0, 255), 1)
        cv2.imshow('output',copy0)
        if cv2.waitKey(1)==27:
            try:
                pressESC(copy0,rects)
    
    #���Ի������ĵ�һ�������� Ҳ����ͼƬ������
            except:
                pass
            


    cap.release()
    cv2.destroyAllWindows()
    
