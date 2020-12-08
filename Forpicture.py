import cv2
import dlib

picture = '/home/sunshine/faces/harden1.jpg'
detector = dlib.get_frontal_face_detector()

def add_face_from_image(image):
	imdata = cv2.imread(image)
	rgb_image = cv2.cvtColor(imdata, cv2.COLOR_BGR2RGB)
	faces = detector(rgb_image, 1)
	if len(faces) == 0:
		print("There is no result")
	else:
	     # we now get a likely result
	     pass
