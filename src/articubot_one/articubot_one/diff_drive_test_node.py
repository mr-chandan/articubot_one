import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped

class DiffDriveTestNode(Node):
    def __init__(self):
        super().__init__('diff_drive_test_node')
        self.publisher = self.create_publisher(TwistStamped, '/diff_cont/cmd_vel', 10)
        self.get_logger().info("Node initialized and publisher created.")

        self.command = TwistStamped()
        self.command.twist.linear.x = 0.1
        self.command.twist.angular.z = 0.1

        self.timer = self.create_timer(0.05, self.publish_command)

    def publish_command(self):
        self.command.header.stamp = self.get_clock().now().to_msg()
        self.publisher.publish(self.command)
        self.get_logger().debug("Published velocity command.")

def main(args=None):
    rclpy.init(args=args)
    node = DiffDriveTestNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
