# Node to publish a string topic
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class LedController(Node):

	def __init__(self):
		super().__init__('led_controller')
		self.ser = serial.Serial('/dev/ttyACM0')
		self.red_sub = self.create_subscription(String,
			                                         'led_red_topic',
			                                         self.red_listener_callback,
			                                         10)
		self.red_sub # prevent unused variable warning
		self.yellow_sub = self.create_subscription(String,
			                                         'led_yellow_topic',
			                                         self.yellow_listener_callback,
			                                         10)
		self.yellow_sub # prevent unused variable warning
		self.green_sub = self.create_subscription(String,
			                                         'led_green_topic',
			                                         self.green_listener_callback,
			                                         10)
		self.green_sub # prevent unused variable warning
		self.all_led_sub = self.create_subscription(String,
			                                         'led_all_topic',
			                                         self.all_listener_callback,
			                                         10)
		self.all_led_sub # prevent unused variable warning


	def red_listener_callback(self, msg):
		if msg.data == "on":
			self.ser.write(b'redon!')
			self.get_logger().info('Command sent to turn red on')
		

	def yellow_listener_callback(self, msg):
		if msg.data == "on":
			self.ser.write(b'yellowon!')
			self.get_logger().info('Command sent to turn yellow on')


	def green_listener_callback(self, msg):
		if msg.data == "on":
			self.ser.write(b'greenon!')
			self.get_logger().info('Command sent to turn green on')


	def all_listener_callback(self, msg):
		if msg.data == "on":
			self.ser.write(b'allon!')
			self.get_logger().info('Command sent to turn all LEDs on')



def main(args=None):
	rclpy.init(args=args)
	led_controller = LedController()
	rclpy.spin(led_controller)

if __name__ == '__main__':
	main()