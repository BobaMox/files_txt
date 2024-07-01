dict_txt = {}
count_lines_1 = 0
count_lines_2 = 0
count_lines_3 = 0


with open('files/1.txt') as f_1:
    lines = f_1.readlines()
    for line in lines:
        count_lines_1 += 1
        dict_txt['1_txt'] = count_lines_1, line
with open('files/2.txt') as f_2:
    lines = f_2.readlines()
    for line in lines:
        count_lines_2 += 1
        dict_txt['2_txt'] = count_lines_2, line
with open('files/3.txt') as f_3:
    lines = f_3.readlines()
    for line in lines:
        count_lines_3 += 1
        dict_txt['3_txt'] = count_lines_3, line

print(dict_txt)