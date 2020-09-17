import webfont_exporter
import android_xml_creator
import strings_converter.strings_to_csv as strings_to_csv
import strings_converter.csv_to_strings as csv_to_strings
import os

# if __name__ == '__main__':
webfont_exporter.clear()
# inp = str(input("Please enter a filepath of style.css of webfont: "))
# path = inp
# icons_dict = webfont_exporter.get_icon_names()
# webfont_exporter.get_icon_names(path)
# webfont_exporter.get_output(icons_dict, path)
selection = -1
while selection < 0 or selection > 2:
    webfont_exporter.clear()
    if os.name == "nt":
        directory_mark = "\\"
    else:
        directory_mark = "/"
    selection = int(input(
        "\n Welcome Dear User, please select a function.\n\n (I advise you to create android layout (choose 1) first, \n then rename in Android Studio and convert strings to iOS (choose 2).)\n\n 1. Create Android layout, Android strings, iOS variables\n 2.Convert Android strings to ios variables\n Your Selection: "))

if selection == 1:
    android_xml_creator.get_layout_and_fonts()
    str(input("\n Now you can access output files. files are located near style.css (input file path)."))

elif selection == 2:
    str(input(
        "\n\n\t\t\t**WARNING**\n You have to rename your Android string file as \"strings_tr.xml\" and put it\n into \"" + str(
            os.getcwd()) + "\" directory.\n Do it then press enter to continue."))
    strings_to_csv.xml_to_csv(platform=1)
    csv_to_strings.csv_to_xml(platform=2)
    str(input("\n Now you can access output files.\n iOS variables path: \"" + str(
        os.getcwd()) + directory_mark + "ios_variables.swift\"\n Csv file path: " + str(
        os.getcwd()) + directory_mark + "strings.csv\""))
