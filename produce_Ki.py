"""
生产子密钥（K1 -- K16）
"""

import read_file


def produce_ki(bits, l_key, r_key):
    ki = ''
    l_key1 = l_key[bits:]+l_key[:bits]
    r_key1 = r_key[bits:]+r_key[:bits]
    temp1 = l_key1 + r_key1
    pc2 = read_file.read_pc2()
    for i in pc2:
        for j in i:
            ki = ki + temp1[int(j)-1]
    return ki, l_key1, r_key1


def produce(key):
    k_i = []
    temp_key = key
    pc1 = read_file.read_pc1()
    l_key = ''
    for i in pc1[0]:
        for j in i:
            l_key = l_key + temp_key[int(j)-1]
    r_key = ''
    for i in pc1[1]:
        for j in i:
            r_key = r_key + temp_key[int(j)-1]
    bits_rotated = read_file.read_bits()
    for i, bits in enumerate(bits_rotated):
        ki, l_key, r_key = produce_ki(int(bits), l_key, r_key)
        k_i.append(ki)
    return k_i

