import time
from djitellopy import Tello
from examples import objectdetection

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

# 50 point balloon recognition
tello.takeoff()
# need to add colors other than green and multi-object detection
while objectdetection(frame_read.frame) == None:
    time.sleep(0.01)
tello.land()

# 50 point go to mission pad
tello.takeoff()
# searching for mission pad
move = 1
direction = "forward"
while tello.get_mission_pad() != 1:
    match direction:
        case"forward":
            for i in range(move):
                tello.move_forward(10)
                direction = "left"
                if tello.get_mission_pad() == 1:
                    break
        case "left":
            for i in range(move):
                tello.move_left(10)
                direction = "back"
                move += 1
                if tello.get_mission_pad() == 1:
                    break
        case "back":
            for i in range(move):
                tello.move_forward(10)
                direction = "right"
                if tello.get_mission_pad() == 1:
                    break
        case "right":
            for i in range(move):
                tello.move_right(10)
                direction = "forward"
                move += 1
                if tello.get_mission_pad() == 1:
                    break
tello.go_xyz_speed(tello.get_mission_pad_distance_x(), tello.get_mission_pad_distance_y(), tello.get_mission_pad_distance_z, 10)