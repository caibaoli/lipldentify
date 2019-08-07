import numpy as np
import cv2
import dlib
from PIL import Image


def crop(source, pos):
    x1 = pos[2][0]
    y1 = pos[2][1]
    x2 = pos[1][0]
    y2 = pos[1][1]
    d = abs(x2 - x1)
    region = source[(int)(y1 - d * 0.75):y2, x1:x2]
    # save the image
    cv2.imwrite("output/Mouth1.jpg", region)

    x1 = pos[1][0]
    y1 = pos[1][1]
    x2 = pos[0][0]
    y2 = pos[0][1]
    d = abs(x1 - x2)
    region = source[y1 - d:y2, x1:x2]
    # save the image
    cv2.imwrite("output/Mouth2.jpg", region)


def detect_mouth(img, pos):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    detector = dlib.get_frontal_face_detector()
    # use the predictor　
    predictor = dlib.shape_predictor('color_json/shape_predictor_68_face_landmarks.dat')
    dets = detector(img, 1)
    print("Number of faces detected: {}".format(len(dets)))
    for a in dets:
        cv2.rectangle(img, (a.left(), a.top()), (a.right(), a.bottom()), (255, 0, 0))
    # point_list=[]#save the mouth point to point_list[]#
    # Extract 68 feature points of the face and crop the lip image#
    for index, face in enumerate(dets):
        print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(),
                                                                     face.bottom()))
        shape = predictor(gray, face)
        for i, pt in enumerate(shape.parts()):
            # print('Part {}: {}'.format(i, pt))
            # print(i)
            pt_pos = (pt.x, pt.y)
            if i >= 48 and i <= 67:
                cv2.circle(img, pt_pos, 2, (255, 0, 0), 1)
            if i >= 56 and i <= 58:
                # print(pt_pos)
                pos[i - 56][0] = pt.x
                pos[i - 56][1] = pt.y
            # cv2.circle(img, pt_pos, 2, (255, 0, 0), 1)
    return img


if __name__ == "__main__":
    img = cv2.imread("images/face.jpg")
    # copy the input image for the later crop#
    img_clone = np.copy(img)
    cv2.imwrite("input/source.jpg", img_clone)
    # save the lip position to pos array#
    pos = np.zeros((3, 2), dtype=int)
    result = detect_mouth(img, pos)
    cv2.imwrite("input/source2.jpg", result)
    # crop the lip areas#
    source = cv2.imread("input/source2.jpg")
    crop(source, pos)
    # show the result
    cv2.imshow('FaceDetect', result)
    cv2.waitKey(0)
    cv2.destroyAllWindow