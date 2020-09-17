# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:22:48 2020

@author: yigit
"""

import time
from os import system, name

class csv_to_xml:
    dictionary={}   #dictCreator functions update this dictionary
    platform=-1  #platform==False is Android, platform==true IOS
    platform_list=["IOS","Android"]
    selected_platform="Android"
    languages=["tr"]

    def __init__(self,platform=""):
        if platform=="":
            while csv_to_xml.platform not in [0,1,2]:
                try:
                    csv_to_xml.platform=int(input("Welcome, \nPlease Locate Your CSV File in the Same Directory With This Tool.(Ctrl+double tap C to Exit)\n0.IOS\n1.Android\nSelect a Platform: "))
                    #input("\nPlatform Was Set as Android. Please Press Enter to Continue or Ctrl+C to exit.")
                    csv_to_xml.selected_platform=csv_to_xml.platform_list[csv_to_xml.platform]


                except:
                    csv_to_xml.platform=-1
                    csv_to_xml.clear()
                    time.sleep(0.5)
                    print("\n\n** Please enter either 0(IOS) or 1(Android). **\n\n")
                    time.sleep(2)
        else:
            csv_to_xml.platform=platform
        csv_to_xml.main()
    def dictCreator(inputString):
        inputString=inputString.replace("\n","\ğ",inputString.count("\n"))
        lines=inputString.split("\ğ")
        for i in lines:
            if i=="" or i=="\n" or len(i.split(";"))<len(csv_to_xml.languages)+1:
                pass
            elif len(i.split(";"))>len(csv_to_xml.languages)+1:
                item=i.split(";")
                csv_to_xml.dictionary[item[0]]=[item[1],item[2]]

            else:
                item=i.split(";")
                csv_to_xml.dictionary[item[0]]=[item[1],item[2]]

    def StringsCreatorAndroid(dictionary):
        for i in range(len(csv_to_xml.languages)):
            print("strings_"+csv_to_xml.languages[i]+".xml")
            file=open("strings_"+csv_to_xml.languages[i]+".xml", "w", encoding="UTF-8")
            outputString="<resources>\n"
            for j in dictionary:
                outputString+="\n<string name=\"{}\">{}</string>".format(j,csv_to_xml.dictionary[j][i])
            outputString+="\n</resources>"
            file.write(outputString)
            file.close()

    def StringsCreatorIOS(dictionary):
        for i in range(len(csv_to_xml.languages)):
            file=open("Localizable_" + csv_to_xml.languages[i] + ".strings", "w", encoding="UTF-8")
            outputString=""
            for j in dictionary:
                if csv_to_xml.dictionary[j][i][0]=="\"":
                    outputString+="\"{}\" = \"{}\";\n".format(j,csv_to_xml.dictionary[j][i][1:len(csv_to_xml.dictionary[j][i])-1])
                else:
                    outputString+="\"{}\" = \"{}\";\n".format(j,csv_to_xml.dictionary[j][i])

            file.write(outputString)
            file.close()

    def ios_icon_font_variable_creator(dictionary):
        for i in range(len(csv_to_xml.languages)):
            file = open("ios_variables.swift", "w", encoding="UTF-8")
            outputString = ""
            for j in dictionary:
                if csv_to_xml.dictionary[j][i][0] == "\"":
                    outputString += "public let {} = String(format: \"%C\", 0x{})\n".format(j,
                                                                                            csv_to_xml.dictionary[j][i][
                                                                                            4:len(csv_to_xml.dictionary[
                                                                                                      j][i]) - 1])
                else:
                    outputString += "public let {} = String(format: \"%C\", 0x{})\n".format(j,
                                                                                            csv_to_xml.dictionary[j][i][3:])

            file.write(outputString)
            file.close()

    def main():
        #print(csv_to_xml.platform)
        inputFile=open("strings.csv","r", encoding="UTF-8")
        inputString=""
        inputString=inputFile.read()
        inputFile.close()

        if csv_to_xml.platform==1:
            csv_to_xml.dictCreator(inputString)
            csv_to_xml.StringsCreatorAndroid(csv_to_xml.dictionary)

        elif csv_to_xml.platform==0:
            csv_to_xml.dictCreator(inputString)
            csv_to_xml.StringsCreatorIOS(csv_to_xml.dictionary)

        elif csv_to_xml.platform == 2:
            csv_to_xml.dictCreator(inputString)
            csv_to_xml.ios_icon_font_variable_creator(csv_to_xml.dictionary)

        #csv_to_xml.csvCreator(csv_to_xml.dictionary)
        print("\nfinished")
        inputString=""
