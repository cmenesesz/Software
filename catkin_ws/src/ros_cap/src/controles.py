#!/usr/bin/env python

import rospy #importar ros para python
from duckietown_msgs.msg import Twist2DStamped
from sensor_msgs.msg import Joy

class Control(object):
	def __init__(self):
		super(Control, self).__init__()
                self.publisher = rospy.Publisher("/duckiebot/wheels_driver_node/car_cmd",Twist2DStamped,queue_size=10)
		self.subscriber = rospy.Subscriber("/duckiebot/joy/",Joy,self.controlar)
		self.twist = Twist2DStamped()
		


	def controlar(self,msg):
		x=msg.axes[1]*2
		y=msg.axes[0]*10
		z=msg.buttons[0]
		if z==1:
			self.twist.v= 0.0
			self.twist.omega = 0.0
		else:
			self.twist.v = x
			self.twist.omega = y
		self.publisher.publish(self.twist)

def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Control() # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
