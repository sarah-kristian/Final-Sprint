#Robot Project - Group 3
 
# define global variables to simplify the code
robot = robot_ctrl
yaw = yaw_ctrl
gimbal = gimbal_ctrl
chassis = chassis_ctrl
media = media_ctrl
led = led_ctrl
define = define
gun = gun_ctrl
vision = vision_ctrl



# Define Actions for the Robot to Perform
##########################################

# LED "Rock out" Function we found on GitHub
def rockout():
    
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


#Fire Gun Once
def handle_fire():
    # Fire the gun
    led.set_bottom_led(define.armor_bottom_all,255, 0, 0,define.effect_always_on)#Changes LED lights to red
    led.set_top_led(define.armor_top_all,255, 0, 0,define.effect_always_on)#Changes LED lights to red
    gun.fire_once()
    vision.disable_detection(define.vision_detection_marker)
 
#Handle Danger and Continue
def handle_danger():
    led.set_bottom_led(define.armor_bottom_all,255, 0, 0,define.effect_always_on)#Changes LED lights to red
    led.set_top_led(define.armor_top_all,255, 0, 0,define.effect_always_on)#Changes LED lights to red
    # Skip the post and continue
    vision.disable_detection(define.vision_detection_marker)
 

#Move to Safety
def move_to_safety():
    # Move back to A (reverse the path)
    led.set_bottom_led(define.armor_bottom_all,255, 255, 0,define.effect_always_on)#Changes LED lights to yellow
    led.set_top_led(define.armor_top_all,255, 255, 0,define.effect_always_on)#Changes LED Lights to yellow
    chassis.rotate_with_degree(define.clockwise, 180)
    chassis.move_with_distance(0, 2.74)
    chassis.move_with_distance(0, 2.74)
    chassis.rotate_with_degree(define.anticlockwise, 90)
    chassis.move_with_distance(0, 0.8)
    chassis.rotate_with_degree(define.clockwise, 90)
    chassis.move_with_distance(0, 2.74)
    chassis.move_with_distance(0, 2.74)




#Move to Start Point(A)
def return_to_start_A():
     chassis.move_with_distance(0, 5)
     chassis.move_with_distance(0, 5)
     chassis.move_with_distance(0, 5)
     chassis.move_with_distance(0, 5)
     chassis.move_with_distance(0, 5)
     chassis.move_with_distance(0, 5)
     chassis.move_with_distance(0, 5)
     chassis.move_with_distance(0, 4.5)
     time.sleep(5)
 
def move_back_to_start_A():
    chassis.move_with_distance(0, 5)
    chassis.move_with_distance(0, 5)
    chassis.move_with_distance(0, 5)
    chassis.move_with_distance(0, 5)
    chassis.move_with_distance(0, 0.27)
    chassis.rotate_with_degree(define.anticlockwise, 180)
    chassis.rotate_with_degree(define.clockwise, 180)
    gimbal.rotate(define.gimbal_up)
    gimbal.rotate(define.gimbal_down)
    gimbal.rotate(define.gimbal_left)
    gimbal.rotate(define.gimbal_right)
    led.set_bottom_led(define.armor_bottom_all,69,215,255,define.effect_flash)
    led.set_bottom_led(define.armor_bottom_all,69,215,255,define.effect_flash)
    led.set_bottom_led(define.armor_bottom_all,69,215,255,define.effect_flash)
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
#     vision.enable_detection(define.vision_detection_marker)
#     gimbal.yaw(-90)
#     gimbal.yaw(90)
 
#     # Detect and handle markers
#     if vision.detect_marker_and_aim(define.marker_letter_F):
#         handle_fire()
#     elif vision.detect_marker_and_aim(define.marker_letter_D):
#         handle_danger()
#     elif vision.detect_marker_and_aim(define.marker_letter_P):
#         handle_person()
 
 #Scan and Handle Markers at different posts
def scan_and_handle_marker_at(post):
    # Detect and handle marker P
    if vision.detect_marker_and_aim(define.marker_letter_P):
        if post == "C":
            chassis.rotate_with_degree(define.anticlockwise, 180)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 0.21)
            chassis.rotate_with_degree(define.clockwise, 180)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 0.21)

        elif post == "E":
            chassis.rotate_with_degree(define.anticlockwise, 180)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 3.99)
            chassis.rotate_with_degree(define.clockwise, 180)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 3.99)


        elif post == "G":
            chassis.rotate_with_degree(define.anticlockwise, 180)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 3.32)
            chassis.rotate_with_degree(define.clockwise, 180)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 5)
            chassis.move_with_distance(0, 3.32)
            chassis.rotate_with_degree(define.clockwise, 90)

    elif vision.detect_marker_and_aim(define.marker_letter_F):
        handle_fire()
    elif vision.detect_marker_and_aim(define.marker_letter_D):
        handle_danger()




# Define Move to Post / Reset Points for the Robot
##########################################
 
#Move to Reset Point B
def move_to_reset_point_B():
    led.set_bottom_led(define.armor_bottom_all,0, 255, 0,define.effect_always_on)#Changes LED lights to green
    led.set_top_led(define.armor_top_all,0, 255, 0,define.effect_always_on)#Changes LED Lights to green
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
    
#Move to Reset Point C
def move_to_reset_point_C():
    led.set_bottom_led(define.armor_bottom_all,255, 255, 255,define.effect_always_on)#Changes LED lights to white
    led.set_top_led(define.armor_top_all,255, 255, 255,define.effect_always_on)#Changes LED Lights to white
    #chassis.rotate_with_degree(define.clockwise, 90)
    chassis.move_with_distance(0, 5)
    chassis.move_with_distance(0, 1.71)
 
    vision.enable_detection(define.vision_detection_marker)
    # Scan the area by rotating the gimbal
    gimbal.yaw(-90)
    gimbal.yaw(90)

    scan_and_handle_marker_at("C")
    
 
#Move to Reset Point D
def move_to_reset_point_D():
    led.set_bottom_led(define.armor_bottom_all,255, 165, 0,define.effect_always_on)#Changes LED lights to orange
    led.set_top_led(define.armor_top_all,255, 165, 0,define.effect_always_on)#Changes LED Lights to orange
    chassis.move_with_distance(0, 4.89)
    time.sleep(5)  # Reset point
    
 
#Move to Post E
def move_to_post_E():
    led.set_bottom_led(define.armor_bottom_all,128, 0, 128,define.effect_always_on)#Changes LED lights to light purple
    led.set_top_led(define.armor_top_all,0, 128, 0,define.effect_always_on)#Changes LED Lights to light purple
    chassis.move_with_distance(0, 4.14)
 
    # Scan the area by rotating the gimbal
    scan_and_handle_marker_at("E")

 
 #Move to Reset Point F
def move_to_reset_point_F():
    led.set_bottom_led(define.armor_bottom_all,255, 218, 185,define.effect_always_on)#Changes LED lights to peach
    led.set_top_led(define.armor_top_all,255, 218, 185,define.effect_always_on)#Changes LED Lights to peach
    # Add the correct movement logic to move to reset point F
    chassis.move_with_distance(0, 4.61)  # Placeholder values, adjust as needed
    time.sleep(5)  # Reset point
    
 
#Move to Post G
def move_to_post_G():
    led.set_bottom_led(define.armor_bottom_all,255, 192, 203,define.effect_always_on)#Changes LED lights to pink
    led.set_top_led(define.armor_top_all,255, 192, 203,define.effect_always_on)#Changes LED Lights to pink
    chassis.move_with_distance(0, 4.46)  
    #Scan for Markers
    scan_and_handle_marker_at(G)

 
#Move to Reset Point H
def move_to_reset_point_H():
    chassis.move_with_distance(0, 5)
    chassis.move_with_distance(0, 0.66)
    chassis.rotate_with_degree(define.clockwise, 180)
    time.sleep(5)  # Reset point
 
def move_back_to_reset_point_D():
    chassis.move_with_distance(0, 5)
    chassis.move_with_distance(0, 5)
    chassis.move_with_distance(0, 5)
    chassis.move_with_distance(0, 3.80)
    time.sleep(5)
 

 
#Starting Function
def main():
    # Set the robot to free mode
    robot.set_mode(define.robot_mode_free)
 
    # Set translation speed
    chassis.set_trans_speed(0.5)
 
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
 

if __name__ == "__main__":
    main()