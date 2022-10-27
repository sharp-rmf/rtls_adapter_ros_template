#!/usr/bin/env python3
import time
import sys
import argparse
import yaml
import nudged
import rclpy
from rclpy.node import Node
from rtls_adapter_ros_template.RTLSClientAPI import rtlsAPI
from rmf_rtls_msgs.msg import TagState, TagLocation
from geometry_msgs.msg import Point


class RTLSAdapter(Node):
    def __init__(self, transform):
        super().__init__("rtls_adapter_ros_template")
        
        ### Enter potential Adapter Parameters ###
        #        IMPLEMENT YOUR CODE HERE        # 
        # <Some Basic Paramters>                 #
        # self.model  = "model_name"             #
        # self.tag_id = "unique_tag_id"          #
        #                                        #
        # <Adapter Connection Paramters>         #
        # self.serial = "/dev/ttyUSB0"           #
        # or                                     #
        # self.host = '192.168.10.1'             #
        # self.port = 5000                       #
        ##########################################

        ## Basic ROS settings and rtlsAPI setup
        self.tag_topic_name = "/tag_state"
        self.update_freq = 1
        self.pose_publisher = self.create_publisher(TagState, self.tag_topic_name, 10)
        self.api = rtlsAPI("Adapter Connection paramters")
        try:
            self.api.connect()
            self.get_rmf_transform(transform)
            self.timer = self.create_timer(self.update_freq, self.start_tracking)
        except Exception as e:
            self.get_logger().error(f"{e}")
 

    def get_rmf_transform(self, transform):
        rmf_ref_coordinates = transform['transform']['rmf_ref_coordinates']
        rtls_ref_coordinates = transform['transform']['rtls_ref_coordinates']
        try:
            self.rtls2rmf_transform = nudged.estimate(rtls_ref_coordinates, rmf_ref_coordinates)
            self.rmf2rtls_transform = nudged.estimate(rmf_ref_coordinates, rtls_ref_coordinates)
        except Exception as e:
            self.get_logger().info(f"Error: {e}")
            return False
        return True

    def start_tracking(self):
        if self.api.isconnected:
            tag_state = TagState()
            tag_location = TagLocation()
            tag_pose = Point()
            x, y, z = self.api.get_pos()
            pose = self.rmf2rtls_transform.transform([x, y])
            ### Sample TagState variable inputs ###
            #      IMPLEMENT YOUR CODE HERE       #
            # tag_pose.x = pose[0]                #
            # tag_pose.y = pose[1]                #
            # tag_location.map = self.map_id      #
            # tag_location.pose = tag_pose        #
            # tag_state.model = self.model        #
            # tag_state.name = self.tag_id        #
            # tag_state.status = 5                #
            # tag_state.type = "Description"      #
            # tag_state.location = tag_location   #
            #######################################
            self.get_logger().info("Publishing Tag State")
            self.pose_publisher.publish(tag_state)
            time.sleep(self.update_freq)

def main(argv=sys.argv):
    rclpy.init(args=sys.argv)
    args_without_ros = rclpy.utilities.remove_ros_args(sys.argv)

    parser = argparse.ArgumentParser(
        prog="rtls_adapter",
        description="Configure and spin up the rtls adapter")
    parser.add_argument("-c", "--config-file", type=str, required=True,
                        help="Path to the config.yaml file")
    args = parser.parse_args(args_without_ros[1:])
    config_path = args.config_file
   
    # Load config for reference coordinates used in nudged
    with open(config_path, "r") as f:
        config_yaml = yaml.safe_load(f)

    try:
        print(f"Starting RTLS adapter...")
        tag = RTLSAdapter(config_yaml)
        # Start the rtls adapter
        rclpy.spin(tag)
    except KeyboardInterrupt:
        # Shutdown
        tag.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main(sys.argv)