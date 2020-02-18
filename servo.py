import RPi.GPIO as GPIO
import time

import sys, os
import termios, fcntl
import select


fd = sys.stdin.fileno()
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON
newattr[3] = newattr[3] & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldterm = termios.tcgetattr(fd)
oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)




pin=18

DEFAULT_POSITION=3.0
MIN_POSITION=3.0
MAX_POSITION=10.0
STEP=0.1

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

p=GPIO.PWM(pin, 50)
p.start(DEFAULT_POSITION)
cur_pos=DEFAULT_POSITION

try:
  while True:

    inp, outp, err = select.select([sys.stdin], [], [])
    c = sys.stdin.read()
    if c == 'q':
        raise KeyboardInterrupt
        break
    elif c == '+':
        if(cur_pos <= MAX_POSITION):
            cur_pos=cur_pos + STEP
    elif c == '-':
        if(cur_pos >= MIN_POSITION):
            cur_pos=cur_pos - STEP
    else:
        print("fuck")

    #print("cur_pos :", str(cur_pos))
    p.ChangeDutyCycle(cur_pos)


except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
  termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
  fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
