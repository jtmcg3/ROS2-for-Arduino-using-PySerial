# Node to publish a string topic
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):

	def __init__(self):
		super().__init__('minimal_subscriber')
		self.red_sub = self.create_subscription(String,
			                                         'led_red_topic',
			                                         self.listener_callback,
			                                         10)
		self.red_sub # prevent unused variable warning
		self.yellow_sub = self.create_subscription(String,
			                                         'led_yellow_topic',
			                                         self.listener_callback,
			                                         10)
		self.yellow_sub # prevent unused variable warning
		self.green_sub = self.create_subscription(String,
			                                         'led_green_topic',
			                                         self.listener_callback,
			                                         10)
		self.green_sub # prevent unused variable warning
		self.all_led_sub = self.create_subscription(String,
			                                         'led_all_topic',
			                                         self.listener_callback,
			                                         10)
		self.all_led_sub # prevent unused variable warning
		self.motor_sub = self.create_subscription(String,
			                                         'motor_topic',
			                                         self.listener_callback,
			                                         10)
		self.motor_sub # prevent unused variable warning

	def listener_callback(self, msg):		
		self.get_logger().info('I heard: {}'.format(msg.data))

def main(args=None):
	rclpy.init(args=args)
	minimal_subscriber = MinimalSubscriber()
	rclpy.spin(minimal_subscriber)

if __name__ == '__main__':
	main()