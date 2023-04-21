import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

# led setup

led = machine.Pin(2, machine.Pin.OUT)


# 16x2 LCD Screen setup

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

face = bytearray([0x00,0x00,0x0A,0x00,0x11,0x0E,0x00,0x00])

# Button setup

changeFoodBtn = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
changePortionBtn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)


