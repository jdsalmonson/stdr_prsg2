# plotbag_stdr.py - script to open and plot contents of a ROS bag from the PRSG2
# Jay Salmonson
# 8/8/2017
# 10/1/2017 - adapted to STDR simulation

import rosbag
import numpy as np

bagfile = "/tmp/stdr-prsg2-sensors_2017-10-01-13-01-47.bag"
#bagfile = "/tmp/stdr-prsg2-sensors_2017-09-30-00-36-28.bag"
#bagfile = "/tmp/stdr-prsg2-sensors_2017-09-24-00-51-09.bag"

bag = rosbag.Bag(bagfile)
#topic, msg, t = bag.read_messages(topics=['/arduino/sensor/battery_voltage']).next()

#tm0 = bag.get_start_time()

#: read bag data
voltage = []
tm = []
for topic, msg, t in bag.read_messages(topics=['/arduino/sensor/battery_voltage']):
    voltage.append(msg.value)
    tm.append(msg.header.stamp.to_nsec())


ir_1 = []
tm_ir_1 = []
for _, msg, t in bag.read_messages(topics=['/robot0/sonar_0']): #'/arduino/sensor/ir_1']):
    ir_1.append(msg.range)
    tm_ir_1.append(msg.header.stamp.to_nsec())

#get a time zero:
print("ir_1 = ",ir_1)
print("tm_ir_1 = ",tm_ir_1)
tm0 = tm_ir_1[0]

ir_2 = []
tm_ir_2 = []
for _, msg, t in bag.read_messages(topics=['/robot0/sonar_1']): #'/arduino/sensor/ir_2']):
    ir_2.append(msg.range)
    tm_ir_2.append(msg.header.stamp.to_nsec())

servo_1 = []
tm_servo_1 = []
for _, msg, t in bag.read_messages(topics=['/robot0/sonar_0/angle']): #/arduino/sensor/servo_1']):
    servo_1.append(msg.data) #value)
    tm_servo_1.append(t.to_nsec()) #msg.header.stamp.to_nsec())

servo_2 = []
tm_servo_2 = []
for _, msg, t in bag.read_messages(topics=['/robot0/sonar_1/angle']): #/arduino/sensor/servo_2']):
    servo_2.append(msg.data) #value)
    tm_servo_2.append(t.to_nsec()) #msg.header.stamp.to_nsec())

odom_angz = []
odom_linx = []
tm_odom = []
for _, msg, t in bag.read_messages(topics=['/robot0/odom']):
    if msg.twist.twist.linear.z <> 0. or msg.twist.twist.linear.y <> 0.:
        print(msg.twist.twist)
    odom_angz.append(msg.twist.twist.angular.z)
    odom_linx.append(msg.twist.twist.linear.x)
    tm_odom.append(msg.header.stamp.to_nsec())

cmdvel_angz = []
cmdvel_linx = []
tm_cmdvel = []
for _, msg, msg_tm in bag.read_messages(topics=['/robot0/cmd_vel']):
    if msg.linear.z <> 0. or msg.linear.y <> 0.:
        print(msg.twist.twist)
    cmdvel_angz.append(msg.angular.z)
    cmdvel_linx.append(msg.linear.x)
    tm_cmdvel.append(msg_tm.to_nsec())

bag.close()

#: plot data
from pylab import plt

#f, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True)
#ax1.set_title(bagfile)
#ax1.plot((np.array(tm)-tm0)/1.e9, np.array(voltage), 'k', label="voltage [mV]")
#ax1.legend(frameon=True, framealpha=0.5)
f, (ax2, ax3, ax4) = plt.subplots(3, sharex=True)
ax2.plot((np.array(tm_ir_1)-tm0)/1.e9, np.array(ir_1), 'r-', label="ir_1")
ax2.plot((np.array(tm_ir_2)-tm0)/1.e9, np.array(ir_2), 'b-', label="ir_2")
ax2.legend(frameon=True, framealpha=0.5)
ax3.plot((np.array(tm_servo_1)-tm0)/1.e9, np.array(servo_1), 'r-', label="servo_1")
ax3.plot((np.array(tm_servo_2)-tm0)/1.e9, np.array(servo_2), 'b-', label="servo_2")
ax3.legend(frameon=True, framealpha=0.5)
ax4.plot((np.array(tm_odom)-tm0)/1.e9, np.array(odom_linx), 'g-', label="odom.linear.x")
ax4.plot((np.array(tm_odom)-tm0)/1.e9, np.array(odom_angz), 'm-', label="odom.angular.z")
ax4.plot((np.array(tm_cmdvel)-tm0)/1.e9, np.array(cmdvel_linx), 'c-', label="cmd_vel.linear.x")
ax4.plot((np.array(tm_cmdvel)-tm0)/1.e9, np.array(cmdvel_angz), 'y-', label="cmd_vel.angular.z")
ax4.legend(frameon=True, framealpha=0.5)
ax4.set_xlabel("time [s]")
f.subplots_adjust(hspace=0)
plt.show()

