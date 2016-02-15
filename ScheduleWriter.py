# This writes all relevant schedule information to the schedule file and asks
# the user what needs to be added to the schedule

# Author: Logan Gremler 1/26/16 and a bit later
import sys
import os.path

# Create a .sdl file:
document = open('Schedule.sdl', 'a')
if os.path.exists('./Schedule.sdl'):
    document = open('Schedule.sdl', 'r+')

# Take user input:
print "***Separate tasks with a comma***"
monday = raw_input("What needs done this Monday?")
tuesday = raw_input("What needs done this Tuesday?")
wednesday = raw_input("What needs done this Wednesday?")
thursday = raw_input("What needs done this Thursday?")
friday = raw_input("What needs done this Friday?")
saturday = raw_input("What needs done this Saturday?")
sunday = raw_input("What needs done this Sunday?")

# Separate tasks by replacing commas with blank lines:
day1 = monday.replace(",", "\n")
day2 = tuesday.replace(",", "\n")
day3 = wednesday.replace(",", "\n")
day4 = thursday.replace(",", "\n")
day5 = friday.replace(",", "\n")
day6 = saturday.replace(",", "\n")
day7 = sunday.replace(",", "\n")


# Write all relevant information to the schedule:
def write_schedule():
    header1 = document.write("Monday:\n")
    task1 = document.write(day1)
    header2 = document.write("\n\nTuesday:\n")
    task2 = document.write(day2)
    header3 = document.write("\n\nWednesday:\n")
    task3 = document.write(day3)
    header4 = document.write("\n\nThursday:\n")
    task4 = document.write(day4)
    header5 = document.write("\n\nFriday:\n")
    task5 = document.write(day5)
    header6 = document.write("\n\nSaturday:\n")
    task6 = document.write(day6)
    header7 = document.write("\n\nSunday:\n")
    task7 = document.write(day7)
