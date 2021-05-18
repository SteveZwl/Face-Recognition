import cv2
import os
from PIL import Image


#加载训练数据集文件
recogizer=cv2.face.LBPHFaceRecognizer_create()
recogizer.read('trainer/trainer.yml')
#准备识别的图片
img=cv2.imread('11.pgm')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_detector = cv2.CascadeClassifier(
    'C:\\Users\WenlongZhang\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
faces = face_detector.detectMultiScale(gray)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #人脸识别
    id,confidence=recogizer.predict(gray[y:y+h,x:x+w])
    print('label id:',id,'credit score：',confidence)

def read_img():
  # os.path.join("./data/jm",id+".pgm")  # 连接两个目录
    im = Image.open(os.path.join("./data/jm",".pgm",'id'))  # 读取文件
    im.show()    # 展示图片
    print(im.size)   # 输出图片大小

if __name__ == "__main__":
    read_img()     # 调用read_img()

cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()