#!/usr/bin/env python3
import numpy as np
import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2
from std_msgs.msg import Header

def main():
    rospy.init_node("orchard_map_publisher")

    path = "/home/robot/fastplanner_experiments/fixed_seed_12345/map_seed_12345.xyz"
    points = np.loadtxt(path, dtype=np.float32)
    points = points[np.isfinite(points).all(axis=1)]

    pub = rospy.Publisher(
        "/orchard_map/points", PointCloud2, queue_size=1, latch=True
    )

    header = Header()
    header.stamp = rospy.Time(0)
    header.frame_id = "map"

    cloud = point_cloud2.create_cloud_xyz32(header, points.tolist())
    pub.publish(cloud)

    rospy.loginfo(
        "Published %d orchard points on /orchard_map/points", len(points)
    )
    rospy.spin()

if __name__ == "__main__":
    main()
