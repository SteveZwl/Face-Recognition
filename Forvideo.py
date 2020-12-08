import cv2
import dlib
from pathlib import Path
video = cv2.VideoCapture(0)
save_path = '/home/fantasy/faces'

def read_camera0():
    """
    Open camera
    """

    while 1:
        ok, frame = video.read()
        if not ok:
            print("success or failed")
            return
        else:
            yield frame

    video.release()

def putText(image, text, location=(100, 150), font=cv2.FONT_HERSHEY_COMPLEX, size=1.1, color=(0, 255, 255), font_weight=2):
    """
   
    param: image 
    param: text  
    param: location 
    param: font 
    param: size: 
    param: color: 
    param: font_weight 
    """
    cv2.putText(image, text, location, font, size, color, font_weight, lineType=cv2.LINE_AA)

def add_face_from_camera():
	frames = cv_tools.read_camera0()
    count = 0
    for frame in frames:
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        title = 'Register'
        press = cv2.waitKey(2)
        data = detector(image_rgb)
        if len(data) == 0:
            putText(frame, "No face was detected!", color=(0, 0, 255))
        if press == ord('q'):
            break
        if press == ord('a'):
            if len(data) == 0:
                putText(frame, "No face was detected!", color=(0, 0, 255))
            else:
                count += 1
                impath = Path(save_path).joinpath('%s.jpg' % count)
                print("保存照片 %s" % impath)
                cv2.imwrite(str(impath), frame)
        cv_tools.putText(frame, 'a:Add', location=(40, 300))
        cv_tools.putText(frame, 'q:Quit', location=(40, 350))
        cv_tools.putText(frame, 'save count:%s' % count, location=(40, 400), size=1.0)
        cv2.imshow(title, frame)
    cv2.destroyAllWindows()
