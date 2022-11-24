
# Modified from SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# Modified from SPDX-License-Identifier: MIT

"""Simple test for I2C RGB character LCD shield kit"""
import time
import board
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

lcd_columns = 16
lcd_rows = 2

options = [ ["Shirt","Skirt","Trousers","Shorts","Dress"],
			["Red","Green","Blue","Black","White"]
		  ]

# Initialise I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)


#lcd.cursor = True

#lcd.blink = True


def refresh(i, j):
	lcd.clear()
	lcd.message=  '^v<> Options' +'\n' + option[i][j]
	time.sleep(0.5)



while True:
	lcd.clear()
	lcd.message= "Custom Clothing\nEnter to scan"
	lcd.color = [0, 0, 100]

	while not lcd.select_button:
		pass
	time.sleep(0.5)
	while lcd.select_button:
		pass
	lcd.clear()
	lcd.message= "Scanning...\nSelect when done"
	lcd.color = [100, 0, 0]
	time.sleep(1)

	while not lcd.select_button:
		pass
	time.sleep(0.5)		
	while lcd.select_button:
		pass

	lcd.clear()
	lcd.message= "Scan successful\nSelect 4 options"
	lcd.color = [0, 0, 100]

	while not lcd.select_button:
		pass
	time.sleep(0.5)		
	while lcd.select_button:
		pass


	lcd.clear()
	lcd.message= "Scan successful\nSelect 4 options"


	while not lcd.select_button:
		pass
	time.sleep(0.5)		
	while lcd.select_button:
		pass

	i = 0
	j = 0
	refresh(i,j)

	while not lcd.select_button:
		if lcd.up_button:
			i = i+1% len(options)
			j=0
			refresh(i,j)

		elif lcd.down_button:
			i = i-1% len(options)
			j=0
			refresh(i,j)

		elif lcd.left_button:
			j = j-1% len(options[i])	
			refresh(i,j)		

		elif lcd.right_button:
			j = j+1% len(options[i])
			refresh(i,j)

	time.sleep(0.5)		
	while not lcd.select_button:
		pass
	lcd.clear()
	lcd.message= "Options chosen\nOrder made"

	


