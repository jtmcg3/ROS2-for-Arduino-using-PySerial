import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

class MotorController(Node):

	def __init__(self):
		super().__init__('motor_controller')
		self.ser = serial.Serial('/dev/ttyACM0')
		self.motor_sub = self.create_subscription(String,
			                                         'motor_topic',
			                                         self.motor_listener_callback,
			                                         10)
		self.motor_sub # prevent unused variable warning


	def motor_listener_callback(self, msg):
		time.sleep(1)
		if msg.data == "lock":
			self.ser.write(b"lock!")
			self.get_logger().info('Command send to {} the box'.format(msg.data))
		else:
			self.ser.write(b'unlock!')
			self.get_logger().info('Command send to {} the box'.format(msg.data))



def main(args=None):
	rclpy.init(args=args)
	motor_controller = MotorController()
	rclpy.spin(motor_controller)

if __name__ == '__main__':
	main()