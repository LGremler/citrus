# This reads a .sdl file and prints it to the command line with proper
# formatting.

# Author: Logan Gremler 2/15/16

import sys
import os.path

def read_schedule():
    # Get a week code from the user:
    getWeekCode = raw_input("What is the Week Code of the schedule you would like to view? ")

    # Open the proper .sdl file:
    document = 'Week' +str(getWeekCode) +'.sdl'
    schedule = open(document)

    # Output the contents of the schedule:
    print schedule.read()
