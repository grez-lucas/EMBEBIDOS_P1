import time
from hx711 import HX711
# from machine import Pin

# Global vars

hx = HX711()
#hx.set_scale(hx)
hx.tare()


lcd.begin()
 
led_red.on()
led_red.value(1)

choices = {'Peanuts': 50, 'Almonds': 80, 'Nuts  ': 100}
food_picked = 'Peanuts'
amount_picked_index = 0

# functions
def startup_message():
    lcd.clear()
    lcd.set_cursor(col=0, row=0)
    lcd.print(" Food Dispenser")


    lcd.create_char(
    location=0,
    charmap=[0x00, 0x00, 0x11, 0x04, 0x04, 0x11, 0x0E, 0x00]
)
    lcd.set_cursor(col=0, row=1)
    lcd.print("Starting...  " + chr(0))

    sleep(4)


def print_status():
    lcd.clear()
    lcd.set_cursor(col=0, row=0)
    lcd.print(" Food: " + food_picked)
    lcd.set_cursor(col=0, row=1)
    lcd.print("Portion: " + str(choices[food_picked]) + "g x"+str(amount_picked_index+1))
    sleep(0.5)

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
startup_message()
print_status()

while True:
    valor = ldr.value()
    # print(valor)
    if valor <160:
        led_red.on()
        led_green.off()
    else:
        led_green.on()
        led_red.off()
    if not changeFoodBtn.value():
        print("Changing food..")
        change_food()
    if not changePortionBtn.value():
        print("Changing portion...")
        change_portion()
    if not enterBtn.value():
        print("Dispensing...")

        if food_picked == 'Peanuts':
            for i in list(range(amount_picked_index+1)):
                s1.step(500)
        elif food_picked == 'Almonds':
            for i in list(range(amount_picked_index+1)):
                s1.step(500)
        elif food_picked == 'Nuts  ':
            for i in list(range(amount_picked_index+1)):
                s1.step(500)
            """
        while True:
            reading = hx.get_units(10)
            print(reading, (choices[food_picked]*(amount_picked_index+1)*5))
            s1.step(200)
            if reading > (choices[food_picked]*(amount_picked_index+1)*100):
                print("Done dispensing")
                break
"""
            