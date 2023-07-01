import os

path_to_folder = r"C:\Users\alexa\Desktop\HomeWork\hw_files\task_three\files"
directory = os.listdir(path_to_folder)

file_list = []
for file in directory:
    with open(os.path.join(path_to_folder, file), encoding='utf-8') as f:
        file_list.append(f.readlines())

id = 0
for list in file_list:
    list.insert(0, len(list))
    list.insert(0, directory[id])
    id += 1

sorted_file_list = file_list.sort(key=lambda x: len(x))

with open('result.txt', 'w', encoding='utf-8') as result_file:
    result_file.write(file_list[0][0] + '\n' + str(file_list[0][1]) + '\n' + ''.join(file_list[0][2:]) + '\n')
    result_file.write(file_list[1][0] + '\n' + str(file_list[1][1]) + '\n' + ''.join(file_list[1][2:]) + '\n')
    result_file.write(file_list[2][0] + '\n' + str(file_list[2][1]) + '\n' + ''.join(file_list[2][2:]) + '\n')