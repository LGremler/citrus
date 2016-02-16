# This file runs the program and allows the user to either create a new schedule
# or view an existing one.

# Author: Logan Gremler 1/26/16 and a bit later

from Menu import main_menu
from ScheduleWriter import write_schedule
from ScheduleReader import read_schedule
import sys
import os.path

# Display the main menu and ask the user what they want to do:
main_menu()
option = raw_input("Choose an option: ")

if option == "1":
    write_schedule()
    
elif option == "2":
    read_schedule()
