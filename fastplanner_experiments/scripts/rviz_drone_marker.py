#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from visualization_msgs.msg import Marker

rospy.init_node("rviz_drone_marker")
pub = rospy.Publisher("/rviz_drone_marker", Marker, queue_size=1)

def callback(msg):
    marker = Marker()
    marker.header = msg.header
    marker.ns = "drone"
    marker.id = 0
    marker.type = Marker.ARROW
    marker.action = Marker.ADD
    marker.pose = msg.pose.pose
    marker.scale.x = 1.5
    marker.scale.y = 0.18
    marker.scale.z = 0.18
    marker.color.r = 1.0
    marker.color.g = 0.1
    marker.color.b = 0.1
    marker.color.a = 1.0
    marker.lifetime = rospy.Duration(0)
    pub.publish(marker)

rospy.Subscriber("/mavros/local_position/odom", Odometry, callback)
rospy.spin()
