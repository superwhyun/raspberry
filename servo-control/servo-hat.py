
from lib import PCA9685 
import time



if __name__ == '__main__':
  pwm = PCA9685.PCA9685(0x40, debug=False)
  pwm.setPWMFreq(50)


  for i in range(6):
    pwm.setServoPulse(i, 500) 
    time.sleep(0.4)

  for i in range(6):
    pwm.setServoPulse(i, 1000)
    time.sleep(0.4)

  print('Done')
  time.sleep(2)

