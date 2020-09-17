# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 13:52:44 2020

@author: yigit
"""
import time
import strings_to_csv
import csv_to_strings
from os import system, name

platform = -1  # platform==False is Android, platform==true IOS
platform_list = ["IOS", "Android"]
selected_platform = "Android"
function = -1  # [1,0] Android strings to ios, [0,1] ios strings to Android


def clear():
    # for windows 

    if name == 'nt':
        system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')


while True:
    clear()
    while function not in [0, 1, 2, 3, 4, 5,6]:
        try:
            function = int(input(
                "\nFunctions (Ctrl+double tap C to Exit):\n0.Android Strings to CSV\n1.IOS Strings to CSV\n2.Android Strings to IOS Strings\n3.IOS Strings to Android Strings\n4.CSV to Android Strings\n5.CSV to IOS Strings\n6.Android Strings to iOS Webfont Variable\nSelect a Function: "))
            # input("\nPlatform Was Set as Android. Please Press Enter to Continue or Ctrl+C to exit.")





        except:
            function = -1
            clear()
            time.sleep(0.5)
            print("\n\n** Please enter either 0(IOS) or 1(Android). **\n\n")
            time.sleep(2)

    if function == 0:
        strings_to_csv.xml_to_csv(platform=1)
    elif function == 1:
        strings_to_csv.xml_to_csv(platform=0)
    elif function == 2:
        strings_to_csv.xml_to_csv(platform=1)
        csv_to_strings.csv_to_xml(platform=0)
    elif function == 3:
        strings_to_csv.xml_to_csv(platform=0)
        csv_to_strings.csv_to_xml(platform=1)
    elif function == 4:
        csv_to_strings.csv_to_xml(platform=1)
    elif function == 5:
        csv_to_strings.csv_to_xml(platform=0)
    elif function == 6:
        strings_to_csv.xml_to_csv(platform=1)
        csv_to_strings.csv_to_xml(platform=2)
    function = -1
    input("please press Enter to continue or Ctrl+C to exit")
