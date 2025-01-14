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
    h = add_zero(random.randrange(16) + 6)
    m = add_zero(random.randrange(59))
    s = add_zero(random.randrange(59))
    # print(f"{h}:{m}:{s}")
    return f"{h}:{m}:{s}"

def create_list_line(title, file_name):
    hms = get_random_clock()
    date8 = file_name.replace(".txt", "") # 20240625
    tempstr = f"6|6|{date8}|{title}|ENGLISH_TITLE|{date8[:4]}-{date8[4:6]}-{date8[6:8]}_{hms}|0\n"
    # 4|5|20240624|Reaper Preset Organizer について|Reaper Preset Organizer|2024-06-24_00:43:24|0
    # print(tempstr)
    return tempstr

def get_title_from_line_1(file_name):
    f = open(f"{INPUT_DIL}/{file_name}", "r", encoding='utf-8')
    lines = f.readlines()
    f.close()
    return lines[0].replace("\n", "")

def get_titles(file_names):
    titles = []
    for f in file_names:
        title = get_title_from_line_1(f)
        titles.append(title)
    return titles

def get_titles_with_filenames(file_names):
    title_arrays = []
    for f in file_names:
        title = get_title_from_line_1(f)
        title_arrays.append([f, title])
    return title_arrays

# def create_txt(doc):
#     f = open("output/converted.txt", "w", encoding='utf-8')
#     for paragraph in doc.paragraphs:
#         f.write(paragraph.text + "\n")
#     f.close()

# def open_docx(file_name):
#     document = docx.Document(f"{INPUT_DIL}/{file_name}")
#     create_txt(document)

# open_docx()

def convert_filenames(arr):
    new_arr = []
    for f in arr:
        new_title = f"20{f[:6]}.txt"
        if new_title in new_arr:
            print(f"ERROR: The title [{new_title}] already exists.")
            return False
        else:
            new_arr.append(new_title)
            # print(f"Added {new_title}")
    return new_arr

def mkdir_img(arr):
    for f in arr:
        path = f"{IMG_PATH}/{f[:8]}"
        os.mkdir(path)

def test_print_titles():
    fs = get_filenames()
    converted_fs = convert_filenames(fs)
    title_arrays = get_titles_with_filenames(fs)
    for title_array in title_arrays:
        print(f"{title_array[0]}: {title_array[1]}")

def test_check_title_conflict():
    fs = get_filenames()
    converted_fs = convert_filenames(fs)
    if converted_fs != False:
        print("No conflict:")
        print(converted_fs)

def for_my_lost_diary():
    fs = get_filenames()
    converted_fs = convert_filenames(fs)
    # mkdir_img(converted_fs) # success
    print_titles(get_titles(fs))
    # print(converted_fs)
    # for f in fs:


# get_filenames()
# print(get_filenames())
# print(get_random_clock())
# print(create_list_line("テストタイトル", "20190703"))
# for_my_lost_diary()
# test_check_title_conflict()
test_print_titles()