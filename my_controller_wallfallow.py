"""my_controller_wallfallow controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
def run_robot(robot):
    """wall fallowing robot"""

    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    max_speed=6.28
    
    # Enable motors
    left_motor=robot.getMotor('left wheel motor')
    right_motor=robot.getMotor('right wheel motor')
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    prox_sensors=[]
    for ind in range(8):
        sensor_name= 'ps'+str(ind)
        prox_sensors.append(robot.getDistanceSensor(sensor_name))
        prox_sensors[ind].enable(timestep)
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Read the sensors:
        for ind in range(8):
            print("ind:{},val:{}".format(ind,prox_sensors[ind].getValue()))
        # Enter here functions to read sensor data, like:
        #  val = ds.getValue()
    
        # Process sensor data here.
        left_wall = prox_sensors[5].getValue() > 80
        left_corner =prox_sensors[6].getValue() >80
        front_wall = prox_sensors[7].getValue() > 80
        
        
        left_speed=max_speed
        right_speed=max_speed
        
        if front_wall:
            print("Trun right in place")
            left_speed = max_speed
            right_speed = -max_speed
        else:
            if left_wall:
                print("Drive forward")
                left_speed = max_speed
                right_speed = max_speed
            else:
                print("trun left")
                left_speed =max_speed/8
                right_speed = max_speed
            if left_corner:
                print("came too close,drive right")
                left_speed = max_speed
                right_speed = max_speed/8  
                
   
        # Enter here functions to send actuator commands, like:
        #  motor.setPosition(10.0)
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
       

# Enter here exit cleanup code.
if __name__ =="__main__":
# create the Robot instance.
    myrobot=Robot()
    print("code is running")
    run_robot(myrobot)
    