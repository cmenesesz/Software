#!/usr/bin/env python

import rospy #importar ros para python
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
import numpy as np


class distancia(object):
	def __init__(self):
		super(distancia, self).__init__()
                self.publisher = rospy.Publisher("/dectecciondeimagenespato2",Image,queue_size=10)
		self.subscriber = rospy.Subscriber("/dectecciondeimagenespato",Image,self.caldist)
		self.twist = Image()
		


	def caldist(self,msg):
		
		self.publisher.publish(Msg)


def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = distancia() # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
