import cv2
import io
import socket
import struct
import time
import pickle
import numpy as np
import imutils
import serial
import threading

def returnCameraIndexes():
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr


def testWebCAM(x):
    cap = cv2.VideoCapture(x)
    while(True):
        ret, frame = cap.read()

        # 將圖片轉為灰階
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# receive data from server 
def recv_thread():
    #python -m serial.tools.list_ports
    # global receiveWord,lock

    COM_PORT = '/dev/ttyACM0'
    BAUD_RATES=115200
    ser = serial.Serial(COM_PORT,BAUD_RATES)
    client_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket2.connect(('192.168.20.21', 20101))
    # client_socket2.setblocking(False)
    # addr = ("192.168.20.21",20101)
    # client_socket2.sendto("hello".encode,addr)
    tmp=bytes('Unknown Person\n',encoding='utf8')

    try:
        while 1:
            recv_data=client_socket2.recv(1024)
            print(recv_data)
            # print(recv_data.decode('utf8'))
            if (recv_data==tmp):
                print('enter ALARM !!!')
                ser.write(tmp)
    except Exception as err:
        print('thread-Receive result:')
        print(err)

# as client to send data to server
def client_thread():
    # global receiveWord,lock

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.connect(('0.tcp.ngrok.io', 19194))
    client_socket.connect(('192.168.20.21', 20100))
    # client_socket.setblocking(False)

    cam = cv2.VideoCapture(0)
    img_counter = 0
    #encode to jpeg format
    #encode param image quality 0 to 100. default:95
    #if you want to shrink data size, choose low image quality.
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),100]

    while True:
        try:
            ret, frame = cam.read()
            # print(frame.shape)
            # 影像縮放
            # frame = imutils.resize(frame, width=320)
            # 鏡像
            # frame = cv2.flip(frame,180)
            result, image = cv2.imencode('.jpg', frame, encode_param)
            data = pickle.dumps(image, 0)
            size = len(data)

            print(img_counter)
            if img_counter%5==0:
                client_socket.sendall(struct.pack(">Q", size) + data)
                cv2.imshow('client',frame)

                
            img_counter += 1


            # 若按下 q 鍵則離開迴圈
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except Exception as err:
            print('thread-Receive result:')
            print(err)
            print('-------end the video stream------')
            break

    print('Closing the Socket & Camera...')
    client_socket.close()
    cam.release()


# global var
# receiveWord='empty'
# lock = threading.Lock()




# first_thread = threading.Thread(target = client_thread)
# first_thread.start()

second_thread = threading.Thread(target = recv_thread)
second_thread.start()

# first_thread.join()
second_thread.join()

# testWebCAM(0)
print('End main process')