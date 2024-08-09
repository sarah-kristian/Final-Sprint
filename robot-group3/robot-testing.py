PostCtr = 0
 

def move_to_reset_point_B():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_always_on)  # Green LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, rm_define.effect_always_on)  # Green LEDs
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
    time.sleep(5)
 
def move_to_post_C():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 255, 255, rm_define.effect_always_on)  # White LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 255, 255, rm_define.effect_always_on)  # White LEDs
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 1.78)
    time.sleep(2)
 
 
def move_to_reset_point_D():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 165, 0, rm_define.effect_always_on)  # Orange LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 165, 0, rm_define.effect_always_on)  # Orange LEDs
    chassis_ctrl.move_with_distance(0, 4.89)
    time.sleep(5)
 
def move_to_post_E():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 128, 0, 128, rm_define.effect_always_on)  # Light Purple LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 128, 0, 128, rm_define.effect_always_on)  # Light Purple LEDs
    chassis_ctrl.move_with_distance(0, 4.14)
 
 
def move_to_reset_point_F():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 218, 185, rm_define.effect_always_on)  # Peach LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 218, 185, rm_define.effect_always_on)  # Peach LEDs
    chassis_ctrl.move_with_distance(0, 4.61)
    time.sleep(5)
 
def move_to_post_G():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 192, 203, rm_define.effect_always_on)  # Pink LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 192, 203, rm_define.effect_always_on)  # Pink LEDs
    chassis_ctrl.move_with_distance(0, 4.46)
 
 
def move_to_reset_point_H():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_always_on)  # Blue LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 255, rm_define.effect_always_on)  # Blue LEDs
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 0.66)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    time.sleep(5)
 
 
def move_back_to_reset_point_H_F():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.9)
    time.sleep(3)
 
 
def move_back_to_reset_point_F_D():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 3.65)
    rockout()
    time.sleep(5)
 
def move_back_to_start_D_B():
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 255, rm_define.effect_flash)  # Flashing Purple LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 255, rm_define.effect_flash)  # Flashing Purple LEDs
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 1.57)
    time.sleep(3)
 
def move_back_to_start_B_A():
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 3.49)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
    time.sleep(3)
 
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
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(90)
 
 
def vision_recognized_marker_letter_F(msg):
    print("Found marker F ...")
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    led_ctrl.gun_led_on()
    gun_ctrl.fire_once()
    led_ctrl.gun_led_off()
    chassis_ctrl.rotate_with_time(rm_define.clockwise, 90)
    
 
 
def vision_recognized_marker_letter_D(msg):
    print("Found marker D ...")
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    chassis_ctrl.rotate_with_time(rm_define.clockwise, 90)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)
     
 
def vision_recognized_marker_letter_P(msg):
    global PostCtr
    print("Found marker P ...")
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 255, 0, rm_define.effect_always_on)  # Yellow LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 255, 0, rm_define.effect_flash)  # Yellow LEDs
    
    print(PostCtr)
    if PostCtr == 1:
        print("Found place 1/C ...")
        gimbal_ctrl.recenter()
        chassis_ctrl.set_rotate_speed(90)
        gimbal_ctrl.set_rotate_speed(300)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 270)
        gimbal_ctrl.recenter()
        # C to B
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.86)
        time.sleep(3)
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
        # B to C
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.86)
        time.sleep(5)
        
    elif PostCtr == 2:
        print("Found place 2/E ...")
        gimbal_ctrl.recenter()
        chassis_ctrl.set_rotate_speed(90)
        gimbal_ctrl.set_rotate_speed(300)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 270)
        gimbal_ctrl.recenter()
        # the distance E to D
        chassis_ctrl.move_with_distance(0, 4.06)
        time.sleep(3)
        # the distance D to B
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.57)
        time.sleep(3)
        # the distance B to A
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.49)
        time.sleep(5)
        # return
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        time.sleep(5)
 
        # the distance A to B
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.49)
        time.sleep(3)
 
        # the distance B to D
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.57)
        time.sleep(3)
 
        # the distance D to E
        chassis_ctrl.move_with_distance(0, 4.06)
        time.sleep(5)
 
    elif PostCtr == 3:
        print("Found place 3/G ...")
        gimbal_ctrl.recenter()
        chassis_ctrl.set_rotate_speed(90)
        gimbal_ctrl.set_rotate_speed(300)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 270)
        gimbal_ctrl.recenter()
        # G to F
        chassis_ctrl.move_with_distance(0, 4.41)
        time.sleep(3)
        # F to D
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.65)
        # D to B
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.57)
        # B to A
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.49)
        time.sleep(5)
        # return
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        time.sleep(5)
        # A to B
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.49)
        time.sleep(3)
        # B to D
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.57)
        time.sleep(3)
        # D to F
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.65)
        time.sleep(3)
        # F to G
        chassis_ctrl.move_with_distance(0, 4.41)
        time.sleep(5)
       
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    # Increment the counter
 
 
def vision_recognized_marker_number_one(msg):
    print("Found the Number 1")
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    gimbal_ctrl.yaw_ctrl(250)
    gimbal_ctrl.recenter()
    led_ctrl.gun_led_on()
    led_ctrl.gun_led_off()
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
 
def vision_recognized_marker_number_two(msg):
    print("Found the Number 2")
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 52, 177, 235, rm_define.effect_always_on)  # Light blue LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 52, 235, 55, rm_define.effect_always_on)  # Green LEDs
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
 
def vision_recognized_marker_number_three(msg):
    print("Found the Number 3")
    gimbal_ctrl.yaw_ctrl(250)
    gimbal_ctrl.recenter()
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 52, 177, 235, rm_define.effect_always_on)  # Light blue LEDs
    led_ctrl.set_top_led(rm_define.armor_top_all, 52, 235, 55, rm_define.effect_flash)  # Green LEDs
    led_ctrl.gun_led_on()
    led_ctrl.gun_led_off()
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    
 
def start():
    global PostCtr
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    chassis_ctrl.set_trans_speed(0.5)
    move_to_reset_point_B()
 
    move_to_post_C()
    PostCtr += 1
    scan_for_marker()
 
    move_to_reset_point_D()
 
    move_to_post_E()
    PostCtr += 1
    scan_for_marker()
 
    move_to_reset_point_F()
    scan_for_marker()
 
    move_to_post_G()
    PostCtr += 1
    scan_for_marker()
    
    move_to_reset_point_H()
    
    move_back_to_reset_point_H_F()
 
    move_back_to_reset_point_F_D()
 
    move_back_to_start_D_B()
 
    move_back_to_start_B_A()
 
    move_back_to_start_A()