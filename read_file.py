"""
read_file文件中主要内容为读取文件信息
将DES加密算法中的置换和混乱中的固定信息保存到文件中
将每个文件都设置为一个函数，便于查错
"""


def read_s(file_name):
    s = []
    with open('file/'+file_name) as file:
        temp = file.read().splitlines()
    for i in temp:
        s.append(i.split('\t'))
    return s


def read_bits():
    with open('file/Bits_rotated.txt') as file:
        bits_rotated = file.readline().split(' ')
        return bits_rotated


def read_pc1():
    l_key = []
    r_key = []
    with open('file/pc1.txt') as file:
        temp = file.read().splitlines()
    for i in range(4):
        l_key.append(temp[i].split('\t'))
    for i in range(4):
        r_key.append(temp[i+4].split('\t'))
    return l_key, r_key


def read_pc2():
    pc2 = []
    with open('file/pc2.txt') as file:
        temp = file.read().splitlines()
    for i in temp:
        pc2.append(i.split('\t'))
    return pc2


def read_ip():
    ip = []
    with open('file/IP.txt') as file:
        temp = file.read().splitlines()
    for i in temp:
        ip.append(i.split(','))
    return ip


def read_ip1():
    ip1 = []
    with open('file/IP_1.txt') as file:
        temp = file.read().splitlines()
    for i in temp:
        ip1.append(i.split(','))
    return ip1


def read_expansion():
    expansion = []
    with open('file/expansion.txt') as file:
        temp = file.read().splitlines()
    for i in temp:
        expansion.append(i.split('\t'))
    return expansion


def read_p():
    p = []
    with open('file/p.txt') as file:
        temp = file.read().splitlines()
    for i in temp:
        p.append(i.split('\t'))
    return p


if __name__ == '__main__':
    read_pc1()
    read_expansion()
