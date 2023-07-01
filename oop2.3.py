sum_line = {}
d = []

with open('1.txt', 'rt', encoding='utf-8') as f_1:
    sum_line_1 = {}
    counting_1 = 0
    for line in f_1.readlines():
        counting_1 += 1
        sum_line_1['f_1'] = counting_1
    d.append(counting_1)
    # print(sum_line_1)

with open('2.txt', 'rt', encoding='utf-8') as f_1:
    sum_line_2 = {}
    counting_2 = 0
    for line in f_1.readlines():
        counting_2 += 1
        sum_line_2['f_2'] = counting_2
    d.append(counting_2)
    # print(sum_line_2)

with open('3.txt', 'rt', encoding='utf-8') as f_1:
    sum_line_3 = {}
    counting_3 = 0
    for line in f_1.readlines():
        counting_3 += 1
        sum_line_3['f_3'] = counting_3
    d.append(counting_3)
    # print(sum_line_3)

# sum_line = sorted(zip(sum_line_1, sum_line_2, sum_line_3))
d.sort()
print(d)
print(sum_line)