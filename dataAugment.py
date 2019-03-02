"""
you can flip your images and your bounding box 
"""
import fire
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import re

def image_flip(imageDir_path="", trainLabel_path="", outputpath="") :
    """
    flip image left to right, and flip the bounding box either.
    output pic end with "-flipped"
    Args: 
        imageDir_path: the path of the train pic dir
        trainLabel_path: the path of the train label path
        outputpath: the path of the flipped pic and train label

    """
    bounding_boxs = get_bounding_box(trainLabel_path)
    image_data = read_images(imageDir_path)
    ids = get_ids(imageDir_path)

    newImages = {}
    new_pd_data = []

    for id in ids:
        width = image_data[id].shape[1]
        newImages[id+"flipped"] = np.flipud(image_data[id])
        for bounding in bounding_boxs[id]:
            if (id+"flipped") not in newBounding_boxes:
                newBounding_boxes[id+"flipped"] = []
            num = str(width - int(bounding.split()[0]))
            num1 = str(bounding.split()[1])
            num2 = str(width - int(bounding.split()[2]))
            num3 - str(bounding.split()[3])
            new_pd_data.append({"ID":id, "Detection" : " ".join((num, num1, num2, num3))})

    output_csv_path = outputpath + "flipped_label.csv"
    new_pd_data.to_csv(output_csv_path) 

    for id in ids:
        name = re.split(r".jpg|.png|.jpeg ", id)[0]
        print(outputpath + name + "-flipped.jpg")
        cv2.imwrite(newImages[id+"flipped"], outputpath+name+"-flipped.jpg")



def image_udflip(imageDir_path="", trainLabel_path="", outputpath="") :
    """
    flip image up to down and flip the bounding box either
    output pic end with "-updown"

    Args: 
        imageDir_path: the path of the train pic dir
        trainLabel_path: the path of the train label path
        outputpath: the path of the flipped pic and train label
    """


def image_roate(imageDir_path = "", trainLabel_path = "", outputpath="", roate=90):
    """
    roate the image clockwise 
    output pic end with "-roated"
    Args:
        imageDir_path: the path of the train pic dir
        trainLabel_path: the path of the train label path
        outputpath: the path of the flipped pic and train label
        roate: the degree pic will roate
    """

def image_saltNoise(imageDir_path = "", trainLabel_path = "", outputpath = ""):
    """
    Add salt noise to the pic
    output pic end with "-salt"
    Args:
        imageDir_path: the path of the train pic dir
        trainLabel_path: the path of the train label path
        outputpath: the path of the flipped pic and train label
    """


def image_GaussianNoise(imageDir_path = "", trainLabel_path = "", outputpath = ""):
    """
    Add salt obeyed the gaussian distribution to the pic
    output pic end with "-gauss"
    Args:
        imageDir_path: the path of the train pic dir
        trainLabel_path: the path of the train label path
        outputpath: the path of the flipped pic and train label
    """

def image_moveUp(imageDir_path = "", trainLabel_path = "", outputpath = "", distance = 0):
    """
    move up ur pic with the distance
    """

def image_moveDown(imageDir_path = "", trainLabel_path ="", outputpath= "", distance = 0):
    """
    move down ur pic with distance 
    """

def image_moveLeft(imageDir_path = "", trainLabel_path = "", outputpath = "", distance = 0):
    """
    move left ur pic with distance
    """

def image_moveRight(imageDir_path = "", trainLabel_path = "", outputpath ="", distance = 0):
    """
    move right ur pic with distance
    """


def read_images(imageDir_path):
    """
    read images data of the image dir
    return a dict which the key is the pic name 
    and the value the pic data
    """
    image_names = get_ids(imageDir_path)
    image_data = {}
    for image in image_names:
        if image not in image_data:
            image_data[image] = np.array(cv2.imread(image))
    
    return image_data

def get_bounding_box(trainLabel_path):
    """
    I supposed the trainlabel is the csv file and 
    the data is read as follows

    ID, Detection

    Detection's value is a four element pair (x1, y1, x2, y2) 
    for example 11, 153, 69, 572
    
    return a dict which the key is the image name and 
    value is the list containing the bounding box
    """

    label_data = pd.read_csv(trainLabel_path)
    ids = label_data["ID"]
    label_box = {}
    for id in ids:
        if id not in label_box:
            label_box[id] = []
        for value in label_data.loc[data["ID"] == id]["Detection"]:
            label_box[id].append(value)

    return label_box

def get_ids (imageDir_path):
    image_names = []
    for root, dir, files in os.walk(imageDir_path):
        for file in files:
            image_name.append(file)

    return image_names

if __name__ == "__main__":
    fire.Fire()
