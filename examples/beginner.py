import time
import cv2
from djitellopy import Tello

tello = Tello()

tello.connect()

# 5 point hover
tello.takeoff()
time.sleep(15)
tello.land()

# 5 points square
tello.takeoff
tello.move_left(100)
tello.move_forward(100)
tello.move_right(100)
tello.move_back(100)

# 10 points diamond
tello.rotate_clockwise(45)
tello.move_left(100)
tello.move_forward(100)
tello.move_right(100)
tello.move_back(100)

# 10 points circle
tello.curve_xyz_speed(100, 100, 0, 200, 0, 0, 10)
tello.curve_xyz_speed(-100, -100, 0, -200, 0, 0, 10)

# 20 points image
tello.streamon()
frame_read = tello.get_frame_read()
cv2.imwrite("team.png", frame_read.frame)

# 20 points read 4 ArUCo tags
tello.enable_mission_pads()
pad = tello.get_mission_pad_id()
for i in range(4):
    while pad != i:
        time.sleep(0.01)
    tello.land()
    tello.takeoff()
    break

# 30 points pop ballon
tello.move_forward(100)
tello.move_backward(100)


tello.land()