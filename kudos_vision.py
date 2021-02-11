"#!/usr/bin/env python"
import tensorflow as tf
import cv2
import numpy as np
import darknet
import rospy
from darknetA.msg import position
import kudos_darknet
from collections import deque
import time

class priROS():
    def __init__(self):
        pass

    def talker(self, posX, posY):
        pub = rospy.Publisher('visionPos', position, queue_size=10)
        rospy.init_node('visiontalker', anonymous = True)
        message = position()
        message.posX = posX
        message.posY = posY
        rospy.loginfo(message)
        pub.publish(message)

class DataFormatTransfer():
    def __init__(self):
        pass
    
    def get_one_center_from_detections(self, detections, label):
        max_confidence = 0
        objectCenter = [-1,-1]
        for detections_index,detection in enumerate(detections):
            #print(detection)#(label, confidence, (left, top, right, bottom))
            if detection[0] == label:
                if detection[1]>max_confidence:
                    max_confidence = detection[1]
                    bbox = detection[2]
                    objectCenter = [bbox[2]+(bbox[0]-bbox[2])/2, bbox[3]+(bbox[1]-bbox[3])/2]
        return objectCenter

if __name__=='__main__':
    darknet_config_args = kudos_darknet.parser()
    kudos_darknet.check_arguments_errors(darknet_config_args)
    darknet_network, darknet_class_names, darknet_class_colors, darknet_width, darknet_height = kudos_darknet.Initialize_darknet(darknet_config_args)
    cap = cv2.VideoCapture(-1)
    priROS = priROS()
    DataFormatTransfer = DataFormatTransfer()

    while True:
        frame, detections = kudos_darknet.getResults_with_darknet(cap, darknet_width, darknet_height, darknet_network, darknet_class_names, darknet_class_colors,darknet_config_args)
        peopleCenter = DataFormatTransfer.get_one_center_from_detections(detections, label='person')
        if np.any(frame) != False:
            cv2.imshow("showIMG", frame)
        posX = peopleCenter[0]
        posY = peopleCenter[1]
        priROS.talker(posX, posY)
        k = cv2.waitKey(1) 
        if k == 27:
            break
    cap.release
    cv2.destroyAllWindows()


'''
    while True:
        x =  np.random.randn(10,100)
        posX = 100
        posY = 50
        priROS.talker(posX, posY)
'''