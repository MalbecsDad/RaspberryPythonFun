from sense_hat import SenseHat
from random import randint
sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

while True:

    # Generate a random colour
    def pick_random_colour():
        random_red = randint(0, 255)
        random_green = randint(0, 255)
        random_blue = randint(0, 255)
        return (random_red, random_green, random_blue)

    sense.show_message("Hello George", text_colour=pick_random_colour(), back_colour=pick_random_colour())
