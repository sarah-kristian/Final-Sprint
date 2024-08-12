#Robot Python Project - Mario Tank
#Date Started: Aug. 1st, 2024. Date Completed: Aug. 11th, 2024
#Group 3: Abdul, Noah, Amanda, Walid, Sarah, & Alexander
 
#Global Variable
PostCtr = 0
 
 
#Move to Point B(Obstacle Course)
def move_to_reset_point_B():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_always_on)  # Green LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, rm_define.effect_always_on)  # Green LEDs
    media_ctrl.play_sound(rm_define.media_custom_audio_4)#"Here we goooo"
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
    #time.sleep(5)
 
#Move to Post C
def move_to_post_C():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 255, 255, rm_define.effect_always_on)  # White LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 255, 255, rm_define.effect_always_on)  # White LEDs
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 1.78)
    time.sleep(2)
 
#Move to Reset Point D
def move_to_reset_point_D():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 165, 0, rm_define.effect_always_on)  # Orange LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 165, 0, rm_define.effect_always_on)  # Orange LEDs
    chassis_ctrl.move_with_distance(0, 5)
    
#Move to Post E 
def move_to_post_E():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 128, 0, 128, rm_define.effect_always_on)  # Light Purple LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 128, 0, 128, rm_define.effect_always_on)  # Light Purple LEDs
    chassis_ctrl.move_with_distance(0, 4.14)
 
#Move to Reset Point F
def move_to_reset_point_F():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 218, 185, rm_define.effect_always_on)  # Peach LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 218, 185, rm_define.effect_always_on)  # Peach LEDs
    chassis_ctrl.move_with_distance(0, 4.61)
    
#Move to Post G 
def move_to_post_G():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 192, 203, rm_define.effect_always_on)  # Pink LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 192, 203, rm_define.effect_always_on)  # Pink LEDs
    chassis_ctrl.move_with_distance(0, 4.46)
 
#Move to Reset Point H 
def move_to_reset_point_H():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_always_on)  # Blue LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_always_on)  # Blue LEDs
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 0.9)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    gimbal_ctrl.recenter()
    
 
#Move back to Reset Point F from H
def move_back_to_reset_point_H_F():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    time.sleep(3)
    media_ctrl.play_sound(rm_define.media_custom_audio_5)#"Bop, Let's a gooo"
 
#Move back to Reset Point D from F 
def move_back_to_reset_point_F_D():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 3.9)
    rockout()
    play_sleep()
#Move back to Reset Point B from D 
def move_back_to_start_D_B():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 255, rm_define.effect_flash)  # Flashing Purple LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 255, rm_define.effect_flash)  # Flashing Purple LEDs
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 1.57)
    time.sleep(3)
    media_ctrl.play_sound(rm_define.media_custom_audio_5)#"Bop, Let's a gooo"
 
 #Move back to Point A from B
def move_back_to_start_B_A():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 3.69)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
    media_ctrl.play_sound(rm_define.media_custom_audio_8)#"Moon get"
    time.sleep(3)
    
#Rockout function w efound on GitHub that flashes the LED lights and manipulates the gun light performing a dance. 
def rockout():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    chassis_ctrl.set_rotate_speed(120)
    gimbal_ctrl.set_rotate_speed(120)
    media_ctrl.play_sound(rm_define.media_custom_audio_3)#Rockout Fireworks sound
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
 
#Scans for marker
def scan_for_marker():
    print("Scanning for marker ...")
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    #chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(+180)
    gimbal_ctrl.recenter()
 
#Identifying Marker F
def vision_recognized_marker_letter_F(msg):
    print("Found marker F ...")
    cappy_sound()
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    zapper_sound()
    led_ctrl.gun_led_on()
    led_ctrl.gun_led_off()
    gun_ctrl.fire_once()
    gimbal_ctrl.recenter()
    
#Identifying Marker D
def vision_recognized_marker_letter_D(msg):
    print("Found marker D ...")
    cappy_sound()
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_D)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)
    media_ctrl.play_sound(rm_define.media_custom_audio_9)#Waaa sound
    gimbal_ctrl.recenter()
     
#Identifying Marker P(Accounting for Post Positioning)
def vision_recognized_marker_letter_P(msg):
    global PostCtr
    print("Found marker P ...")
    cappy_sound()
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_P)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 255, 0, rm_define.effect_always_on)  # Yellow LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 255, 0, rm_define.effect_flash)  # Yellow LEDs
    
    print(PostCtr)
    if PostCtr == 1:
        print("Found place 1/C ...")
        gimbal_ctrl.recenter()
        chassis_ctrl.set_rotate_speed(90)
        gimbal_ctrl.set_rotate_speed(300)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        # C to B
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.86)
        time.sleep(3)
        media_ctrl.play_sound(rm_define.media_custom_audio_5)#"Bop, Let's a gooo"
        # B to A
        chassis_ctrl.move_with_distance(0, 3.43)
        chassis_ctrl.move_with_distance(0, 5)
        time.sleep(5)
        # return
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        time.sleep(5)
        # A to B
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.43)
        time.sleep(3)
        media_ctrl.play_sound(rm_define.media_custom_audio_5)#"Bop, Let's a gooo"
        # B to C
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.86)
        time.sleep(5)
        
    elif PostCtr == 2:
        print("Found place 2/E ...")
        gimbal_ctrl.recenter()
        chassis_ctrl.set_rotate_speed(90)
        gimbal_ctrl.set_rotate_speed(300)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        #E to D
        chassis_ctrl.move_with_distance(0, 4.06)
        time.sleep(3)
        media_ctrl.play_sound(rm_define.media_custom_audio_5)#"Bop, Let's a gooo"
        #D to B
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.57)
        time.sleep(3)
        media_ctrl.play_sound(rm_define.media_custom_audio_7)#"Wa-hoo"
        #B to A
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.49)
        time.sleep(5)
        # Return
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        time.sleep(5)
 
        #A to B
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.49)
        time.sleep(3)
        media_ctrl.play_sound(rm_define.media_custom_audio_5)#"Bop, Let's a gooo"
 
        #B to D
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.57)
        time.sleep(3)
        media_ctrl.play_sound(rm_define.media_custom_audio_7)#"Wa-hoo"
 
        #D to E
        chassis_ctrl.move_with_distance(0, 4.06)
        time.sleep(5)
        media_ctrl.play_sound(rm_define.media_custom_audio_5)#"Bop, Let's a gooo"
 
    elif PostCtr == 3:
        print("Found place 3/G ...")
        gimbal_ctrl.recenter()
        chassis_ctrl.set_rotate_speed(90)
        gimbal_ctrl.set_rotate_speed(300)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        #G to F
        chassis_ctrl.move_with_distance(0, 4.41)
        time.sleep(3)
        media_ctrl.play_sound(rm_define.media_custom_audio_7)#"Wa-hoo"
        #F to D
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.65)
        #D to B
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.57)
        #B to A
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.49)
        time.sleep(5)
        #Return
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        time.sleep(5)
        #A to B
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.49)
        time.sleep(3)
        media_ctrl.play_sound(rm_define.media_custom_audio_5)#"Bop, Let's a gooo"
        #B to D
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.57)
        time.sleep(3)
        media_ctrl.play_sound(rm_define.media_custom_audio_7)#"Wa-hoo"
        #D to F
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.65)
        time.sleep(3)
        media_ctrl.play_sound(rm_define.media_custom_audio_5)#"Bop, Let's a gooo"
        #F to G
        chassis_ctrl.move_with_distance(0, 4.41)
        time.sleep(5)
       
   
#Identifying Marker 1
def vision_recognized_marker_number_one(msg):
    print("Found the Number 1")
    cappy_sound()
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    gimbal_ctrl.yaw_ctrl(250)
    gimbal_ctrl.recenter()
    led_ctrl.gun_led_on()
    led_ctrl.gun_led_off()
  
#Identifying Marker 2
def vision_recognized_marker_number_two(msg):
    print("Found the Number 2")
    cappy_sound()
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_two)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 52, 177, 235, rm_define.effect_flash)  # Light blue LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 52, 235, 55, rm_define.effect_flash)  # Green LEDs
    
#Identifying Marker 3
def vision_recognized_marker_number_three(msg):
    print("Found the Number 3")
    cappy_sound()
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_three)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.yaw_ctrl(250)
    gimbal_ctrl.recenter()
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 52, 177, 235, rm_define.effect_always_on)  # Light blue LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 52, 235, 55, rm_define.effect_flash)  # Green LEDs
    led_ctrl.gun_led_on()
    led_ctrl.gun_led_off()
    
 
#media_ctrl.play_sound(rm_define.media_custom_audio_undefined) 
 
#Sleep Function to Sleep and Play Sleep Sound
def play_sleep():   
    media_ctrl.play_sound(rm_define.media_custom_audio_0) #Sleep sound
    time.sleep(5)
 
#Function for Marker Recognition Sound
def cappy_sound():
    media_ctrl.play_sound(rm_define.media_custom_audio_1)#Cappy transformation
 
#Function for Zapper Sound
def zapper_sound():
    media_ctrl.play_sound(rm_define.media_custom_audio_2)#Zapper sound
    
 
#Sources for extra audio sounds
'''
media_ctrl.play_sound(rm_define.media_custom_audio_5)#"Bop, Let's a gooo"
media_ctrl.play_soundrm_define.media_custom_audio_7#"Wa-hoo"
media_ctrl.play_soundrm_define.media_custom_audio_8#"Moon get"
 '''   
    
    
#Main Program begins here:
def start():
    global PostCtr
    
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    chassis_ctrl.set_trans_speed(0.5)
    gimbal_ctrl.set_rotate_speed(60)
    
    move_to_reset_point_B()
    play_sleep()
 
    move_to_post_C()
    PostCtr += 1#Increments Post by 1
    scan_for_marker()
    
    move_to_reset_point_D()
    play_sleep()
    
    move_to_post_E()
    PostCtr += 1#Increments Post by 1
    scan_for_marker()
    
    move_to_reset_point_F()
    scan_for_marker()
    play_sleep()
    
    move_to_post_G()
    PostCtr += 1#Increments Post by 1
    scan_for_marker()
        
    move_to_reset_point_H()
    play_sleep()
        
    move_back_to_reset_point_H_F()
    
    move_back_to_reset_point_F_D()
    
    move_back_to_start_D_B()
    
    move_back_to_start_B_A()
    
    play_sleep()
 
#End of Program