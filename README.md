# Parallax
Code for the ISS Tracker project

Objective: Build a 3D printed device that uses a pointer to indicate the position of the ISS in a straight line from the device's current location. The device will have it's own GPS antenna as well as WiFi and a 9-DOF sensor for calibration and positioning.

Constraints on production:
1. Programmed in Python3
2. Runs on Raspberry Pi Zero W

Bill Of Materials:
1. 3D Printed Parts
2. M3 Hardware (I'll add the detailed list when it's more final)
3. Raspberry Pi Zero WH with SD Card
4. Asafruit Stacking Header for Pi - PID: 1979
5. Adafruit DC & Stepper Motor Bonnet - PID: 4280
6. Adafruit Mini GPS PA1010D - PID: 4415
7. Adafruit 9-DOF Absolute Orientation IMU Fusion Breakout - BNO055 - PID: 4646
8. Adafruit Monochrome 1.3" 128x64 OLED Graphic Display - PID: 938
9. Sparkfun Qwiic or Stemma QT Shim - PID: 4463
10. Quantity 4: Stemma QT Cable 100mm - PID: 4210
11. Nema 17 Stepper Motor
12. Micro Servo
13. Slip Ring
14. Bearing: 30x55x13mm

You will need basic soldering skills and tools, heat-shrink tubing or electrical tape for finishing.

Slip Ring Wiring Plan
Board Side:
  Red: 5v (red) I2C line
  Black: Ground (black) I2C line
  Yellow: Yellow I2C line
  Brown: Blue I2C line
  Orange: Ras Pi GPIO Pin #
  Green: None

Staff Side:
  Red: 5v (red) I2C line & Servo Voltage
  Black: Ground (black) I2C line & Servo Ground
  Yellow: Yellow I2C line
  Brown: Blue I2C line
  Orange: Servo Data
  Green: None
