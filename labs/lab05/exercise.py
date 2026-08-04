# Lab 05 - practice file
#
# Use this file to try out the examples as you work through the lab.
# Type them in, run the file, then clear it out and use it again for the next one.
#
# Run it from the terminal with:   python exercise.py
# On Windows you may need:         py exercise.py
#
# Nothing in this file is marked, so experiment as much as you like.
# Let's see Python keywords

# Import entire modules
import math
import random
import datetime

# Using imported modules
circle_area = math.pi * (5 ** 2)
random_number = random.randint(1, 100)
current_date = datetime.date.today()

# Import specific functions from modules
from math import sqrt, pow, sin, cos
from random import choice, shuffle
from datetime import datetime, timedelta

# Using imported functions directly (no module prefix needed)
square_root = sqrt(25)
power_result = pow(2, 8)
random_choice = choice(['apple', 'banana', 'cherry'])