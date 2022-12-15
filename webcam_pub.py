# Basic ROS 2 program to for IRS technical interview 
# video from your built-in webcam
# Author:
# - Parastoo Azizinezhad
  
# Import the necessary libraries
import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

import keyboard
from std_msgs.msg import String
from std_msgs.msg import Float64
import numpy as np

 
class ImagePublisher(Node):
  """
  Create an ImagePublisher class, which is a subclass of the Node class.
  """
  def __init__(self):
    """
    Class constructor to set up the node
    """
    # Initiate the Node class's constructor and give it a name
    super().__init__('image_publisher')
      
    # Create the publisher. This publisher will publish an Image
    # to the video_frames topic. The queue size is 1 messages.
    self.publisher_ = self.create_publisher(Image, 'video_frames', 1)
    # to the mean_pixle_value topic. The queue size is 10 messages. 
    self.publisher_mean = self.create_publisher(Float64, 'mean_pixel_value', 10) # task3
    #subscription to filter topic
    self.subscription = self.create_subscription( String,
            'filter',
            self.listener_callback,
            10)
    self.subscription  # prevent unused variable warning 
    
   
         
    # Create a VideoCapture object
    # The argument '0' gets the default webcam.
    self.cap = cv2.VideoCapture(0)
         
    # Used to convert between ROS and OpenCV images
    self.br = CvBridge()
    
    
  def listener_callback(self, msg):
  
    
    self.get_logger().info('I heard: "%s"' % msg.data)
    i=0
    #while(i<20):
      #ret, frame = self.cap.read()
      #self.publisher_.publish(self.br.cv2_to_imgmsg(frame))
      #i=i+1
      #print(i)
    #print(ret)
    #status = cv2.imwrite('~/results/ros2test.png', frame)
    #if ret == True:
      #cv2.imshow('images',frame)
      #print("ifwastrue")
    
    command = msg.data
    
    if command == 'N' or command == 'n':
      self.get_logger().info('Publishing the original Image')
      while(i<5):
        ret, frame = self.cap.read()
        #image = frame
        #cv2.imshow('window',frame)
        i=i+1
      self.publisher_.publish(self.br.cv2_to_imgmsg(frame))

    elif command == 'B' or command == 'b':
      self.get_logger().info('Publishing a Black and White Image')
      while(i<10):
        ret, frame = self.cap.read()
        bwframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        i=i+1
      self.publisher_.publish(self.br.cv2_to_imgmsg(bwframe))
    elif command == 'T' or command == 't':
      self.get_logger().info('Publishing the Image with Binary Threshold')
      while(i<10):
        ret, frame = self.cap.read()
        i=i+1
      bwframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      ret, threshframe = cv2.threshold(bwframe, 127,255,cv2.THRESH_BINARY)
      meanvalue = Float64()
      meanvalue.data = threshframe.mean()
      print("The mean pixel value: ",meanvalue.data)
      self.publisher_mean.publish(meanvalue)
      self.publisher_.publish(self.br.cv2_to_imgmsg(threshframe))
    elif command == 'G' or command == 'g':
      self.get_logger().info('Publishing the Image with Gaussian Blur Filter on Black and white image')
      while(i<10):
        ret, frame = self.cap.read()
        #ret, gussianframe = cv2.GussianBlur(frame, (5,5),cv2.BORDER_DEFAULT)
        i=i+1
      bwframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      gaussianframe = cv2.GaussianBlur(bwframe, (9,9),cv2.BORDER_DEFAULT)
      meanvalue = Float64()
      meanvalue.data = gaussianframe.mean()
      print("The mean pixel value: ",meanvalue.data)
      self.publisher_mean.publish(meanvalue)
      self.publisher_.publish(self.br.cv2_to_imgmsg(gaussianframe))
    elif command == 'L' or command == 'l':
      self.get_logger().info('Publishing the Image with Gaussian Blur Filter on color image')
      while(i<10):
        ret, frame = self.cap.read()
        #ret, gussianframe = cv2.GussianBlur(frame, (5,5),cv2.BORDER_DEFAULT)
        i=i+1
      gaussianframe = cv2.GaussianBlur(frame, (9,9),cv2.BORDER_DEFAULT)
      meanvalue = Float64()
      meanvalue.data = gaussianframe.mean()
      print("The mean pixle value: ",meanvalue.data)
      self.publisher_mean.publish(meanvalue)
      self.publisher_.publish(self.br.cv2_to_imgmsg(gaussianframe))
    else:
      print("Unvalid Entry.")
 
 

def main(args=None):
  
  
  # Initialize the rclpy library'
  rclpy.init(args=args)
  
  # Create the node
  image_publisher = ImagePublisher()
  
  # Spin the node so the callback function is called.
  rclpy.spin(image_publisher)
  
  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  image_publisher.destroy_node()
  
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()
