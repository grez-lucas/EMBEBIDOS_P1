import machine
# from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
import Stepper
from ldr import LDR

# led setup

led = machine.Pin(15, machine.Pin.OUT)
ldr = LDR(12)
led = machine.Pin(14,machine.Pin.OUT)

# 16x2 LCD Screen setup

""" I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16 """

s1 = Stepper.create(machine.Pin(32,machine.Pin.OUT),machine.Pin(33,machine.Pin.OUT),machine.Pin(25,machine.Pin.OUT),machine.Pin(26,machine.Pin.OUT))
#i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)

# lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# face = bytearray([0x00,0x00,0x0A,0x00,0x11,0x0E,0x00,0x00])

# Button setup

changeFoodBtn = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
changePortionBtn = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
enterBtn = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)


