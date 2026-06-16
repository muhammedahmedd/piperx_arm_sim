# Piper X Arm Sim

This repository is a modified fork of the original AgileX `agx_arm_sim` repository.

I use this fork for my Piper X arm setup with ROS 2 Humble, MoveIt 2, and Isaac Sim. The main goal of this fork is to make the Piper X MoveIt setup work cleanly with Isaac Sim by synchronizing MoveIt-related ROS 2 nodes with Isaac Sim simulation time.

This is important because Isaac Sim publishes simulated timestamps through `/clock`. MoveIt, `robot_state_publisher`, `ros2_control_node`, and joint state updates need to use that same simulated clock so planning, controller timing, and joint state feedback stay consistent.

The original AgileX repository content is still available in the `master` branch of this fork. For the full original documentation and all supported AgileX robot models, refer to that branch or the upstream `agilexrobotics/agx_arm_sim` repository.

## What this fork changes

This branch focuses on the Piper X arm and includes the changes needed for my MoveIt/Isaac Sim workflow:

* Updates MoveIt-related launch files to use Isaac Sim simulation time.
* Sets `use_sim_time` for nodes such as `move_group`, `robot_state_publisher`, and `ros2_control_node`.
* Keeps MoveIt timing, joint state updates, and controller behavior synchronized with Isaac Sim timestamps.
* Updates controller spawning so the joint state broadcaster, arm controller, and gripper controller load in order.
* Points the URDF submodule to my Piper X-focused URDF fork, which includes a fixed `gripper_tcp` frame.

## Repository structure

```text
piperx_arm_sim/
├── agx_arm_description/
│   └── agx_arm_urdf/                   # Piper X-focused URDF submodule
├── Moveit2/
│   └── piper_x_gripper_moveit_config/  # Piper X MoveIt configuration
├── realsense2_description/             # RealSense camera description package
└── .gitmodules                         # Submodule configuration
```

## Clone the repository

Clone the repository with submodules:

```bash
cd ~/piperx_ws/src
git clone --recursive https://github.com/muhammedahmedd/piperx_arm_sim.git
```

If the repository was cloned without `--recursive`, initialize the submodule manually:

```bash
cd ~/piperx_ws/src/piperx_arm_sim
git submodule update --init --recursive
```

## Environment

This repository is intended to be used as a dependency inside a larger ROS 2 Humble workspace.

In my project, the ROS 2 and MoveIt dependencies are handled by the main project Docker setup. This fork only provides the Piper X description and MoveIt configuration files needed by that workspace.

If you are not using the Docker setup from the main project, install the required ROS 2 dependencies manually, including MoveIt 2, ROS 2 control, controller packages, and `topic_based_ros2_control`.


## Build

From the workspace root:

```bash
cd ~/piperx_ws
colcon build
source install/setup.bash
```

## Run MoveIt and RViz

Start the Isaac Sim simulation first. The Isaac Sim scene should be loaded and running before launching MoveIt because this fork uses Isaac Sim simulation time.

After Isaac Sim is running, launch MoveIt and RViz with:

```bash
ros2 launch piper_x_gripper_moveit_config demo.launch.py
```

This launch starts MoveIt, RViz, `robot_state_publisher`, `ros2_control_node`, and the controller spawners with simulation-time support. This keeps MoveIt timing, joint state updates, and controller behavior synchronized with the timestamps coming from Isaac Sim.

When everything starts correctly, the joint state broadcaster, arm controller, and gripper controller should load, and MoveGroup should be ready for planning.

## Notes

This branch is project-focused. It is not meant to replace the full AgileX `agx_arm_sim` repository. This branch keeps the parts needed for my Piper X arm workflow.

For the original AgileX package and full multi-arm documentation, use the `master` branch of this fork or the upstream AgileX repository.
