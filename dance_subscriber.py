import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DanceSubscriber(Node):
    def __init__(self):
        super().__init__('dance_subscriber')
        self.subscription = self.create_subscription(
            String, 'dance_moves', self.listener_callback, 10)
        self.get_logger().info("🕺 Dance Move Subscriber Ready...")

    def listener_callback(self, msg):
        move = msg.data
        self.get_logger().info(f"🤖 Robot imitates: {move} 💃")

def main(args=None):
    rclpy.init(args=args)
    node = DanceSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
