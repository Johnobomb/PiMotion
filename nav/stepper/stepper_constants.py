import math
# Stepper mode select
STEPPER_m0 = 17
STEPPER_m1 = 27
STEPPER_m2 = 22

# First wheel GPIO Pin
BR_step = 21
BR_dir = 20

# Second wheel GPIO Pin
FR_step = 11
FR_dir = 10

# Third wheel GPIO Pin
BL_step = 7
BL_dir = 8

# Fourth wheel GPIO Pin
FL_step = 24
FL_dir = 23

# Direction constants
FWD = True
REV = False

# Clockwise and Counter-clockwise constants 
CW = 1 			                 
CCW = 0

# whole, 1/2, 1/4, and 1/8 steps per revolution constants.
# steps per revolution is obtained by (360/1.8) * denominator. 
# ie: (360/1.8) * 2 = 400 for half steps per revolution
STEPS_PER_REVOLUTION = 200
HALF_STEPS_PER_REVOLUTION = 400
QUARTER_STEPS_PER_REVOLUTION = 800 		
EIGTH_STEPS_PER_REVOLUTION = 1600

DISTANCE = 60*math.pi/25.4

# individual steps per inch based off of whole step, 1/2 step, 1/4 step, and 1/8 step.
STEPS_PER_INCH = STEPS_PER_REVOLUTION/DISTANCE
HALF_STEPS_PER_INCH = HALF_STEPS_PER_REVOLUTION/DISTANCE
QUARTER_STEPS_PER_INCH = QUARTER_STEPS_PER_REVOLUTION/DISTANCE
EIGTH_STEPS_PER_INCH = EIGTH_STEPS_PER_REVOLUTION/DISTANCE

STEPPER_DELAY = 0.0005
