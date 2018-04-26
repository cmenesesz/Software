#!/usr/bin/env python

import rospy #importar ros para python
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
import numpy as np


class detectar(object):
	def __init__(self):
		super(detectar, self).__init__()
                self.publisher = rospy.Publisher("/dectecciondeimagenespato",Image,queue_size=10)
		self.subscriber = rospy.Subscriber("/duckiebot/camera_node/image/rect",Image,self.detectarpatos)
		self.twist = Image()
		


	def detectarpatos(self,msg):
		bridge=CvBridge()
		image=bridge.imgmsg_to_cv2(msg,"bgr8")
		image_out1=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
		mask=cv2.inRange(image_out1,np.array([20,150,115]),np.array([35,255,255]))
		image_out2=cv2.bitwise_and(image_out1,image_out1,mask=mask)
		kernel=np.ones((7,7),np.uint8)
		image_out3=cv2.erode(image_out2,kernel,iterations=1)
		image_out4=cv2.dilate(image_out3,kernel,iterations=1)
		(_,contours,hierarchy)=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		image_out5=image.copy()		
		for contornos in contours:
			area=cv2.contourArea(contornos)
			if area>300:
				x,y,w,h=cv2.boundingRect(contornos)
				image_out5=cv2.rectangle(image,(x,y),(x+w,y+h),([0,255,0]),2)
		Msg=bridge.cv2_to_imgmsg(image_out5,"bgr8")
		self.publisher.publish(Msg)


def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = detectar() # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
