from pprint import pprint
dict_txt = {}
count_lines_1 = 0
count_lines_2 = 0
count_lines_3 = 0
text_1 = ''
text_2 = ''
text_3 = ''

with open('files/1.txt') as f_1:
    lines = f_1.readlines()
    for line in lines:
        count_lines_1 += 1
        text_1 += line.strip('\n')
        dict_txt['1_txt'] = count_lines_1, text_1
with open('files/2.txt') as f_2:
    lines = f_2.readlines()
    for line in lines:
        count_lines_2 += 1
        text_2 += line.strip('\n')
        dict_txt['2_txt'] = count_lines_2, text_2
with open('files/3.txt') as f_3:
    lines = f_3.readlines()
    for line in lines:
        count_lines_3 += 1
        text_3 += line.strip('\n')
        dict_txt['3_txt'] = count_lines_3, text_3

pprint(dict_txt)

with open('4.txt', 'w') as f_4:
    f_4.write(f'{dict_txt}\n')