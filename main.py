from pioneer_sdk import Pioneer
from time import sleep

mini = Pioneer()
poits = [
    (0, 0, 1, 0),
    (0, 3, 1, 0),
    (3, 3, 1, 0),
    (3, 0, 1, 0),
    (0, 0, 1, 0)
]
if __name__ == "__main__":
    mini.arm()
    mini.takeoff()
    for i in range(5):
        x, y, z, yaw = poits[i]
        mini.go_to_local_point(x, y, z, yaw)
        while mini.point_reached():
            pass
    mini.land()
    mini.disarm()