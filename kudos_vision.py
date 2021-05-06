"#!/usr/bin/env python"
import tensorflow as tf
import cv2
import numpy as np
import darknet
import rospy
from darkneta.msg import position
import kudos_darknet
from collections import deque
import time
import zmq
import zmqnumpy as znp

detect_from_virtual_ENV = False
#capture_target = "test_flag.mp4" #-1
capture_target = -1
#host_address = "tcp://192.168.0.20:9010"
host_address = "tcp://localhost:9010"

class priROS():
    def __init__(self):
        pass

    def talker(self, posX, posY, goalposX, goalposY):
        pub = rospy.Publisher('visionPos', position, queue_size=10)
        rospy.init_node('visiontalker', anonymous = True)
        message = position()
        message.posX = posX
        message.posY = posY
        message.goalposX = goalposX
        message.goalposY = goalposY
        rospy.loginfo(message)
        pub.publish(message)

class DataFormatTransfer():
    def __init__(self):
        pass
    
    def get_one_center_from_detections(self, detections, label):
        max_confidence = 0
        objectCenter = [-1.0,-1.0]
        for detections_index, detection in enumerate(detections):
            #print(detection)#(label, confidence, (left, top, right, bottom))
            if detection[0] == label:
                if detection[1]>max_confidence:
                    max_confidence = detection[1]
                    bbox = detection[2]
                    objectCenter = [bbox[0], bbox[1]]
        return objectCenter

    def get_mean_center_from_detections(self, detections, label):
        objectCenter = [-1.0,-1.0]
        object_width_list = []
        object_height_list = []
        detect_flag = False
        for detections_index, detection in enumerate(detections):
            #print(detection)#(label, confidence, (left, top, right, bottom))
            if detection[0] == label:
                bbox = detection[2]
                object_width_list.append(bbox[0])
                object_height_list.append(bbox[1])
                detect_flag = True
        if detect_flag == True:
            objectCenter = [np.mean(object_width_list), np.mean(object_height_list)]

        return objectCenter

    def mapping_point_to_float_shape(self, npArr, objectCenter):
        if objectCenter != [-1.0, -1.0]:
            im_width_size = np.shape(npArr)[0]
            im_hight_size = np.shape(npArr)[1]
            objectCenter[0] = objectCenter[0]/im_width_size
            objectCenter[1] = objectCenter[1]/im_hight_size

        return objectCenter

def get_socket_and_send_ini_message(host_adress):
    context = zmq.Context()
    #Socket to talk to server
    print("Connecting to hello world server...")
    socket = context.socket(zmq.REQ)
    socket.connect(host_address)
    socket.send(b"hello, this is kudos_vision!")

    return socket

if __name__=='__main__':
    darknet_config_args = kudos_darknet.parser()
    kudos_darknet.check_arguments_errors(darknet_config_args)
    darknet_network, darknet_class_names, darknet_class_colors, darknet_width, darknet_height = kudos_darknet.Initialize_darknet(darknet_config_args)
    if detect_from_virtual_ENV == False:
        cap = cv2.VideoCapture(capture_target)
    else:
        socket = get_socket_and_send_ini_message(host_address)
    priROS = priROS()
    DataFormatTransfer = DataFormatTransfer()

    while True:
        if detect_from_virtual_ENV == False:
            ret, frame = cap.read()
        else:
            frame = znp.recv_array(socket)
            ret = True
        frame, detections = kudos_darknet.getResults_with_darknet(ret, frame, darknet_width, darknet_height, darknet_network, darknet_class_names, darknet_class_colors,darknet_config_args)
        ballCenter = [-1.0, -1.0]
        goalCenter = [-1.0, -1.0]
        if np.any(frame) != False:
            cv2.imshow("showIMG", frame)
            ballCenter = DataFormatTransfer.get_one_center_from_detections(detections, label='ball')
            ballCenter = DataFormatTransfer.mapping_point_to_float_shape(frame, ballCenter)
            goalCenter = DataFormatTransfer.get_mean_center_from_detections(detections, label='goal')
            goalCenter = DataFormatTransfer.mapping_point_to_float_shape(frame, goalCenter)
        posX = ballCenter[0]
        posY = ballCenter[1]
        goalposX = goalCenter[0]
        goalposY = goalCenter[1]
        if detect_from_virtual_ENV == False:
            priROS.talker(posX, posY, goalposX, goalposY)
        else:
            position_list = [posX, posY, goalposX, goalposY]
            position_npArr = np.array(position_list)
            znp.send_array(socket, position_npArr)
        k = cv2.waitKey(1) 
        if k == 27:
            break
    cap.release
    cv2.destroyAllWindows()