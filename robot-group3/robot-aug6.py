import time 


# LED "Rock out" Function

def rockout():

    robot_ctrl.set_mode(rm_define.robot_mode_free)

    chassis_ctrl.set_rotate_speed(120)

    gimbal_ctrl.set_rotate_speed(120)

    led_ctrl.set_flash(rm_define.armor_all, 4)

    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, rm_define.effect_marquee)

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_flash)

    led_ctrl.gun_led_on()

    for i in range(2):

        gimbal_ctrl.rotate(rm_define.gimbal_right)

        chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 0.3)

        gimbal_ctrl.rotate(rm_define.gimbal_left)

        chassis_ctrl.rotate_with_time(rm_define.clockwise, 0.6)

        gimbal_ctrl.rotate(rm_define.gimbal_right)

        chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 0.3)

    led_ctrl.turn_off(rm_define.armor_all)

    led_ctrl.gun_led_off()

    gimbal_ctrl.stop()

    chassis_ctrl.stop()

    gimbal_ctrl.recenter()



def scan_for_marker():

    print("Scanning for marker ...")

    vision_ctrl.enable_detection(rm_define.vision_detection_marker)

    #chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    #gimbal_ctrl.recenter()

    gimbal_ctrl.yaw_ctrl(-90)

    gimbal_ctrl.yaw_ctrl(+180)

    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)




def vision_recognized_marker_letter_F(msg):

    print("Found marker F ...")

    vision_ctrl.disable_detection(rm_define.vision_detection_marker)

    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)

    gun_ctrl.fire_once()




def vision_recognized_marker_letter_D(msg):

    print("Found marker D ...")

    vision_ctrl.disable_detection(rm_define.vision_detection_marker)

    vision_ctrl.detect_marker(rm_define.marker_letter_D)






def vision_recognized_marker_letter_P(msg):

    print("Found marker P ...")

    vision_ctrl.disable_detection(rm_define.vision_detection_marker)

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 255, 0, rm_define.effect_always_on)  # Changes LED lights to yellow

    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 255, 0, rm_define.effect_always_on)  # Changes LED lights to yellow   

    if current_post == "C":

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 0.21)

        # Return

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 0.21)

    elif current_post == "E":

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 3.99)

        time.sleep(5)

            # return

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 3.99)

        time.sleep(5)

    elif current_post == "G":

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 3.32)

        time.sleep(5)

            # return

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 5)

        chassis_ctrl.move_with_distance(0, 3.32)

        time.sleep(5)


def vision_recognized_marker_number_one(msg):

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

        gimbal_ctrl.yaw_ctrl(250)

        gimbal_ctrl.recenter()

        #Lights

def vision_recognized_marker_number_two(msg):

        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,232, 235, 52,rm_define.effect_always_on)#Changes LED lights to yellow

        led_ctrl.set_top_led(rm_define.armor_top_all,52, 235, 55,rm_define.effect_always_on)#Changes LED lights to green

        #All 3

def vision_recognized_marker_number_three(msg):

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

        gimbal_ctrl.yaw_ctrl(250)

        gimbal_ctrl.recenter()

        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,232, 235, 52,rm_define.effect_always_on)#Changes LED lights to yellow

        led_ctrl.set_top_led(rm_define.armor_top_all,52, 235, 55,rm_define.effect_always_on)#Changes LED lights to green






# Move to Reset Point B

def move_to_reset_point_B():

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_always_on)  # Changes LED lights to green

    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, rm_define.effect_always_on)  # Changes LED lights to green

    chassis_ctrl.move_with_distance(0, 5)

    chassis_ctrl.move_with_distance(0, 0.8)

    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    chassis_ctrl.move_with_distance(0, 0.81)

    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    chassis_ctrl.move_with_distance(0, 0.38)

    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    chassis_ctrl.move_with_distance(0, 1.68)

    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    chassis_ctrl.move_with_distance(0, 0.46)

    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    chassis_ctrl.move_with_distance(0, 0.54)

    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)

    chassis_ctrl.move_with_distance(0, 1.5)

    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)

    chassis_ctrl.move_with_distance(0, 0.52)

    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    chassis_ctrl.move_with_distance(0, 0.85)

    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    chassis_ctrl.move_with_distance(0, 0.4)

    time.sleep(5)  # Reset point

# Move to Post C

def move_to_post_C():

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 255, 255, rm_define.effect_always_on)  # Changes LED lights to white

    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 255, 255, rm_define.effect_always_on)  # Changes LED lights to white

    chassis_ctrl.move_with_distance(0, 5)

    chassis_ctrl.move_with_distance(0, 1.78)

    scan_for_marker()

# Move to Reset Point D

def move_to_reset_point_D():

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 165, 0, rm_define.effect_always_on)  # Changes LED lights to orange

    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 165, 0, rm_define.effect_always_on)  # Changes LED lights to orange

    chassis_ctrl.move_with_distance(0, 4.89)

    time.sleep(5)  # Reset point

# Move to Post E

def move_to_post_E():

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 128, 0, 128, rm_define.effect_always_on)  # Changes LED lights to light purple

    led_ctrl.set_top_led(rm_define.armor_top_all, 128, 0, 128, rm_define.effect_always_on)  # Changes LED lights to light purple

    chassis_ctrl.move_with_distance(0, 4.14)

    scan_for_marker()


# Move to Reset Point F

def move_to_reset_point_F():

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 218, 185, rm_define.effect_always_on)  # Changes LED lights to peach

    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 218, 185, rm_define.effect_always_on)  # Changes LED lights to peach

    chassis_ctrl.move_with_distance(0, 4.61)  # Adjust as needed

    # number 1,2 and 3

    time.sleep(5)  # Reset point

# Move to Post G

def move_to_post_G():

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 192, 203, rm_define.effect_always_on)  # Changes LED lights to pink

    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 192, 203, rm_define.effect_always_on)  # Changes LED lights to pink

    chassis_ctrl.move_with_distance(0, 4.46)

    scan_for_marker()


# Move to Reset Point H

def move_to_reset_point_H():

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_always_on)  # Changes LED lights to blue

    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_always_on)  # Changes LED lights to blue

    chassis_ctrl.move_with_distance(0, 5)

    chassis_ctrl.move_with_distance(0, 0.66)

    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)

    time.sleep(5)  # Reset point

# Move back to reset point D from H

def move_back_to_reset_point_D():

    chassis_ctrl.move_with_distance(0, 5)

    chassis_ctrl.move_with_distance(0, 5)

    chassis_ctrl.move_with_distance(0, 5)

    chassis_ctrl.move_with_distance(0, 3.80)

    rockout()

    time.sleep(5)

# Return to Start Point A from Reset Point D

def move_back_to_start_A():

    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 255, rm_define.effect_flash)  # Changes LED lights to flashing purple

    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 255, rm_define.effect_flash)  # Changes LED lights to flashing purple

    chassis_ctrl.move_with_distance(0, 5)

    chassis_ctrl.move_with_distance(0, 5)

    chassis_ctrl.move_with_distance(0, 5)

    chassis_ctrl.move_with_distance(0, 5)

    chassis_ctrl.move_with_distance(0, 0.27)

    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)

    time.sleep(5)



# Starting Function

def start():

    robot_ctrl.set_mode(rm_define.robot_mode_free)

    chassis_ctrl.set_trans_speed(0.6)

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


if __name__ == "__main__":
    start()
 