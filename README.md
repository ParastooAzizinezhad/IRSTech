This program will ask for input about the desired frame and filter. Then will publish the chosen image which is captured from camera.
for filters, it also calculates and publishes the mean pixel value.

I used ROS2 Humble, python3, Ubuntu 22.04

How to get started:


Go to your ros workspace:

cd ~/ros2_ws/src


source ros:

source /opt/ros/humble/setup.bash



creake a package (name the package anything you want):

ros2 pkg create --build-type ament_python cv_basics --dependencies rclpy image_transport cv_bridge sensor_msgs std_msgs opencv2



prepration:

cd ~/dev_ws/src/cv_basics

gedit package.xml              #copy the package xml file here or just paste it in this repository

cd ~/ros2_ws

colcon build



copy the files:

cd ~/ros2_ws/src/cv_basics/cv_basics

gedit keyboardcontrol.py

gedit webcam_pub.py

gedit webcam_sub.py

cd ~/dev_ws/src/cv_basics

getit setup.py



Build the package:

cd ~/ros2_ws

rosdep install -i --from-path src --rosdistro humble -y

colcon build 



run the nodes:

in terminal 1 :

source /opt/ros/humble/setup.bash

source ~/ros2_ws/install/local_setup.bash

ros2 run cv_basics keyboard_controller 


in terminal 2 :

source /opt/ros/humble/setup.bash

source ~/ros2_ws/install/local_setup.bash

ros2 run cv_basics img_publisher 


in terminal 3 :

source /opt/ros/humble/setup.bash

source ~/ros2_ws/install/local_setup.bash

ros2 run cv_basics img_subscriber 




Note:
mean pixle value will be printed in img-publisher terminal. It can also be seen using ros2 topic echo /mean_pixel_value

