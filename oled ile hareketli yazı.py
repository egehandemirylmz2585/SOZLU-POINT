

from machine import Pin, SoftI2C
import ssd1306
from time import sleep


i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

x = "Hallo "
x1 = "Ich bin "
x3 = "VBO"

screen2_row1 = "VEHBI BATUHAN OKUDUCU"
screen2_row2 = "2614 Hz/B"

screen3_row1 = "VBO"

screen1 = [[0, 0 , x], [0, 16, x1], [0, 32,x3]]
screen2 = [[0, 0 , screen2_row1], [0, 16, screen2_row2]]
screen3 = [[0, 40 , screen3_row1]]

# Scroll in screen horizontally from left to right
def scroll_in_screen(screen):
  for i in range (0, oled_width+1, 4):
    for line in screen:
      oled.text(line[2], -oled_width+i, line[1])
    oled.show()
    if i!= oled_width:
      oled.fill(0)

# Scroll out screen horizontally from left to right
def scroll_out_screen(speed):
  for i in range ((oled_width+1)/speed):
    for j in range (oled_height):
      oled.pixel(i, j, 0)
    oled.scroll(speed,0)
    oled.show()

# Continuous horizontal scroll
def scroll_screen_in_out(screen):
  for i in range (0, (oled_width+1)*2, 1):
    for line in screen:
      oled.text(line[2], -oled_width+i, line[1])
    oled.show()
    if i!= oled_width:
      oled.fill(0)

# Scroll in screen vertically
def scroll_in_screen_v(screen):
  for i in range (0, (oled_height+1), 1):
    for line in screen:
      oled.text(line[2], line[0], -oled_height+i+line[1])
    oled.show()
    if i!= oled_height:
      oled.fill(0)

# Scroll out screen vertically
def scroll_out_screen_v(speed):
  for i in range ((oled_height+1)/speed):
    for j in range (oled_width):
      oled.pixel(j, i, 0)
    oled.scroll(0,speed)
    oled.show()

# Continous vertical scroll
def scroll_screen_in_out_v(screen):
  for i in range (0, (oled_height*2+1), 1):
    for line in screen:
      oled.text(line[2], line[0], -oled_height+i+line[1])
    oled.show()
    if i!= oled_height:
      oled.fill(0)

while True:

  # Scroll in, stop, scroll out (horizontal)
  scroll_in_screen(screen1)
  sleep(2)
  scroll_out_screen(4)

  scroll_in_screen(screen2)
  sleep(2)
  scroll_out_screen(4)

  scroll_in_screen(screen3)
  sleep(2)
  scroll_out_screen(4)

  # Continuous horizontal scroll
  scroll_screen_in_out(screen1)
  scroll_screen_in_out(screen2)
  scroll_screen_in_out(screen3)

  # Scroll in, stop, scroll out (vertical)
  scroll_in_screen_v(screen1)
  sleep(2)
  scroll_out_screen_v(4)

  scroll_in_screen_v(screen2)
  sleep(2)
  scroll_out_screen_v(4)

  scroll_in_screen_v(screen3)
  sleep(2)
  scroll_out_screen_v(4)

  # Continuous verticall scroll
  scroll_screen_in_out_v(screen1)
  scroll_screen_in_out_v(screen2)
  scroll_screen_in_out_v(screen3)