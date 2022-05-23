from rplidar import RPLidar

def scan ():
    ret = []
    lidar = RPLidar('COM8')
    for i, scan in enumerate(lidar.iter_scans()):
        ret.append(scan)
        if i > 0:
            break

    lidar.stop()
    lidar.stop_motor()
    return ret

def stop():
    lidar = RPLidar('/dev/ttyUSB1')
    lidar.stop()
    lidar.stop_motor()