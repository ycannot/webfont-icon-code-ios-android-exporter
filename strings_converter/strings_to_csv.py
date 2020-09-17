# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:36:57 2020

@author: yigit
"""
import time
from os import system, name

class xml_to_csv:
    dictionary={}   #dictCreator functions update this dictionary
    platform=-1  #platform==False is Android, platform==true IOS
    platform_list=["IOS","Android"]
    selected_platform="Android"
    languages=["tr"]
    def __init__(self,platform=""):
        if platform=="":
            while xml_to_csv.platform not in [0,1]:
                try:
                    xml_to_csv.platform=int(input("Welcome, \nPlease Locate Your Translation Files in the Same Directory With This Tool.(Ctrl+double tap C to Exit)\n0.IOS\n1.Android\nSelect a Platform: "))
                    #input("\nPlatform Was Set as Android. Please Press Enter to Continue or Ctrl+C to exit.")                
                    xml_to_csv.selected_platform=xml_to_csv.platform_list[xml_to_csv.platform]
                    
                        
                except:
                    xml_to_csv.platform=-1
                    xml_to_csv.clear()
                    time.sleep(0.5)
                    print("\n\n** Please enter either 0(IOS) or 1(Android). **\n\n")
                    time.sleep(2)
        else:
            xml_to_csv.platform=platform
        xml_to_csv.main()
        
    def dictCreatorAndroid(inputString):
        cursor=0
        inputString=inputString.replace("\n","",inputString.count("\n"))
        while(inputString.count("name=\"",cursor)>0):
            name_start_index=inputString.find("name=\"",cursor)+6
            cursor=name_start_index
            name_end_index=inputString.find("\">",cursor)
            cursor=name_end_index+2
            string_start_index=cursor
            string_end_index=inputString.find("</string>",cursor)
            cursor=string_end_index+9
            
            if inputString[name_start_index:name_end_index] not in xml_to_csv.dictionary:
                xml_to_csv.dictionary[inputString[name_start_index:name_end_index]]=[]
                xml_to_csv.dictionary[inputString[name_start_index:name_end_index]].append(inputString[string_start_index:string_end_index])
            else:
                xml_to_csv.dictionary[inputString[name_start_index:name_end_index]].append(inputString[string_start_index:string_end_index])
    def dictCreatorIOS(inputString):
        inputString=inputString.replace(";\n",";\ğ",inputString.count(";\n"))
        inputString=inputString.replace("\"","",inputString.count("\""))
        if inputString.count("*/")>0:
            inputString=inputString[0:inputString.find("*/")+2]
        lines = inputString.split(";\ğ")
        for i in lines:
            if i.count(" = ")>0:
                temp=i.split(" = ")
            else:
                temp=i.split("=")
           
            if len(temp)==2:
                if temp[0] not in xml_to_csv.dictionary:
                    xml_to_csv.dictionary[temp[0]]=[]
                    xml_to_csv.dictionary[temp[0]].append(temp[1])
                    
                else:
                    
                    xml_to_csv.dictionary[temp[0]].append(temp[1])
            
            
        #print(lines)
        
    def clear(): 
        # for windows 
        
        if name == 'nt': 
            system('cls') 
      
        # for mac and linux(here, os.name is 'posix') 
        else: 
            system('clear') 
    
    def csvCreator(d):
        lines=[]
        for i in d:
            temp="\n"+i
            for j in d[i]:
                temp+=";"+j
            lines.append(temp)
        file=open("strings.csv", "w", encoding="UTF-8")
        try:
            file.writelines(lines)
        finally:
            file.close()
    
    def fileOperation(filename,operation,output_string=""):
        #operation is "r", "w", etc.
        if operation=="r":
            input_file=open(filename,operation, encoding="UTF-8")
            temp=input_file.read()
            input_file.close()
            return temp
        elif operation=="w":
            output_file=open(filename,operation, encoding="UTF-8")
            temp=input_file.write(output_string)
            output_file.close()
        else:
            raise ValueError('\nPlease check fileOperation function.')
        
    def main():    
        #print(xml_to_csv.platform)
        
        if xml_to_csv.platform==1:
            for i in xml_to_csv.languages:
                try:
                    print()
                    inputString=str(xml_to_csv.fileOperation("strings_"+i+".xml","r"))
                    print(i, "strings are parsing...")
                    xml_to_csv.dictCreatorAndroid(inputString)
                    print(i, "strings are done.")
                except:
                    raise ValueError("\n***Error:strings_"+i+".xml couldn't found or an read error happened. Please check the file.")
                
            
        elif xml_to_csv.platform==0:
            for i in xml_to_csv.languages:
                try:
                    print()
                    inputString=str(xml_to_csv.fileOperation("Localizable_"+i+".strings","r"))
                    print(i, "strings are parsing...")
                    xml_to_csv.dictCreatorIOS(inputString)
                    print(i, "strings are done.")
                except:    
                    raise ValueError("\n***Error:Localizable_"+i+".strings couldn't found or an read error happened. Please check the file.")
                    
        xml_to_csv.csvCreator(xml_to_csv.dictionary)
        #print(xml_to_csv.dictionary)
        inputString=""
        print("\nfinished")
        
        
    
