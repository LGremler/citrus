# This writes all relevant schedule information to the schedule file and asks
# the user what needs to be added to the schedule

# Author: Logan Gremler 1/26/16 and a bit later
import sys
import os.path

# Get a week code from the user:
week = raw_input("Enter a numerical week code: ")

# Create and open a new .sdl file:
document = 'Week' +str(week) +'.sdl'
schedule = open(document, 'w')

# Take user input:
print "***Separate tasks with a comma***"
monday = raw_input("What needs done this Monday? ")
tuesday = raw_input("What needs done this Tuesday? ")
wednesday = raw_input("What needs done this Wednesday? ")
thursday = raw_input("What needs done this Thursday? ")
friday = raw_input("What needs done this Friday? ")
saturday = raw_input("What needs done this Saturday? ")
sunday = raw_input("What needs done this Sunday? ")

# Separate tasks by replacing commas with blank lines and adding a "-"
# to signal the start of a task:
day1 = "- " + monday.replace(",", "\n- ")
day2 = "- " + tuesday.replace(",", "\n- ")
day3 = "- " + wednesday.replace(",", "\n- ")
day4 = "- " + thursday.replace(",", "\n- ")
day5 = "- " + friday.replace(",", "\n- ")
day6 = "- " + saturday.replace(",", "\n- ")
day7 = "- " + sunday.replace(",", "\n- ")


# Write all relevant information to the schedule:
def write_schedule():
    header1 = schedule.write("Monday:\n")
    task1 = schedule.write(day1)
    header2 = schedule.write("\n\nTuesday:\n")
    task2 = schedule.write(day2)
    header3 = schedule.write("\n\nWednesday:\n")
    task3 = schedule.write(day3)
    header4 = schedule.write("\n\nThursday:\n")
    task4 = schedule.write(day4)
    header5 = schedule.write("\n\nFriday:\n")
    task5 = schedule.write(day5)
    header6 = schedule.write("\n\nSaturday:\n")
    task6 = schedule.write(day6)
    header7 = schedule.write("\n\nSunday:\n")
    task7 = schedule.write(day7)

