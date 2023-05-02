import machine
from lcd_i2c import LCD
from machine import Pin, I2C
from time import sleep
import Stepper
from ldr import LDR

# led setup

led = machine.Pin(15, machine.Pin.OUT)
ldr = LDR(12)
led = machine.Pin(14,machine.Pin.OUT)

# 16x2 LCD Screen setup

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
FREQ = 800000

s1 = Stepper.create(machine.Pin(32,machine.Pin.OUT),machine.Pin(33,machine.Pin.OUT),machine.Pin(25,machine.Pin.OUT),machine.Pin(26,machine.Pin.OUT))


i2c = I2C(1, scl=Pin(21), sda=Pin(22), freq=FREQ)
lcd = LCD(addr=I2C_ADDR, cols=I2C_NUM_COLS, rows=I2C_NUM_ROWS, i2c=i2c)

# Button setup

changeFoodBtn = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
changePortionBtn = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
enterBtn = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)


