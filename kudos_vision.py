"#!/usr/bin/env python"
# import tensorflow as tf
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
save_input_video = False
#capture_target = "test_flag.mp4" #-1
capture_target = -1
#host_address = "tcp://192.168.0.20:9010"
host_address = "tcp://localhost:9010"
default_x = -100.0
default_y = -100.0


class priROS():
    def __init__(self):
        pass

    def talker(self, posX, posY, goalposX, goalposY, ball_size):
        pub = rospy.Publisher('visionPos', position, queue_size=1)
        rospy.init_node('visionPos', anonymous = False)
        message = position()
        message.posX = posX
        message.posY = posY
        message.goalposX = goalposX
        message.goalposY = goalposY
        message.POS_size = ball_size
        rospy.loginfo(message)
        pub.publish(message)

class DataFormatTransfer():
    def __init__(self):
        pass
    
    def get_one_center_from_detections(self, detections, label):
        max_confidence = 0
        objectCenter = [default_x ,default_y]
        object_size = 0
        for detections_index, detection in enumerate(detections):
            #print(detection)#(label, confidence, (left, top, right, bottom))
            if detection[0] == label:
                if detection[1]>max_confidence:
                    max_confidence = detection[1]
                    bbox = detection[2]
                    objectCenter = [bbox[0], bbox[1]]
                    object_size = (bbox[2]+bbox[3])/2
        return objectCenter, object_size

    def get_mean_center_from_detections(self, detections, label):
        objectCenter = [default_x ,default_y]
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

        return objectCenter, 0

    def mapping_point_to_float_shape(self, npArr, objectCenter, objectSize):
        if objectCenter != [default_x, default_y]:
            im_width_size = np.shape(npArr)[0]
            im_hight_size = np.shape(npArr)[1]
            objectSize = objectSize/((im_width_size+im_hight_size)/2)
            objectCenter[0] = objectCenter[0]/im_width_size
            objectCenter[1] = objectCenter[1]/im_hight_size
            objectCenter[0] = (objectCenter[0] - 0.5)
            objectCenter[1] = (objectCenter[1] - 0.5)



        return objectCenter, objectSize

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
        cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    else:
        socket = get_socket_and_send_ini_message(host_address)
    
    if save_input_video == True:
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        out = cv2.VideoWriter('save.avi', fourcc, 25.0,(640,480))
    priROS = priROS()
    DataFormatTransfer = DataFormatTransfer()

    while True:
        if detect_from_virtual_ENV == False:
            ret, frame = cap.read()
        else:
            frame = znp.recv_array(socket)
            ret = True
        if save_input_video == True:
            out.write(frame)
        frame, detections = kudos_darknet.getResults_with_darknet(ret, frame, darknet_width, darknet_height, darknet_network, darknet_class_names, darknet_class_colors,darknet_config_args)
        ballCenter = [-100.0, -100.0]
        goalCenter = [-100.0, -100.0]
        ball_size = 0
        if np.any(frame) != False:
            cv2.imshow("showIMG", frame)
            ballCenter, ball_size = DataFormatTransfer.get_one_center_from_detections(detections, label='ball')
            ballCenter,ball_size = DataFormatTransfer.mapping_point_to_float_shape(frame, ballCenter, ball_size)
            goalCenter,_ = DataFormatTransfer.get_mean_center_from_detections(detections, label='goal')
            goalCenter,_ = DataFormatTransfer.mapping_point_to_float_shape(frame, goalCenter, 0)
        posX = ballCenter[0]
        posY = ballCenter[1]
        goalposX = goalCenter[0]
        goalposY = goalCenter[1]
        if detect_from_virtual_ENV == False:
            priROS.talker(posX, posY, goalposX, goalposY, ball_size)
        else:
            position_list = [posX, posY, goalposX, goalposY]
            position_npArr = np.array(position_list)
            znp.send_array(socket, position_npArr)
        k = cv2.waitKey(1) 
        if k == 27:
            break
    cap.release
    cv2.destroyAllWindows()
