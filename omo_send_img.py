import zmq
import zmqnumpy as znp
import numpy as np
import time
import cv2

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:9010")
    print("wait receive message from client...")
    message = socket.recv()
    print("message: ", message)
    cap = cv2.VideoCapture(0)
    while 1:
        #ret, frame = cap.read()
        position_list = [0.666,0.999,0.444,0.222]
        position_npArr = np.array(position_list)
        print(position_npArr)
        if np.any(position_npArr) != False:
            znp.send_array(socket, position_npArr)
        time.sleep(2)

