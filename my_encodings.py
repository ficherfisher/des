"""
用于处理明文，密钥与二进制之间的转化
"""


# 生成映射表
def create_mapping_table():
    mapping_table = []
    temp1 = {'number': 0, 'letter': ' '}
    mapping_table.append(temp1)
    for number, letter in enumerate(range(48, 58), 1):
        temp = {'number': number, 'letter': chr(letter)}
        mapping_table.append(temp)
    for number, letter in enumerate(range(65, 91), 11):
        temp = {'number': number, 'letter': chr(letter)}
        mapping_table.append(temp)
    for number, letter in enumerate(range(97, 123), 37):
        temp = {'number': number, 'letter': chr(letter)}
        mapping_table.append(temp)
    return mapping_table


# 输入转化
def out_put(string, category):
    mapping_tables = create_mapping_table()
    str1 = ''
    for i in list(string):
        for j in mapping_tables:
            if j['letter'] == i:
                temp = bin(j['number']).replace('0b', '')
                str1 = str1 + temp.zfill(6)
    if category == 1:  # 判断是否为生成密钥时的转化(1表示密钥， 0表示明文)
        if len(str1) > 64:
            str1 = str1[0:64]
        elif len(str1) < 64:
            str1 = str1 + ''.join(['0'+'' for i in range(64 - len(str1))])
    return str1


# 输出转化
def in_put(string):
    segmentation = []
    remainder = len(string) % 6
    if remainder != 0:
        temp = ''.join('0'+'' for i in range(6 - remainder))
        string = string + temp
    for i in range(len(string) // 6):
        segmentation.append(string[i*6:(i+1)*6])
    result = ''
    mapping_table = create_mapping_table()
    for i in segmentation:
        for j in mapping_table:
            if int(i, 2) == j['number']:
                result = result + j['letter']
    return result



