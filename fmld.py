import docx
import os
import random

INPUT_DIL = "input"
IMG_PATH = "output/img"

def get_filenames():
    # dir_path = "input"
    file_names = [
        f for f in os.listdir(INPUT_DIL) if os.path.isfile(os.path.join(INPUT_DIL, f))
    ]
    # print(file_names)
    return file_names

def add_zero(num):
    if num < 10:
        return f"0{num}"
    else:
        return str(num)

def get_random_clock():
    h = add_zero(random.randrange(23))
    m = add_zero(random.randrange(59))
    s = add_zero(random.randrange(59))
    # print(f"{h}:{m}:{s}")
    return f"{h}:{m}:{s}"

def create_list_line(title, file_name):
    hms = get_random_clock()
    date6 = file_name.replace(".docx", "") # 240625
    tempstr = f"6|6|20{date6}|{title}|ENGLISH_TITLE|20{date6[:2]}-{date6[2:4]}-{date6[4:6]}_{hms}|0\n"
    # 4|5|20240624|Reaper Preset Organizer について|Reaper Preset Organizer|2024-06-24_00:43:24|0
    # print(tempstr)
    return tempstr

def create_txt(doc):
    f = open("output/converted.txt", "w", encoding='utf-8')
    for paragraph in doc.paragraphs:
        f.write(paragraph.text + "\n")
    f.close()

def open_docx(file_name):
    document = docx.Document(f"{INPUT_DIL}/{file_name}")
    create_txt(document)

# open_docx()

def convert_filenames(arr):
    new_arr = []
    for f in arr:
        new_title = f"20{f[:6]}.txt"
        if new_title in new_arr:
            print(f"ERROR: The title [{new_title}] already exists.")
            break
        else:
            new_arr.append(new_title)
            # print(f"Added {new_title}")
    return new_arr

def mkdir_img(arr):
    for f in arr:
        path = f"{IMG_PATH}/{f[:8]}"
        os.mkdir(path)

def for_my_lost_diary():
    fs = get_filenames()
    converted_fs = convert_filenames(fs)
    mkdir_img(converted_fs)
    # print(converted_fs)
    # for f in fs:


# get_filenames()
# print(get_filenames())
# print(create_list_line("テストタイトル", "190703"))
for_my_lost_diary()