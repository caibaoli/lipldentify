
#coding=utf8
import cv2
import time
print('Press Esc to exit')
imgWindow = cv2.namedWindow('FaceDetect', cv2.WINDOW_NORMAL)
import sys
import os
import dlib
import glob
import numpy
from skimage import io
def detect_face():
    capInput = cv2.VideoCapture(0)
    #nextCaptureTime = time.time()
    faces = []
    feas = []
    if not capInput.isOpened(): print('Capture failed because of camera')
    while 1:
        ret, img = capInput.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        time=0
        eTime = time.time() + 0.1
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
        dets = detector(gray, 1)
        print("Number of faces detected: {}".format(len(dets)))
        for a in dets:
           cv2.rectangle(img,(a.left(),a.top()),(a.right(),a.bottom()),(255,0,0))
        for index, face in enumerate(dets):
           print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(), face.bottom()))
           shape = predictor(gray, face)
           for i, pt in enumerate(shape.parts()):
            #print('Part {}: {}'.format(i, pt))
             pt_pos = (pt.x, pt.y)
             cv2.circle(img, pt_pos, 2, (255, 0, 0), 1)
        cv2.imshow('FaceDetect',img)
        if cv2.waitKey(1) & 0xFF == 27: break
    capInput.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    detect_face()