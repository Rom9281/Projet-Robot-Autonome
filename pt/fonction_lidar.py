from rplidar import RPLidar

def scan ():
    ret = []
    lidar = RPLidar('/dev/ttyUSB0')
    for i, scan in enumerate(lidar.iter_scans()):
        ret.append(scan)
        if i > 0:
            break

    lidar.stop()
    lidar.stop_motor()
    return ret