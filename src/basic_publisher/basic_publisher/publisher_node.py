# Node to publish a string topic
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):

	def __init__(self):
		super().__init__('minimal_publisher')
		self.red_publisher_ = self.create_publisher(String, 'led_red_topic', 10)
		self.yellow_publisher_ = self.create_publisher(String, 'led_yellow_topic', 10)
		self.green_publisher_ = self.create_publisher(String, 'led_green_topic', 10)
		self.all_publisher_ = self.create_publisher(String, 'led_all_topic', 10)
		self.motor_publisher_ = self.create_publisher(String, 'motor_topic', 10)
		timer_period = 3 # second
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0

	def timer_callback(self):
		red = String()
		yellow = String()
		green = String()
		all_led = String()
		motor = String()
		if self.i % 11 == 0:
			red.data = "on"
			yellow.data = "off"
			green.data = "off"
			all_led.data = "off"
			motor.data = "lock"
		elif self.i % 7 == 0:
			red.data = "off"
			yellow.data = "on"
			green.data = "off"
			all_led.data = "off"
			motor.data = "unlock"
		elif self.i % 5 == 0:
			red.data = "off"
			yellow.data = "off"
			green.data = "on"
			all_led.data = "off"
			motor.data = "lock"
		elif self.i % 2 == 0:
			red.data = "off"
			yellow.data = "off"
			green.data = "off"
			all_led.data = "on"
			motor.data = "unlock"

		self.red_publisher_.publish(red)
		self.yellow_publisher_.publish(yellow)
		self.green_publisher_.publish(green)
		self.all_publisher_.publish(all_led)
		self.motor_publisher_.publish(motor)
		self.get_logger().info('So many messages: [{},{},{},{},{}]'.format(red.data,
			                                                               yellow.data,
			                                                               green.data,
			                                                               all_led.data,
			                                                               motor.data))
		self.i += 1

def main(args=None):
	rclpy.init(args=args)
	minimal_publisher = MinimalPublisher()
	rclpy.spin(minimal_publisher)

if __name__ == '__main__':
	main()