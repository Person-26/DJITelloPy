from djitellopy import Tello
from examples import objectdetection
import cv2

tello = Tello()
tello.connect()

# 100 points find and pop baloon
tello.stream_on()
move = 1
direction = "forward"
while len(objectdetection(tello.get_frame_read().frame)) <= 0:
    match direction:
        case"forward":
            for i in range(move):
                tello.move_forward(10)
                direction = "left"
                if len(objectdetection(tello.get_frame_read().frame)) > 0:
                    break
        case "left":
            for i in range(move):
                tello.move_left(10)
                direction = "back"
                move += 1
                if len(objectdetection(tello.get_frame_read().frame)) > 0:
                    break
        case "back":
            for i in range(move):
                tello.move_forward(10)
                direction = "right"
                if len(objectdetection(tello.get_frame_read().frame)) > 0:
                    break
        case "right":
            for i in range(move):
                tello.move_right(10)
                direction = "forward"
                move += 1
                if len(objectdetection(tello.get_frame_read().frame)) > 0:
                    break
cv2.imwrite("picture.png", tello.get_frame_read().frame)

while len(objectdetection(tello.get_frame_read().frame)) > 0:
    while objectdetection(tello.get_frame_read().frame)[0][0] < 290 or objectdetection(tello.get_frame_read().frame)[0][0] > 310 or objectdetection(tello.get_frame_read().frame)[0][1] < 290 or objectdetection(tello.get_frame_read().frame)[0][0] > 310:
        if objectdetection(tello.get_frame_read().frame)[0][0] < 290:
                tello.rotate_clockwise(1)
        if objectdetection(tello.get_frame_read().frame)[0][0] > 310:
                tello.rotate_counter_clockwise(1)
        if objectdetection(tello.get_frame_read().frame)[0][1] < 290:
            tello.move_down(20)
        if objectdetection(tello.get_frame_read().frame)[0][1] > 310:
            tello.move_up(20)
    tello.move_forward(20)
tello.land()

tello.enable_mission_pads()
tello.takeoff()
angle = 0
for i in range(4):
    while tello.get_mission_pad() != i:
        tello.rotate_clockwise(1)
        angle += 1
    while tello.get_mission_pad_distance_y() < -3:
        tello.rotate_clockwise(1)
        angle += 1
    while tello.get_mission_pad_distance_y() > 3:
        tello.rotate_counter_clockwise(1)
        angle -= 1
    print(angle)
tello.land()