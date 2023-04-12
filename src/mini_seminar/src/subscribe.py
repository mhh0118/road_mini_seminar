#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
	print(data.data)
def subscribe():
	rospy.init_node("subscribe", anonymous=True)
	rospy.Subscriber("chatter",String, callback)
	rospy.spin()

if __name__=='__main__':
	subscribe()
