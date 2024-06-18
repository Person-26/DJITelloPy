from djitellopy import Tello
from examples import objectdetection
from examples.pathfinder import pathfinder

tello = Tello()
tello.connect()

# 50 points draw tag
tello.takeoff()
id = tello.get_mission_pad_id()
match int(id / 10):
    case 1:
        tello.go_xyz_speed(10, 10, 0, 10)
        tello.go_xyz_speed(0, -100, 0, 10)
        tello.go_xyz_speed(10, 0, 0, 10)
        tello.go_xyz_speed(-20, 0, 0, 10)
    case 2:
        tello.curve_xyz_speed(50, 50, 0, 100, 0, 0, 10)
        tello.go_xyz_speed(-50, 50, 0, 10)
        tello.go_xyz_speed(100, 0, 0, 10)
    case 3:
        tello.curve_xyz_speed(50, -50, 0, 0, -100, 0, 10)
        tello.curve_xyz_speed(50, -50, 0, 0, -100, 0, 10)
    case 4:
        tello.go_xyz_speed(0, 100, 0, 10)
        tello.go_xyz_speed(-50, -50, 0, 10)
        tello.go_xyz_speed(100, 0, 0, 10)
    case 5:
        tello.go_xyz_speed(-50, 0, 0, 10)
        tello.go_xyz_speed(0, 25, 0, 10)
        tello.curve_xyz_speed(25, -25, 0, 0, 50, 0, 10)
    case 6:
        tello.curve_xyz_speed(-25, -50, 0, 0, -100, 0, 10)
        tello.curve_xyz_speed(25, 25, 0, -25, 50, 0, 10)
    case 7:
        tello.go_xyz_speed(50, 0, 0, 10)
        tello.go_xyz_speed(-50, 100, 0, 10)
    case 8:
        tello.curve_xyz_speed(25, -25, 0, 0, -50, 0, 10)
        tello.curve_xyz_speed(-25, -25, 0, 0, -50, 0, 10)
        tello.curve_xyz_speed(25, 25, 0, 0, 50, 0, 10)
        tello.curve_xyz_speed(-25, 25, 0, 0, 50, 0, 10)
    case 9:
        tello.curve_xyz_speed(25, 50, 0, 0, 100, 0, 10)
        tello.curve_xyz_speed(-25, -25, 0, 25, -50, 0, 10)
tello.move_right(100)
match id % 10:
    case 0:
        tello.curve_xyz_speed(50, 100, 0, 0, 200, 0, 10)
        tello.curve_xyz_speed(-50, -100, 0, 0, -200, 0, 10)
    case 1:
        tello.go_xyz_speed(10, 10, 0, 10)
        tello.go_xyz_speed(0, -100, 0, 10)
        tello.go_xyz_speed(10, 0, 0, 10)
        tello.go_xyz_speed(-20, 0, 0, 10)
    case 2:
        tello.curve_xyz_speed(50, 50, 0, 100, 0, 0, 10)
        tello.go_xyz_speed(-50, 50, 0, 10)
        tello.go_xyz_speed(100, 0, 0, 10)
    case 3:
        tello.curve_xyz_speed(50, -50, 0, 0, -100, 0, 10)
        tello.curve_xyz_speed(50, -50, 0, 0, -100, 0, 10)
    case 4:
        tello.go_xyz_speed(0, 100, 0, 10)
        tello.go_xyz_speed(-50, -50, 0, 10)
        tello.go_xyz_speed(100, 0, 0, 10)
    case 5:
        tello.go_xyz_speed(-50, 0, 0, 10)
        tello.go_xyz_speed(0, 25, 0, 10)
        tello.curve_xyz_speed(25, -25, 0, 0, 50, 0, 10)
    case 6:
        tello.curve_xyz_speed(-25, -50, 0, 0, -100, 0, 10)
        tello.curve_xyz_speed(25, 25, 0, -25, 50, 0, 10)
    case 7:
        tello.go_xyz_speed(50, 0, 0, 10)
        tello.go_xyz_speed(-50, 100, 0, 10)
    case 8:
        tello.curve_xyz_speed(25, -25, 0, 0, -50, 0, 10)
        tello.curve_xyz_speed(-25, -25, 0, 0, -50, 0, 10)
        tello.curve_xyz_speed(25, 25, 0, 0, 50, 0, 10)
        tello.curve_xyz_speed(-25, 25, 0, 0, 50, 0, 10)
    case 9:
        tello.curve_xyz_speed(25, 50, 0, 0, 100, 0, 10)
        tello.curve_xyz_speed(-25, -25, 0, 25, -50, 0, 10)
tello.land()

# 50 points traveling salesman

waypoints = [[]]
relative_position = [0,0,0]

tello.takeoff()
for waypoint in pathfinder(waypoints):
    tello.go_xyz_speed(waypoint[0] - relative_position[0], waypoint[1] - relative_position[1], waypoint[2] - relative_position[2], 10)
    relative_position[0] = waypoint[0]
    relative_position[2] = waypoint[2]
    relative_position[3] = waypoint[3]
tello.land()

# 50 point detect tennis balls
tello.takeoff()
print(len(objectdetection()))
tello.land()

# 50 point search for mission pad
tello.takeoff()
# searching for mission pad
move = 1
pad = 5
direction = "forward"
while tello.get_mission_pad() != pad:
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
for i in range(pad):
    tello.flip_forward()
