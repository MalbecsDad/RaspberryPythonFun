from sense_hat import SenseHat
import time

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

sense = SenseHat()

sense.set_imu_config(True, True, True)

while True:
    orientation = sense.get_orientation()

    if(orientation["pitch"] > 180):
        mod_pitch = 360 - orientation["pitch"]
    else:
        mod_pitch = orientation["pitch"]

    if(orientation["roll"] > 180):
        mod_roll = 360 - orientation["roll"]
    else:
        mod_roll = orientation["roll"]

    if(orientation["yaw"] > 180):
        mod_yaw = 360 - orientation["yaw"]
    else:
        mod_yaw = orientation["yaw"]

    pitch_colour = (-205/180)*mod_pitch+255
    roll_colour = (-205/180)*mod_roll+255
    yaw_colour = (-205/180)*mod_yaw+255

    red_colour = clamp(int(round(pitch_colour)),0,255)
    green_colour = clamp(int(round(roll_colour)),0,255)
    blue_colour = clamp(int(round(yaw_colour)),0,255)

    sense.clear(red_colour, green_colour, blue_colour)


    
