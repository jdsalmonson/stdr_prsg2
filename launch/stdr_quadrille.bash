#!/bin/bash

export ROS_IP=`hostname -I | cut -d' ' -f1`

roslaunch stdr_quadrille_robot0.launch &
sleep 0.5
roslaunch stdr_quadrille_robot1.launch &
sleep 0.5
roslaunch stdr_quadrille_robot2.launch &
sleep 0.5
roslaunch stdr_quadrille_robot3.launch &
sleep 0.5
roslaunch stdr_quadrille_4bots.launch 
