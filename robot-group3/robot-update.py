#Robot Project - Group 3
 
#Fire Gun Once
def handle_fire():
    # Fire the gun
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255, 0, 0,rm_define.effect_always_on)#Changes LED lights to red
    led_ctrl.set_top_led(rm_define.armor_top_all,255, 0, 0,rm_define.effect_always_on)#Changes LED lights to red
    gun_ctrl.fire_once()
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
 
#Handle Danger and Continue
def handle_danger():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255, 0, 0,rm_define.effect_always_on)#Changes LED lights to red
    led_ctrl.set_top_led(rm_define.armor_top_all,255, 0, 0,rm_define.effect_always_on)#Changes LED lights to red
    # Skip the post and continue
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
 

#Move to Safety
def move_to_safety():
    # Move back to A (reverse the path)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255, 255, 0,rm_define.effect_always_on)#Changes LED lights to yellow
    led_ctrl.set_top_led(rm_define.armor_top_all,255, 255, 0,rm_define.effect_always_on)#Changes LED Lights to yellow
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    chassis_ctrl.move_with_distance(0, 2.74)
    chassis_ctrl.move_with_distance(0, 2.74)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 0.8)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 2.74)
    chassis_ctrl.move_with_distance(0, 2.74)



#Move to Start Point(A)
def return_to_start_A():
     chassis_ctrl.move_with_distance(0, 5)
     chassis_ctrl.move_with_distance(0, 5)
     chassis_ctrl.move_with_distance(0, 5)
     chassis_ctrl.move_with_distance(0, 5)
     chassis_ctrl.move_with_distance(0, 5)
     chassis_ctrl.move_with_distance(0, 5)
     chassis_ctrl.move_with_distance(0, 5)
     chassis_ctrl.move_with_distance(0, 4.5)
     time.sleep(5)
 
def move_back_to_start_A():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 0.27)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    gimbal_ctrl.rotate(rm_define.gimbal_up)
    gimbal_ctrl.rotate(rm_define.gimbal_down)
    gimbal_ctrl.rotate(rm_define.gimbal_left)
    gimbal_ctrl.rotate(rm_define.gimbal_right)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,69,215,255,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,69,215,255,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,69,215,255,rm_define.effect_flash)
    time.sleep(5)
 

#Retrun to Start
def return_to_post():
    # Return to the original post (simplified for example purposes)
    move_to_reset_point_C()  # Assuming we are at post C, adjust for other posts 



#Handle Person
def handle_person():
    # Locate the person and take to safety (Back to A)
    move_to_safety()
    return_to_post()
 

 
# #Scan and Hnadle Markers
# def scan_and_handle_marker():
#     # Enable vision detection for markers
#     vision_ctrl.enable_detection(rm_define.vision_detection_marker)
#     gimbal_ctrl.yaw_ctrl(-90)
#     gimbal_ctrl.yaw_ctrl(90)
 
#     # Detect and handle markers
#     if vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F):
#         handle_fire()
#     elif vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_D):
#         handle_danger()
#     elif vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_P):
#         handle_person()
 
 #Scan and Handle Markers at different posts
def scan_and_handle_marker_at(post):
    # Detect and handle marker P
    if vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_P):
        if post == "C":
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 0.21)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 0.21)

        elif post == "E":
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 3.99)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 3.99)


        elif post == "G":
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 3.32)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 3.32)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

    elif vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F):
        handle_fire()
    elif vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_D):
        handle_danger()

 
#Move to Reset Point B
def move_to_reset_point_B():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0, 255, 0,rm_define.effect_always_on)#Changes LED lights to green
    led_ctrl.set_top_led(rm_define.armor_top_all,0, 255, 0,rm_define.effect_always_on)#Changes LED Lights to green
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
    
#Move to Reset Point C
def move_to_reset_point_C():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255, 255, 255,rm_define.effect_always_on)#Changes LED lights to white
    led_ctrl.set_top_led(rm_define.armor_top_all,255, 255, 255,rm_define.effect_always_on)#Changes LED Lights to white
    #chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 1.71)
 
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    # Scan the area by rotating the gimbal
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(90)

    scan_and_handle_marker_at("C")
    
 
#Move to Reset Point D
def move_to_reset_point_D():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255, 165, 0,rm_define.effect_always_on)#Changes LED lights to orange
    led_ctrl.set_top_led(rm_define.armor_top_all,255, 165, 0,rm_define.effect_always_on)#Changes LED Lights to orange
    chassis_ctrl.move_with_distance(0, 4.89)
    time.sleep(5)  # Reset point
    
 
#Move to Post E
def move_to_post_E():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,128, 0, 128,rm_define.effect_always_on)#Changes LED lights to light purple
    led_ctrl.set_top_led(rm_define.armor_top_all,0, 128, 0,rm_define.effect_always_on)#Changes LED Lights to light purple
    chassis_ctrl.move_with_distance(0, 4.14)
 
    # Scan the area by rotating the gimbal
    scan_and_handle_marker_at("E")

 
 #Move to Reset Point F
def move_to_reset_point_F():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255, 218, 185,rm_define.effect_always_on)#Changes LED lights to peach
    led_ctrl.set_top_led(rm_define.armor_top_all,255, 218, 185,rm_define.effect_always_on)#Changes LED Lights to peach
    # Add the correct movement logic to move to reset point F
    chassis_ctrl.move_with_distance(0, 4.61)  # Placeholder values, adjust as needed
    time.sleep(5)  # Reset point
    
 
#Move to Post G
def move_to_post_G():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255, 192, 203,rm_define.effect_always_on)#Changes LED lights to pink
    led_ctrl.set_top_led(rm_define.armor_top_all,255, 192, 203,rm_define.effect_always_on)#Changes LED Lights to pink
    chassis_ctrl.move_with_distance(0, 4.46)  
    #Scan for Markers
    scan_and_handle_marker_at(G)

 
#Move to Reset Point H
def move_to_reset_point_H():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 0.66)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    time.sleep(5)  # Reset point
 
def move_back_to_reset_point_D():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 3.80)
    time.sleep(5)
 

 # LED "Rock out" Function we found on GitHub
def rockout():

    robot=robot_ctrl
    gimbal=gimbal_ctrl
    chassis=chassis_ctrl
    media=media_ctrl
    led=led_ctrl
    define=rm_define
    
    l1,l2=0,255
 
    robot.set_mode(define.robot_mode_free)
    
    chassis.set_rotate_speed(120)
    gimbal.set_rotate_speed(120)
 
    led.set_flash(define.armor_all,4)
    led.set_top_led(define.armor_top_all,l1,l2,l1,define.effect_marquee)
    led.set_bottom_led(define.armor_bottom_all,l1,l2,l1,define.effect_flash)
    led.gun_led_on()
 
    for i in range(2):
        gimbal.rotate(define.gimbal_right)
        chassis.rotate_with_time(define.anticlockwise,0.3)
        gimbal.rotate(define.gimbal_left)
        chassis.rotate_with_time(define.clockwise,0.6)
        gimbal.rotate(define.gimbal_right)
        chassis.rotate_with_time(define.anticlockwise,0.3)
 
    led.turn_off(define.armor_all)
    led.gun_led_off();gimbal.stop()
    chassis.stop();gimbal.recenter()
 
#Starting Function
def start():
    # Set the robot to free mode
    robot_ctrl.set_mode(rm_define.robot_mode_free)
 
    # Set translation speed
    chassis_ctrl.set_trans_speed(0.5)
 
    # Move to reset point B
    move_to_reset_point_B()
 
 
    # Move to Post C and check the marker
    move_to_reset_point_C()
   
 
    # Move to reset point D
    move_to_reset_point_D()
 
    # Move to Post E and check the marker
    move_to_post_E()
    
    # Move to reset point F
    move_to_reset_point_F()
 
    # Move to Post G and check the marker
    move_to_post_G()
 
    # Move to reset point H
    move_to_reset_point_H()
 
    #Turn around and go to D
    move_back_to_reset_point_D()
 
    #Rockout Function at D
    rockout()
 
    # Return to start position A
    return_to_start_A()
 
 

 
#Call Necessary Functions and Begin Program
def main():
    start()
    rockout()

if __name__ == "__main__":
    main()