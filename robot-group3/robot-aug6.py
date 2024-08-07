import time 

# define global variables
robot = robot_ctrl
gimbal = gimbal_ctrl
chassis = chassis_ctrl
media = media_ctrl
led = led_ctrl
define = rm_define
vision = vision_ctrl
gun = gun_ctrl
yaw = yaw_ctrl



# LED "Rock out" Function

def rockout():

    robot.set_mode(define.robot_mode_free)

    chassis.set_rotate_speed(120)

    gimbal.set_rotate_speed(120)

    led.set_flash(define.armor_all, 4)

    led.set_top_led(define.armor_top_all, 0, 255, 0, define.effect_marquee)

    led.set_bottom_led(define.armor_bottom_all, 0, 255, 0, define.effect_flash)

    led.gun_led_on()

    for i in range(2):

        gimbal.rotate(define.gimbal_right)

        chassis.rotate_with_time(define.anticlockwise, 0.3)

        gimbal.rotate(define.gimbal_left)

        chassis.rotate_with_time(define.clockwise, 0.6)

        gimbal.rotate(define.gimbal_right)

        chassis.rotate_with_time(define.anticlockwise, 0.3)

    led.turn_off(define.armor_all)

    led.gun_led_off()

    gimbal.stop()

    chassis.stop()

    gimbal.recenter()



def scan_for_marker(post):

    _post = post

    print("Scanning for marker ...")

    vision.enable_detection(define.vision_detection_marker)

    #chassis.rotate_with_degree(define.anticlockwise, 90)

    #gimbal.recenter()

    gimbal.yaw(-90)

    gimbal.yaw(+180)

    chassis.rotate_with_degree(define.clockwise, 90)




def vision_recognized_marker_letter_F(msg):

    print("Found marker F ...")

    vision.disable_detection(define.vision_detection_marker)

    vision.detect_marker_and_aim(define.marker_letter_F)

    gun.fire_once()





def vision_recognized_marker_letter_D(msg):

    print("Found marker D ...")

    vision.disable_detection(define.vision_detection_marker)

    vision.detect_marker(define.marker_letter_D)






def vision_recognized_marker_letter_P(msg):

    print("Found marker P ...")

    vision.disable_detection(define.vision_detection_marker)

    led.set_bottom_led(define.armor_bottom_all, 255, 255, 0, define.effect_always_on)  # Changes LED lights to yellow

    led.set_top_led(define.armor_top_all, 255, 255, 0, define.effect_always_on)  # Changes LED lights to yellow   

    if _post == "C":

        chassis.rotate_with_degree(define.anticlockwise, 180)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 0.21)

        # Return

        chassis.rotate_with_degree(define.anticlockwise, 180)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 0.21)

    elif _post == "E":

        chassis.rotate_with_degree(define.anticlockwise, 180)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 3.99)

        time.sleep(5)

            # return

        chassis.rotate_with_degree(define.anticlockwise, 180)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 3.99)

        time.sleep(5)

    elif _post == "G":

        chassis.rotate_with_degree(define.anticlockwise, 180)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 3.32)

        time.sleep(5)

            # return

        chassis.rotate_with_degree(define.anticlockwise, 180)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 5)

        chassis.move_with_distance(0, 3.32)

        time.sleep(5)


def vision_recognized_marker_number_one(msg):

        chassis.rotate_with_degree(define.anticlockwise, 90)

        chassis.rotate_with_degree(define.clockwise, 90)

        gimbal.yaw(250)

        gimbal.recenter()

        #Lights

def vision_recognized_marker_number_two(msg):

        led.set_bottom_led(define.armor_bottom_all,232, 235, 52,define.effect_always_on)#Changes LED lights to yellow

        led.set_top_led(define.armor_top_all,52, 235, 55,define.effect_always_on)#Changes LED lights to green

        #All 3

def vision_recognized_marker_number_three(msg):

        chassis.rotate_with_degree(define.anticlockwise, 90)

        chassis.rotate_with_degree(define.clockwise, 90)

        gimbal.yaw(250)

        gimbal.recenter()

        led.set_bottom_led(define.armor_bottom_all,232, 235, 52,define.effect_always_on)#Changes LED lights to yellow

        led.set_top_led(define.armor_top_all,52, 235, 55,define.effect_always_on)#Changes LED lights to green






# Move to Reset Point B

def move_to_reset_point_B():

    led.set_bottom_led(define.armor_bottom_all, 0, 255, 0, define.effect_always_on)  # Changes LED lights to green

    led.set_top_led(define.armor_top_all, 0, 255, 0, define.effect_always_on)  # Changes LED lights to green

    chassis.move_with_distance(0, 5)

    chassis.move_with_distance(0, 0.8)

    chassis.rotate_with_degree(define.anticlockwise, 90)

    chassis.move_with_distance(0, 0.81)

    chassis.rotate_with_degree(define.clockwise, 90)

    chassis.move_with_distance(0, 0.38)

    chassis.rotate_with_degree(define.clockwise, 90)

    chassis.move_with_distance(0, 1.68)

    chassis.rotate_with_degree(define.anticlockwise, 90)

    chassis.move_with_distance(0, 0.46)

    chassis.rotate_with_degree(define.anticlockwise, 90)

    chassis.move_with_distance(0, 0.54)

    chassis.rotate_with_degree(define.clockwise, 45)

    chassis.move_with_distance(0, 1.5)

    chassis.rotate_with_degree(define.clockwise, 45)

    chassis.move_with_distance(0, 0.52)

    chassis.rotate_with_degree(define.clockwise, 90)

    chassis.move_with_distance(0, 0.85)

    chassis.rotate_with_degree(define.anticlockwise, 90)

    chassis.move_with_distance(0, 0.4)

    time.sleep(5)  # Reset point

# Move to Post C

def move_to_post_C():

    led.set_bottom_led(define.armor_bottom_all, 255, 255, 255, define.effect_always_on)  # Changes LED lights to white

    led.set_top_led(define.armor_top_all, 255, 255, 255, define.effect_always_on)  # Changes LED lights to white

    chassis.move_with_distance(0, 5)

    chassis.move_with_distance(0, 1.78)

    current_post = "C"

    scan_for_marker("C")

# Move to Reset Point D

def move_to_reset_point_D():

    led.set_bottom_led(define.armor_bottom_all, 255, 165, 0, define.effect_always_on)  # Changes LED lights to orange

    led.set_top_led(define.armor_top_all, 255, 165, 0, define.effect_always_on)  # Changes LED lights to orange

    chassis.move_with_distance(0, 4.89)

    time.sleep(5)  # Reset point

# Move to Post E

def move_to_post_E():

    led.set_bottom_led(define.armor_bottom_all, 128, 0, 128, define.effect_always_on)  # Changes LED lights to light purple

    led.set_top_led(define.armor_top_all, 128, 0, 128, define.effect_always_on)  # Changes LED lights to light purple

    chassis.move_with_distance(0, 4.14)
    
    current_post = "E"

    scan_for_marker("E")


# Move to Reset Point F

def move_to_reset_point_F():

    led.set_bottom_led(define.armor_bottom_all, 255, 218, 185, define.effect_always_on)  # Changes LED lights to peach

    led.set_top_led(define.armor_top_all, 255, 218, 185, define.effect_always_on)  # Changes LED lights to peach

    chassis.move_with_distance(0, 4.61)  # Adjust as needed

    # number 1,2 and 3

    time.sleep(5)  # Reset point

# Move to Post G

def move_to_post_G():

    led.set_bottom_led(define.armor_bottom_all, 255, 192, 203, define.effect_always_on)  # Changes LED lights to pink

    led.set_top_led(define.armor_top_all, 255, 192, 203, define.effect_always_on)  # Changes LED lights to pink

    chassis.move_with_distance(0, 4.46)

    current_post = "G"

    scan_for_marker("G")


# Move to Reset Point H

def move_to_reset_point_H():

    led.set_bottom_led(define.armor_bottom_all, 0, 0, 255, define.effect_always_on)  # Changes LED lights to blue

    led.set_top_led(define.armor_top_all, 0, 0, 255, define.effect_always_on)  # Changes LED lights to blue

    chassis.move_with_distance(0, 5)

    chassis.move_with_distance(0, 0.66)

    chassis.rotate_with_degree(define.clockwise, 180)

    time.sleep(5)  # Reset point

# Move back to reset point D from H

def move_back_to_reset_point_D():

    chassis.move_with_distance(0, 5)

    chassis.move_with_distance(0, 5)

    chassis.move_with_distance(0, 5)

    chassis.move_with_distance(0, 3.80)

    rockout()

    time.sleep(5)

# Return to Start Point A from Reset Point D

def move_back_to_start_A():

    led.set_bottom_led(define.armor_bottom_all, 255, 0, 255, define.effect_flash)  # Changes LED lights to flashing purple

    led.set_top_led(define.armor_top_all, 255, 0, 255, define.effect_flash)  # Changes LED lights to flashing purple

    chassis.move_with_distance(0, 5)

    chassis.move_with_distance(0, 5)

    chassis.move_with_distance(0, 5)

    chassis.move_with_distance(0, 5)

    chassis.move_with_distance(0, 0.27)

    chassis.rotate_with_degree(define.anticlockwise, 180)

    time.sleep(5)



# Starting Function

def start():

    robot.set_mode(define.robot_mode_free)

    chassis.set_trans_speed(0.6)

#    move_to_reset_point_B()

    scan_for_marker()

    move_to_post_C()

    move_to_reset_point_D()

    move_to_post_E()

    move_to_reset_point_F()

    move_to_post_G()

    move_to_reset_point_H()

    # The Return

    move_back_to_reset_point_D()

    move_back_to_start_A()


# Call Necessary Functions and Begin Program


# Registering Vision Marker Event Handlers
vision.set_marker_detection_callback(define.marker_letter_F, vision_recognized_marker_letter_F)
vision.set_marker_detection_callback(define.marker_letter_D, vision_recognized_marker_letter_D)
vision.set_marker_detection_callback(define.marker_letter_P, vision_recognized_marker_letter_P)
vision.set_marker_detection_callback(define.marker_number_one, vision_recognized_marker_number_one)
vision.set_marker_detection_callback(define.marker_number_two, vision_recognized_marker_number_two)
vision.set_marker_detection_callback(define.marker_number_three, vision_recognized_marker_number_three)



if __name__ == "__main__":
    start()
 