from colorzero import Color
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

start = Color('yellow')
end = Color('cyan')

for color in start.gradient(end, steps=100):
    sense.clear(color.rgb_bytes)
    sleep(0.1)