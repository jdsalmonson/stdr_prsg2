# stdr_prsg2
ROS launch scripts to run the [Programming Robots Study Group](http://programmingrobotsstudygroup.github.io/) robot (PRSG2) in the [STDR](http://stdr-simulator-ros-pkg.github.io/) simulator.  This is a self-contained ROS node.

*Prerequisite:*
The STDR package must be installed on your ROS system.  These should be available on your Ubuntu system (e.g. `apt-cache search stdr`).  If you are using the ServoPose read and write services (so that your sensors can move on servos), install from [source](https://github.com/jdsalmonson/stdr_simulator).

*Installation:*
Copy the `stdr_prsg2/` directory tree into your ROS `catkin_ws/src/` directory.  Then perform a `catkin_make` to install.  This uses ROS Kinetic, but other versions will likely work.

Directories:
* `launch/`

  * `stdr_prsg2.launch` is the main launch script that creates the PRSG robot in a maze, begins bagging topics and starts a teleop node so that you drive the robot around.  Usage: `roslaunch stdr_prsg2.launch`.  To turn off bagging: `roslaunch stdr_prsg2.launch record_sensors := false`

  * `rviz.launch` launches rviz with the robot displayed on the maze.  Usage: after `stdr_prsg2.launch` has been launched, in a different window: `roslaunch rviz.launch`

  * `plotbag_stdr.py` is python script that plots the rosbag of topic data collected from `stdr_prsg2.launch`.  Edit the file so that `bagfile` points to the created bag file.

* `robots/` is where the PRSG2 robot model YAML files are located.

  * `prsg2_jay_robot.yaml` is the YAML file for Jay's two servo-mounted IR sensor robot.
