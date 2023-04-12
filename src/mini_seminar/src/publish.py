#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publish():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('publish', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        name = ["wewon", "minkyum", "jeahyun", "yunsuk", "hohyung", "jeamin", "kueyen","mingue"]
        for i in name:
        	pub.publish(i)
        	        
        rate.sleep()

if __name__ == '__main__':
    try:
        publish()
    except rospy.ROSInterruptException:
        pass
