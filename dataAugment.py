"""
you can flip your images and your bounding box 
"""
import fire
import cv2
import numpy 
import matplotlib.pyplot as plt
import os

def image_flip(imageDir_path="", trainLable_path="", outputpath="") :
    """
    flip image left to right, and flip the bounding box either.
    output pic end with "-flipped"

    Args: 
        imageDir_path: the path of the train pic dir
        trainLable_path: the path of the train label path
        outputpath: the path of the flipped pic and train label

    """

    

def image_udflip(imageDir_path="", trainLable_path="", outputpath="") :
    """
    flip image up to down and flip the bounding box either
    output pic end with "-updown"

    Args: 
        imageDir_path: the path of the train pic dir
        trainLable_path: the path of the train label path
        outputpath: the path of the flipped pic and train label
    """


def image_roate(imageDir_path = "", trainLable_path = "", outputpath="", roate=90):
    """
    roate the image clockwise 
    output pic end with "-roated"
    Args:
        imageDir_path: the path of the train pic dir
        trainLable_path: the path of the train label path
        outputpath: the path of the flipped pic and train label
        roate: the degree pic will roate
    """

def image_saltNoise(imageDir_path = "", trainLable_path = "", outputpath = ""):
    """
    Add salt noise to the pic
    output pic end with "-salt"
    Args:
        imageDir_path: the path of the train pic dir
        trainLable_path: the path of the train label path
        outputpath: the path of the flipped pic and train label
    """


def image_GaussianNoise(imageDir_path = "", trainLable_path = "", outputpath = ""):
    """
    Add salt obeyed the gaussian distribution to the pic
    output pic end with "-gauss"
    Args:
        imageDir_path: the path of the train pic dir
        trainLable_path: the path of the train label path
        outputpath: the path of the flipped pic and train label
    """

def image_moveUp(imageDir_path = "", trainLable_path = "", outputpath = "", distance = 0):
    """
    move up ur pic with the distance
    """

def image_moveDown(imageDir_path = "", trainLable_path ="", outputpath= "", distance = 0):
    """
    move down ur pic with distance 
    """

def image_moveLeft(imageDir_path = "", trainLable_path = "", outputpath = "", distance = 0):
    """
    move left ur pic with distance
    """

def image_moveRight(imageDir_path = "", trainLable_path = "", outputpath ="", distance = 0):
    """
    move right ur pic with distance
    """
if __name__ == "__main__":
    fire.Fire()
