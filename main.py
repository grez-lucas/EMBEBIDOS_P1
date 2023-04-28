import time
from machine import I2C
from hx711 import HX711
# from machine import Pin

# Global vars

hx = HX711()
hx.tare()
choices = {'Peanuts': 50, 'Almonds': 80, 'Nuts  ': 100}
food_picked = 'Peanuts'
amount_picked_index = 0

# functions

def print_status():
    lcd.clear()
    # lcd.putstr(" Food: " + food_picked +"\n   Portion: "+ str(choices[food_picked]) + "g x"+str(amount_picked_index+1))
    sleep(1)

def change_food():
    global food_picked
    if food_picked == 'Peanuts':
        food_picked = 'Almonds'
    elif food_picked == 'Almonds':
        food_picked = 'Nuts  '
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
# lcd.custom_char(1, face)
# lcd.putstr(" Food: " + food_picked +"\n Portion: "+ str(choices[food_picked]) + "g x"+str(amount_picked_index+1))
sleep(2)

#changeFoodBtn.irq(trigger = machine.Pin.IRQ_FALLING, handler = change_food)

while True:
    if not changeFoodBtn.value():
        print("Changing food..")
        # change_food()
    if not changePortionBtn.value():
        print("Changing portion...")
        # change_portion()
    if not enterBtn.value():
        print("boton3")
        s1.step(1000)
        time.sleep(2)
        # while True:
        #     reading = hx.get_units(10)
        #     print('FUNCIONOOOOOOOOOO')
        #     # s1.step(50)
        #     if reading > (choices[food_picked]*amount_picked_index*5):
        #         break