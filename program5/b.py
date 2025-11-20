# (B) Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.
# Python 2.7 on raspberry pi
 # Script to trigger thermostat control on heating
 # Reads room temperatures from Prodserver DONE- from Thermostat01.py
 # All heating control logic is on prodserver. This just reads on/off commands
 # Dependencies
 # sudo pip install max7219- 7 seg 8 digit display driver
 # sudo pip install bs4- beautiful soup web scraper
 # sudo pip install requests- python http library for GET and POST
 # sudo apt-get install python-blinkt blinkt led library
 # GPIO PINS
 # MAX71297seg display
 # DIN =GPIO10(MOSI)
 # CS=GPIO8(SPI CE0)
 # CLK=GPIO11(SPI CLK)
 # Blinkt uses GPIO23,24
 Pin Constants
 PIN_RELAY = 17
 PIN_BOOST_DETECT =4
 import blinkt
 blinkt.set_clear_on_exit(False)
 blinkt.set_all(0,0,0)
 blinkt.set_brightness(0.1)
 blinkt.show()
 # blinkt Timer leds 0,1
 # blinkt Heat leds 2,3
 # blinkt Boost leds 4,5
 import sys
 # 7 seg display set up
 import max7219.led as led
 device = led.sevensegment()
 device.brightness(1)
 import requests
 from bs4 import BeautifulSoup
 fp.write(logstring)
 fp.close()
 print logstring
 def do_7segdisplay(status):
 "display on 7 seg"
 now=status[0]
 segnumber = 10000*now.hour + 100*now.minute + float(status[5])
 device.write_number(0,segnumber,decimalPlaces=2,zeroPad=True)
 def do_timer(status):
 "Deals with timer status led"
 if(status[3]): # timer on
 r,g,b = (0,250,0)
 else:
 r,g,b = (0,0,0)
 blinkt.set_pixel(0,r,g,b)
 #blinkt.set_pixel(1,r,g,b)
 blinkt.show()
 return
 def do_heat(status):
 "Deals with Heat status led and switches relay"
 if(status[4]): # heat on
 r,g,b = (200,000,000)
 GPIO.output(PIN_RELAY, GPIO.LOW)
 else:
 r,g,b = (0,0,0)
 GPIO.output(PIN_RELAY, GPIO.HIGH)
 blinkt.set_pixel(2,r,g,b)
 #blinkt.set_pixel(3,r,g,b)
 blinkt.show()
 return
 def do_boost():
      "No function as yet"
 # MAINPROGRAMME
 status = get_status(server, status)
 do_log(status)
 do_7segdisplay(status)
 do_timer(status)
 do_heat(status)