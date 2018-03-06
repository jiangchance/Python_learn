#������Ŀ���ǽ�ȡ��Ļ���ϴ������ݿ⣬ ocrʶ�����ֺ󷢻ؿͻ���
#������İ�װpip install opencv-python Pillow baidu-aip easygui
#���·����ǣ�1��tkinter�������ڣ�������һ����ťbutton, ��ťλ����Ļ���½�
#���°�ť�� ��������������ʾ���ٺ���ʹ��opencv��ȡ���ο�Ҳ������Ҫʶ�����ֵĵط�
#��󣬰�ͼƬ�ϴ����������ϣ���ȡ������ocr���ֺ�ͬ��easygui���ء�
import tkinter,cv2,PIL,numpy
from PIL import Image,ImageDraw,ImageFont,ImageGrab
from aip import AipOcr
import easygui
import os
   



class OCR():
    #mode=0
    #mouse=False
    
    def __init__(self):
        self.window()

    #��������   
    def window(self):
        window=tkinter.Tk()
        #window.title('ת�ı�')
        position_x=window.winfo_screenwidth()-150
        window.geometry('%dx%d+%d+%d' % (100,30,(window.winfo_screenwidth()-100), (window.winfo_screenheight() - 100) ))
        window.resizable(width=False, height=False)

        button0=tkinter.Button(window, text="��ͼת����", command=self.button_command).pack()
        window.mainloop()


    #�����ť�󣬽�������ȫ����ʾ    
    def button_command(self):
        self.mode=0
        self.mouse=False
        print ('start here')
        
        global img,img_copy
        #filename = 'temp.png'
        im = ImageGrab.grab()
        #im.save(filename)
        #im.close()
        #im=pyautogui.screenshot()
        imgSize=im.size
        font = ImageFont.truetype('simhei.ttf', int((imgSize[0])*0.025))
        draw = PIL.ImageDraw.Draw(im)
        draw.text((imgSize[0]*0.7, (imgSize[1]*0.92)), '��ק����ͼ��ȡ����ESC', (255,0,0), font=font)
        
        img=numpy.array(im)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img_copy=img.copy()
            #img =  cv2.imread('1.png')
        cv2.namedWindow("window_full", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window_full",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        
        cv2.setMouseCallback('window_full',self.mouse_action)
        print ('mid here')
        
        while True:
            

            cv2.imshow("window_full", img)

            #print ('mouse_break',self.mouse_break)
            print ('loop here')
            if cv2.waitKey(1)==27 or self.mode==1:
                print ('esc pressed')
                break
            else:
                print ('self.mode,',self.mode)

        cv2.destroyWindow("window_full")
        

    #���������Ȱ����ƶ����������ο�
    def mouse_action(self,event,x,y,flags,param):
        global img_copy
        self.mouse_break=0
        #global mode,x0,y0,x1,y1,mouse_break
        print (event,x,y,flags,param)
        if event==1:
            self.mouse=True
            self.x0,self.y0=x,y
            print ('x0,y0',self.x0,self.y0)
        if flags==1:
            #img=img_copy()
            cv2.rectangle(img, (self.x0, self.y0), (x, y), (0, 0, 0), 1)
            #cv2.imshow("window_full", img)
            
        
        if event==4 and self.mouse==True:
            self.x1,self.y1=x,y
            self.mode=1
            print ('x1,y1',self.x0,self.y0,self.x1,self.y1)
            roi=img_copy[self.y0:self.y1,self.x0:self.x1]
            #cv2.imshow('hello',roi)
            cv2.imwrite('t.png',roi)
            cv2.destroyWindow("window_full")
            #print (roi)
            #cv2.destroyWindow("window_full")
            #self.mouse_break=1
            print ('hello:',self.mouse_break)
            self.baidu_ocr()

    #�ϴ���������OCR������ ������ʶ��������        
    def baidu_ocr(self):
        APP_ID = '10839731';
        API_KEY = '93THkmKKFHGS5inBt8ulCeGH';
        SECRET_KEY = 'EVUeKdmNuCZFyD7xqx0Pr6FLWYyZENvo'
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        image=open('t.png','rb').read()
        t=client.basicGeneral(image);

        """ ����п�ѡ���� """

        options = {}
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["probability"] = "true"
        print (t)
        print (t['words_result'])
        sum0=''
        for i in t['words_result']:
            sum0=sum0+i['words']+'\n'
        print (sum0)
        easygui.msgbox(sum0,title='��ͼת���֣��ɸ��ƣ����ݵ�IT����Ʒ')
        os.remove('t.png')



if __name__=='__main__':
#���������������ʹ��
    os.environ['https_proxy']='http://wanjianb:Beijing123_@web-gate4a.accounts.intern:3128'
    OCR()

