import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TwistStamped

class TwistToTwistStampedNode(Node):
    def __init__(self):
        super().__init__('twist_to_twist_stamped')
        
        # Subscriber to 'cmd_vel' topic from teleop_twist_keyboard
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.twist_callback,
            10
        )
        
        # Publisher to the diff_drive_base_controller's expected topic
        self.publisher = self.create_publisher(
            TwistStamped,
            '/diff_cont/cmd_vel',
            10
        )
        
        self.get_logger().info('Twist to TwistStamped bridge initialized.')

    def twist_callback(self, twist_msg):
        # Convert Twist to TwistStamped
        twist_stamped = TwistStamped()
        twist_stamped.header.stamp = self.get_clock().now().to_msg()
        twist_stamped.header.frame_id = 'base_link'  # Optional frame ID
        twist_stamped.twist = twist_msg  # Copy twist values

        # Publish the TwistStamped message
        self.publisher.publish(twist_stamped)
        self.get_logger().debug(f'Published TwistStamped: {twist_stamped}')

def main(args=None):
    rclpy.init(args=args)
    node = TwistToTwistStampedNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
