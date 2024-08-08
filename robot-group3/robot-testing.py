

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




def scan_for_marker():


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



# Move to Post C

def move_to_post_C():

    led.set_bottom_led(define.armor_bottom_all, 255, 255, 255, define.effect_always_on)  # Changes LED lights to white
    led.set_top_led(define.armor_top_all, 255, 255, 255, define.effect_always_on)  # Changes LED lights to white
    chassis.move_with_distance(0, 5)
    chassis.move_with_distance(0, 1.78)



# Starting Function

def start():

    robot.set_mode(define.robot_mode_free)
    chassis.set_trans_speed(0.6)

    move_to_post_C()
    scan_for_marker()


# Registering Vision Marker Event Handlers
vision.set_marker_detection_callback(define.marker_letter_F, vision_recognized_marker_letter_F)



if __name__ == "__main__":
    start()
 