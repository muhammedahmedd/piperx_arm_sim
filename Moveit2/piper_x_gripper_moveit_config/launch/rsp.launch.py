from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder(
        "piper_x",
        package_name="piper_x_gripper_moveit_config"
    ).to_moveit_configs()

    ld = LaunchDescription()

    ld.add_action(
        DeclareLaunchArgument(
            "publish_frequency",
            default_value="15.0"
        )
    )

    rsp_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        respawn=True,
        output="screen",
        parameters=[
            moveit_config.robot_description,
            {
                "publish_frequency": LaunchConfiguration("publish_frequency"),
                "use_sim_time": True,
            },
        ],
    )

    ld.add_action(rsp_node)

    return ld