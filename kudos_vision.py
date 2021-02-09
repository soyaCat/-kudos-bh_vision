"#!/usr/bin/env python"
import tensorflow as tf
import cv2
import numpy as np
import darknet
import rospy
from darknetA.msg import position
import kudos_darknet
from Queue import Queue
import time

turnon_darknet = True


class priROS():
    def talker(self, posX, posY):
        pub = rospy.Publisher('visionPos', position, queue_size=10)
        rospy.init_node('visiontalker', anonymous = True)
        message = position()
        message.posX = posX
        message.posY = posY
        rospy.loginfo(message)
        pub.publish(message)

if __name__=='__main__':
    frame_queue = Queue()
    darknet_image_queue = Queue(maxsize=1)
    detections_queue = Queue(maxsize=1)
    fps_queue = Queue(maxsize=1)
    darknet_config_args = kudos_darknet.parser()
    kudos_darknet.check_arguments_errors(darknet_config_args)
    darknet_network, darknet_class_names, darknet_class_colors, darknet_width, darknet_height = kudos_darknet.Initialize_darknet(darknet_config_args)
    cap = cv2.VideoCapture(-1)

    priROS = priROS()
    if turnon_darknet == True:
        pass

    while True:
        frame = kudos_darknet.getResults_with_darknet(cap, darknet_width, darknet_height, darknet_network, darknet_class_names, darknet_class_colors,darknet_config_args)
        if np.any(frame) != False:
            cv2.imshow("showIMG", frame)
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