# This generates a .sdl file and wites all relevant content to the file
# This will be reorganized/cleaned up/improved heavily in the near future

# Author: Logan Gremler 2/9/16
import sys
import os.path

# Create the .sdl file
document = open('Schedule.sdl', 'a')
if os.path.exists('./Schedule.sdl'):
    document = open('Schedule.sdl', 'r+')

# Figure out what needs done:
monday = raw_input("What needs done this Monday? ")
tuesday = raw_input("What needs done this Tuesday? ")
wednesday = raw_input("What needs done this Wednesday? ")
thursday = raw_input("What needs done this Thursday? ")
friday = raw_input("What needs done this Friday? ")
saturday = raw_input("What needs done this Saturday? ")
sunday = raw_input("What needs done this Sunday? ")

# Write all relevant information to the schedule (in a very ugly way for now):
def write_schedule():
    task1 = document.write(monday)
    task2 = document.write(tuesday)
    task3 = document.write(wednesday)
    task4 = document.write(thursday)
    task5 = document.write(friday)
    task6 = document.write(saturday)
    task7 = document.write(sunday)

