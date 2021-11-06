#Mi nombre en magenta

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
color = (255, 0, 255)
sense.show_letter("O", color)
sleep(1)
sense.show_letter("S", color)
sleep(1)
sense.show_letter("C", color)
sleep(1)
sense.show_letter("A", color)
sleep(1)
sense.show_letter("R", color)
