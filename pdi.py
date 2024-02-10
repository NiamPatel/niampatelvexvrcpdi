# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       niam                                                         #
# 	Created:      2/9/2024, 9:39:10 PM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello V5")
DriveStraightPreviousError = 0
ArmPIDPreviousError = 0
TrayPIDPreviousError = 0
kP = .5 #SUBJECT TO CHANGE ONCE TESTED
kD = .4 #SUBJECT TO CHANGE ONCE TESTED
def DriveStraight():
    while True:
        global DriveStraightTarget, DriveStraightVelocity, DriveStraightPreviousError, kP, kD
        Error = BLMotor.rotation(RotationUnits.DEG) - DriveStraightTarget
        derivative = Error - DriveStraightPreviousError
        FRMotor.spin_with_voltage(DirectionType.FWD,(((Error * kP + derivative * kD) * .12) * (DriveStraightVelocity/100)), VoltageUnits.VOLT)
        FLMotor.spin_with_voltage(DirectionType.FWD,(((Error * kP + derivative * kD) * .12) * (DriveStraightVelocity/100)), VoltageUnits.VOLT)
        BRMotor.spin_with_voltage(DirectionType.FWD,(((Error * kP + derivative * kD) * .12) * (DriveStraightVelocity/100)), VoltageUnits.VOLT)
        BLMotor.spin_with_voltage(DirectionType.FWD,(((Error * kP + derivative * kD) * .12) * (DriveStraightVelocity/100)), VoltageUnits.VOLT)
        DriveStraightPreviousError = Error
        sys.sleep(.02)
def ArmPID():
    while True:
        global ArmPIDTarget, ArmPIDVelocity, ArmPIDPreviousError, kP, kD
        Error = ArmPot.value(RotationUnits.DEG) - ArmPIDTarget
        derivative = Error - ArmPIDPreviousError
        ArmMotor.spin_with_voltage(DirectionType.FWD,(((Error * kP + derivative * kD) * .12) * (ArmPIDVelocity/100)), VoltageUnits.VOLT)
        ArmPIDPreviousError = Error
        sys.sleep(.02)
def TrayPID():
    while True:
        global TrayPIDTarget, TrayPIDVelocity, TrayPIDPreviousError, kP, kD
        Error = TrayPot.value(RotationUnits.DEG) - TrayPIDTarget
        derivative = Error - TrayPIDPreviousError
        TrayMotor.spin_with_voltage(DirectionType.FWD,(((Error * kP + derivative * kD) * .12) * (TrayPIDVelocity/100)), VoltageUnits.VOLT)
        TrayPIDPreviousError = Error
        sys.sleep(.02)

def StartAuton():
    TrayMotor.set_stopping(BrakeType.HOLD)
    IntakeLeft.set_stopping(BrakeType.HOLD)
    IntakeRight.set_stopping(BrakeType.HOLD)
    ArmMotor.set_stopping(BrakeType.HOLD)
    BLMotor.set_stopping(BrakeType.HOLD)
    FLMotor.set_stopping(BrakeType.HOLD)
    FRMotor.set_stopping(BrakeType.HOLD)
    TrayMotor.reset_rotation()
    IntakeLeft.reset_rotation()
    IntakeRight.reset_rotation()
    ArmMotor.reset_rotation()
    BLMotor.reset_rotation()
    FLMotor.reset_rotation()
    FLMotor.reset_rotation()
    FRMotor.reset_rotation()

def pre_auton():
    Inertial.start_calibration()
    con.screen.clear_screen()
    brain.screen.clear_screen()
    brain.screen.draw_image_from_file("MenuPage.png",0,0)
    brain.screen.render()
    Auton = 'MenuPage'
    
    pass

def autonomous():
    global TrayPIDTarget, TrayPIDVelocity, ArmPIDTarget, ArmPIDVelocity, DriveStraightTarget, DriveStraightVelocity
    sys.run_in_thread(DriveStraight)
    sys.run_in_thread(ArmPID)
    sys.run_in_thread(TrayPID)
    #START CODE
    StartAuton()
    ArmPIDVelocity = 100   #PUTTING RANDOM NUMBERS FOR ALL OF THIS
    ArmPIDTarget = 50
    sys.sleep(.02)
    TrayPIDVelocity = 100
    TrayPIDTarget = 50
    sys.sleep(.02)
    DriveStraightVelocity = 100
    DriveStraightTarget = 1000
    sys.sleep(.02)
    #END CODE
    sys.exit(DriveStraight)
    sys.exit(ArmPID)
    sys.exit(TrayPID)
    pass

        
