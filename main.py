import time
import i2c_lcd
from machine import I2C

# Global vars


choices = {'Peanuts': [50,70,90], 'Raisins': [30,40,50], 'Nuts': [60,90,100]}
food_picked = 'Peanuts'
amount_picked_index = 0

# functions

def print_status():
    lcd.clear()
    lcd.putstr(" Food: " + food_picked +"\n Portion: "+ str(choices[food_picked][amount_picked_index]) + " g")
    sleep(1)

def change_food():
    global food_picked
    if food_picked == 'Peanuts':
        food_picked = 'Raisins'
    elif food_picked == 'Raisins':
        food_picked = 'Nuts'
    else:
        food_picked = 'Peanuts'
    print_status()

def change_portion():
    global amount_picked_index
    if amount_picked_index < 2:
        amount_picked_index +=1
    else:
        amount_picked_index = 0
    print_status()


# Start lcd with initial values
lcd.custom_char(1, face)
lcd.putstr(" Food: " + food_picked +"\n Portion: "+ str(choices[food_picked][amount_picked_index]) + " g")
sleep(2)

#changeFoodBtn.irq(trigger = machine.Pin.IRQ_FALLING, handler = change_food)

while True:
    if not changeFoodBtn.value():
        print("Changing food..")
        change_food()
    if not changePortionBtn.value():
        print("Changing portion...")
        change_portion()
