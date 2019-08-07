import os
import getColor
from os.path import join as pjoin
from scipy import misc

def load_color(color_dir,list):
    count = 0
    for dir in os.listdir(color_dir):
        img_dir = pjoin(color_dir,dir)
        image = getColor.Image.open(img_dir)
        image = image.convert('RGB')
        get = getColor.get_dominant_color(image)
        list.append(get)
        count = count + 1
    # print(count)
    return count

def Mean_color(count,list):
    Mean_R=Mean_G=Mean_B=0
    for i in range(count):
        tuple=list[i]
        Mean_R+=tuple[0]
        Mean_G+=tuple[1]
        Mean_B+=tuple[2]
    MeanC=((int)(Mean_R/count),(int)(Mean_G/count),(int)(Mean_B)/count)
    return MeanC
