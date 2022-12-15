# Import the necessary libraries
import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes



from std_msgs.msg import String

class keycontroller(Node):

    def __init__(self):
        super().__init__('keycontroller')
        self.publisher_ = self.create_publisher(String, 'filter', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = input("Please enter one of the following: \n N: Normal Frame \n B: Black and White \n T: Threshhold \n G: Gaussian Blur Black and white \n L: Gaussian Blur Color \n")
        #print(msg)
        #print(msg.data)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        


def main(args=None):
    rclpy.init(args=args)

    keyboardcontroller = keycontroller()

    rclpy.spin(keyboardcontroller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    keyboardcontroller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
