import zmq
import zmqnumpy as znp
import numpy as np
import time

host_address = "tcp://localhost:9010"

def get_socket_and_send_ini_message(host_adress):
    context = zmq.Context()
    #Socket to talk to server
    print("Connecting to hello world server...")
    socket = context.socket(zmq.REQ)
    socket.connect(host_address)
    socket.send(b"hello, this is kudos_vision!")

    return socket
if __name__ == "__main__":
    socket = get_socket_and_send_ini_message(host_address)

    for request in range(100):
        received_npArr = znp.recv_array(socket)
        print(np.shape(received_npArr))

