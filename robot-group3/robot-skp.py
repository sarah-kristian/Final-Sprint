
# Adapted from Created by Joseph C. Richardson, GitHub.com
# https://gist.github.com/ROBOMASTER-S1/c0486197ac7e8c6470774f548cd16de0

robot   = robot_ctrl
gimbal  = gimbal_ctrl
chassis = chassis_ctrl
vision  = vision_ctrl
led     = led_ctrl
define  = rm_define
gun     = gun_ctrl

drive_speed = 0.3
gimbal_speed = 30
gimbal_rotate = 90,180
l1,l2 = 0,255
seconds = 2

def scan_for_marker():

    vision.enable_detection(define.vision_detection_marker)
    vision.set_marker_detection_distance(1)

    robot.set_mode(define.robot_mode_chassis_follow)

    gimbal.set_rotate_speed(gimbal_speed)
    chassis.set_trans_speed(drive_speed)

    led.set_top_led(define.armor_top_all,l2,l2,l2,define.effect_always_on)
    led.set_bottom_led(define.armor_bottom_all,l2,l2,l2,define.effect_always_on)
    chassis.move(0)

    while True:
        vision.cond_wait(define.cond_recognized_marker_letter_F)
        vision.cond_wait(define.cond_recognized_marker_letter_D)
        vision.cond_wait(define.cond_recognized_marker_letter_P)
        vision.cond_wait(define.cond_recognized_marker_number_one)
        vision.cond_wait(define.cond_recognized_marker_number_two)
        vision.cond_wait(define.cond_recognized_marker_number_three)
        break


########################
# Vision Markers 1-3
########################


# Do something with gimbal and chassis
def vision_recognized_marker_number_one(msg):

    print("Found marker 1 ...")
    print("Doing something with gimbal and chassis ...")
    
    chassis.rotate_with_degree(define.anticlockwise, 90)
    chassis.rotate_with_degree(define.clockwise, 90)
    gimbal.yaw(250)
    gimbal.recenter()
    time.sleep(seconds)



# Do something with LED lights
def vision_recognized_marker_number_two(msg):
    print("Found marker 2 ...")
    print("Doing something with LED lights ...")

    led.set_bottom_led(define.armor_bottom_all,232, 235, 52,define.effect_always_on)#Changes LED lights to yellow
    led.set_top_led(define.armor_top_all,52, 235, 55,define.effect_always_on)#Changes LED lights to green


# Do something with gimbal and chassis AND LED lights
def vision_recognized_marker_number_three(msg):

    print("Found marker 3 ...")
    print("Doing something with gimbal and chassis ...")
    print("Doing something with LED lights ...")

    chassis.rotate_with_degree(define.anticlockwise, 90)
    chassis.rotate_with_degree(define.clockwise, 90)
    gimbal.yaw(250)
    gimbal.recenter()
    led.set_bottom_led(define.armor_bottom_all,232, 235, 52,define.effect_always_on) #Changes LED lights to yellow
    led.set_top_led(define.armor_top_all,52, 235, 55,define.effect_always_on) #Changes LED lights to green


########################
# Vision Markers F, (D & P to be fixed)
########################


# Put out Fire
def vision_recognized_marker_letter_F(msg):

    print("Found marker F ...")
    print("Aiming at marker F ...")
    print("Firing at marker F ...")
    print("Fire extinguished.")

    gun_ctrl.fire_once()
    time.sleep(seconds)
    chassis.stop()

    gimbal.rotate_with_degree(define.gimbal_right,gimbal_rotate[0])
    chassis.move(0)
    vision.disable_detection(define.vision_detection_marker)




########################
# Vision Markers for TESTING
########################

def vision_recognized_marker_letter_D(msg):
    print("Found marker D ...")
    print("Changing lights for a test")

    led.set_top_led(define.armor_top_all,l2,l2,l1,define.effect_always_on)
    led.set_bottom_led(define.armor_bottom_all,l2,l2,l1,define.effect_always_on)
    time.sleep(seconds)
    chassis.stop()

    gimbal.rotate_with_degree(define.gimbal_right,gimbal_rotate[0])
    chassis.move(0)

def vision_recognized_marker_letter_P(msg):
    print("Found marker P ...")
    print("Changing lights for a test")

    led.set_top_led(define.armor_top_all,l1,l1,l2,define.effect_always_on)
    led.set_bottom_led(define.armor_bottom_all,l1,l1,l2,define.effect_always_on)
    time.sleep(seconds)
    chassis.stop()

    gimbal.rotate_with_degree(define.gimbal_right,gimbal_rotate[0])
    chassis.move(0)



########################
# Movement functions
########################

def move_to_post_C():

    led.set_bottom_led(define.armor_bottom_all, 255, 255, 255, define.effect_always_on)  # Changes LED lights to white
    led.set_top_led(define.armor_top_all, 255, 255, 255, define.effect_always_on)  # Changes LED lights to white
    chassis.move_with_distance(0, 5)
    chassis.move_with_distance(0, 1.78)



########################
# Main program
########################

def start():

    robot.set_mode(define.robot_mode_free)

    chassis.set_trans_speed(0.6)

    move_to_post_C()
    scan_for_marker()
    print("Mission complete.")


if __name__ == "__main__":
    start()