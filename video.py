#! /usr/bin/env python
import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Int8
from std_msgs.msg import Bool
import numpy as np
def callback3(data):
    global dist
    dist=data.data
def callback2(data):
    global img2
    img2=data
def callback4(data):
    global sw
    sw=data.data
def callback(data):
    np_arr = np.fromstring(data.data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    np_arr2 = np.fromstring(img2.data, np.uint8)
    frame2 = cv2.imdecode(np_arr2, cv2.IMREAD_COLOR)
    cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    if(sw):
        frame1 = cv2.resize(frame2, (100, 70))
        frame[0:70, 540:640] = frame1
        if(dist==1):
        	frame[:, :, 0] = 0
        	frame[:, :, 1] = 0
        	frame2[:, :, 0] = 0
        	frame2[:, :, 1] = 0
        	font=cv2.FONT_HERSHEY_SIMPLEX
        	cv2.putText(frame,"WARNING",(400,250),font,1,(255,255,255),1,cv2.LINE_AA)
        	font=cv2.FONT_HERSHEY_SIMPLEX
        	# cv2.putText(frame,"OBJECTS TOO CLOSE",(10,320),font,2,(255,255,255),1,cv2.LINE_AA)
        cv2.imshow("frame", frame)
    elif(not sw):
        frame1 = cv2.resize(frame, (100, 70))
        frame2[0:70, 540:640] = frame1
        if(dist==1):
        	frame[:, :, 0] = 0
        	frame[:, :, 1] = 0
        	frame2[:, :, 0] = 0
        	frame2[:, :, 1] = 0
        	font=cv2.FONT_HERSHEY_SIMPLEX
        	cv2.putText(frame2,"WARNING",(200,250),font,1,(255,255,255),3,cv2.LINE_AA)
        	font=cv2.FONT_HERSHEY_SIMPLEX
        	#cv2.putText(frame2,"OBJECTS TOO CLOSE",(10,320),font,2,(255,255,255),1,cv2.LINE_AA)
        cv2.imshow("frame", frame2)
    cv2.waitKey(1)
def main():
    cam_sub=rospy.Subscriber("/camera1/usb_cam1/image_raw/compressed",CompressedImage,callback)
    cam_sub2=rospy.Subscriber("/camera2/usb_cam2/image_raw/compressed",CompressedImage,callback2)
    dist_sub=rospy.Subscriber("/dist",Int8,callback3)
    switch_sub=rospy.Subscriber("/camera_trigger",Bool,callback4)
    rospy.spin()
if __name__ == '__main__':
    dist=0
    sw=True
    a=True
    rospy.init_node("videosteam")
    img2=CompressedImage()
    main()
