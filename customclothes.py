
# Modified from SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# Modified from SPDX-License-Identifier: MIT

"""Simple test for I2C RGB character LCD shield kit"""
import time
import board
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

lcd_columns = 16
lcd_rows = 2

clothes = ["Shirt","Skirt","Trousers","Shorts","Dress"]
colours = ["Red","Green","Blue","Black","White"]

# Initialise I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.clear()
# Set LCD color to red
lcd.color = [100, 0, 0]
time.sleep(1)
# Print two line message
lcd.message = "Hello\nCircuitPython"

lcd.cursor = True

lcd.blink = True

#scroll_msg = "<-- Scroll"
#lcd.message = scroll_msg
# Scroll to the left
#for i in range(len(scroll_msg)):
#    time.sleep(0.5)
#    lcd.move_left()
#lcd.clear()
#time.sleep(1)
#lcd.message = "Going to sleep\nCya later!"
#time.sleep(5)


while True:
	lcd.message= "Custom Clothing\nPress Select to scan"


	if lcd.select_button:
		lcd.message= "Scanning…\n Press Select to stop scanning"
		lcd.color = [0, 100, 0]
		time.sleep(2)

		if lcd.select_button:
			lcd.message= "Scan successful\nLCD Press button for options"
			lcd.color = [0, 0, 100]
			time.sleep(2)



#if lcd.left_button:

#if lcd.up_button:


#On button release



#<Cycle through options>

