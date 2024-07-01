dict_txt = {}
count_lines = 0
with open('4.txt', 'w') as f_4:
    with open('files/1.txt') as f_1:
        lines = f_1.readlines()
        for line in lines:
            count_lines += 1
            dict_txt['1_txt']=count_lines, line

print(dict_txt)






# with open('2.txt') as f_2:
#     lines = f_2.readlines()
#     for line in lines:
#         f_4.write(line)
# with open('3.txt') as f_3:
#     lines = f_3.readlines()
#     for line in lines:
#         f_4.write(line)