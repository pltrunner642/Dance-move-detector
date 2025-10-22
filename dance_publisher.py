import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class DancePublisher(Node):
    def __init__(self):
        super().__init__('dance_publisher')
        self.publisher_ = self.create_publisher(String, 'dance_moves', 10)
        self.timer = self.create_timer(2.0, self.publish_move)
        self.moves = ['step left', 'step right', 'spin', 'jump', 'clap']
        self.get_logger().info("💃 Dance Move Publisher Started...")

    def publish_move(self):
        move = random.choice(self.moves)
        msg = String()
        msg.data = move
        self.publisher_.publish(msg)
        self.get_logger().info(f"🎶 Detected move: {move}")

def main(args=None):
    rclpy.init(args=args)
    node = DancePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
