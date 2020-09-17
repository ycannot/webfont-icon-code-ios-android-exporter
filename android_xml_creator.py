import webfont_exporter


def get_output(dict_icons, file_path, font_family):
    if file_path.find("style.css") > 0:
        output_path = file_path[0:len(file_path) - 9]
    else:
        output_path = file_path

    if output_path[len(output_path) - 1] != "\\" or output_path[len(output_path) - 1] != "/":
        if output_path.find("/") > 0:
            output_path += "/"
        else:
            output_path += "\\"

    output_file_android = open(output_path + "android_layout.xml", "w", encoding="UTF-8")

    layout_open = "<ScrollView\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"match_parent\"\nandroid:orientation=\"vertical\"\nxmlns:android=\"http://schemas.android.com/apk/res/android\">\n<LinearLayout\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"wrap_content\"\nandroid:orientation=\"vertical\" >\n "
    layout_close = "</LinearLayout>\n</ScrollView>"
    output = ""
    temp = ""
    count = 0
    for i in dict_icons.keys():
        count += 1
        temp += "<TextView\nandroid:id = \"@+id/" + i + "\"\nandroid:layout_width = \"20dp\"\nandroid:layout_height = " \
                                                        "\"20dp\"\nandroid:gravity = \"center_vertical\"\nandroid:text = \"@string/" + i + "\"\nandroid:fontFamily =" \
                                                                                                                                           " \"" + font_family + "\" />\n"
        if count % 20 == 0 or count == len(dict_icons.keys()):
            output += "<LinearLayout\nandroid:layout_width=\"match_parent\"\nandroid:layout_height=\"wrap_content\"\nandroid:orientation=\"horizontal\" >\n " + temp + "</LinearLayout>\n"
            temp = ""
    output_file_android.write(layout_open + output + layout_close)

    output_file_android.close()


def get_layout_and_fonts():
    inp = str(input("Please enter a filepath of style.css of webfont(ex: C:\\Users\\can\\Desktop): "))
    path = inp
    inp = str(input("Please enter webfont fontFamily (ttf) name (ex: @font/groupama_icons): "))
    font_family = inp
    dict_icon = webfont_exporter.get_icon_names(path)
    webfont_exporter.get_output(dict_icon, path)
    get_output(dict_icon, path, font_family)
    return path
