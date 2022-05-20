import os

BASE_PATH = os.getcwd()
FILE_NAME = '1.txt'
WORK_DRECTORY = 'Task7_3\Text'
os.chdir(os.path.join(BASE_PATH, WORK_DRECTORY))
BASE_PATH = os.getcwd()
list_file =os.listdir()
count_line = []
all_info = {}
for i in list_file:
    path = os.path.join(BASE_PATH, i)
    stroke = []
    count_line_file = 1
    text = {}
    with open (path, encoding='utf-8') as file:
        for line in file:
            count_line_file += (line.count('\n'))
            stroke.append(line) 
        text [i] = stroke
    all_info[count_line_file] = text
    count_line.append(count_line_file)
count_line.sort()
os.remove('D:\Python\Task7_3\generally.txt')
for i in count_line:
    text_build = {}
    for key, value in all_info.items():
        if key == i:
            text_build = (all_info.get(i)).copy()
            for name_file, text_file in text_build.items():
                with open ('D:\Python\Task7_3\generally.txt', 'a', encoding='utf-8') as file_general:
                    file_general.write(str(name_file))
                    file_general.write('\n')
                    file_general.write(str(key))
                    file_general.write('\n')
                    for txt in text_file:
                        file_general.write(txt)
                    file_general.write('\n')
