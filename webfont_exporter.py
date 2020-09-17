# **********************************
# * Created by Yigit Can Yilmaz    *
# * 17 Sep 2020                    *
# **********************************
import os


def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


def get_output(dict_icons, file_path):
    if file_path.find("style.css") > 0:
        output_path = file_path[0:len(file_path) - 9]
    else:
        output_path = file_path

    if output_path[len(output_path) - 1] != "\\" or output_path[len(output_path) - 1] != "/":
        if output_path.find("/") > 0:
            output_path += "/"
        else:
            output_path += "\\"

    output_file_android = open(output_path + "android_icons.txt", "w", encoding="UTF-8")
    output_file_ios = open(output_path + "ios_icons.txt", "w", encoding="UTF-8")
    temp_android = ""
    temp_ios = ""
    for i in dict_icons.keys():
        temp_android += "<string name=\"" + i + "\">&#x" + dict_icons[i] + ";</string>\n"
        temp_ios += "public let " + i + " = String(format: \"%C\", 0x" + dict_icons[i] + ")\n"
    output_file_android.write(temp_android)
    output_file_ios.write(temp_ios)
    output_file_android.close()
    output_file_ios.close()


def get_icon_names(file_path):
    dict_icons = {}
    if file_path.find("style.css") > 0:
        input_file = open(file_path, "r", encoding="UTF-8")
    else:
        if file_path[len(file_path) - 1] != "\\" or file_path[len(file_path) - 1] != "/":
            if file_path.find("/") > 0:
                file_path += "/style.css"
            else:
                file_path += "\\style.css"
        input_file = open(file_path, "r", encoding="UTF-8")
    temp = input_file.read()
    input_file.close()
    start_index = 0
    while True:
        if temp.find("\n.", start_index) == 0 or temp.find("\n.", start_index) < start_index:
            break
        else:
            start_index = temp.find("\n.", start_index) + 2
            name = temp[start_index: temp.find(":before", start_index)]
            while name.find("-") > 0:
                name = name.replace("-", "_")
            start_index = temp.find("content: \"\\", start_index) + 11
            value = temp[start_index: temp.find("\"", start_index)]
            dict_icons[name] = value

    return dict_icons
