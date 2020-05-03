import produce_Ki
import read_file
import time
import my_encodings


# 切片（将明文或密文按照64位为一组切片操作）
def segmentation(plaintext):
    plaintext_string = []
    length = len(plaintext)
    remainder = length % 64
    if remainder != 0:
        str1 = ''
        temp = str1.join([str1 + '0' for i in range(64 - remainder)])
        plaintext = plaintext + temp
    number = len(plaintext) // 64
    for i in range(number):
        plaintext_string.append(plaintext[i * 64:(i + 1) * 64])
    return plaintext_string


# 扩展（）
def expansion(r_plaintext):
    temp = ''
    expansion_table = read_file.read_expansion()
    for i in expansion_table:
        for j in i:
            temp = temp + r_plaintext[int(j) - 1]
    return temp


# S盒
def s_box(param, i):
    filename = 's' + str(i) + '.txt'
    s_boxes = read_file.read_s(filename)
    temp = list(map(lambda x: str(x), param))
    col = int(temp[0] + temp[5], 2)
    row = int(''.join(temp[1:5]), 2)
    bin_temp = bin(int(s_boxes[col][row])).replace('0b', '')
    bin1 = bin_temp.zfill(4)
    return bin1


# P置换
def p_replacement(plaintext):
    temp = ''
    p = read_file.read_p()
    for i in p:
        for j in i:
            temp = temp + plaintext[int(j) - 1]
    return temp


# F函数
def f_function(l_plaintext, r_plaintext, ki):
    expansion_plaintext = expansion(r_plaintext)
    result_xor = map(lambda x, y: x ^ y,
                     map(lambda x: int(x), list(expansion_plaintext)),
                     map(lambda x: int(x), list(ki)))
    str1 = ''
    result_xor = list(result_xor)
    for i in range(8):
        result_s = s_box(result_xor[i * 6:(i + 1) * 6], i + 1)
        str1 = str1 + result_s
    p_replacement_result = p_replacement(str1)
    l_plaintext1 = map(lambda x, y: x ^ y,
                       map(lambda x: int(x), list(l_plaintext)),
                       map(lambda x: int(x), list(p_replacement_result)))
    l_plaintext1 = ''.join(map(lambda x: str(x), l_plaintext1))
    return r_plaintext, l_plaintext1


# 初始置换（IP）
def pre_replacement(plaintext):
    temp = ''
    ip = read_file.read_ip()
    for i in ip:
        for j in i:
            temp = temp + plaintext[int(j) - 1]
    return temp


# 逆置换（IP-1）
def suffix_replacement(l_temp, r_temp):
    keys = r_temp + l_temp
    temp = ''
    ip1 = read_file.read_ip1()
    for i in ip1:
        for j in i:
            temp = temp + keys[int(j) - 1]
    return temp


# 加密
def encode(plaintext, key):
    ki = produce_Ki.produce(key)  # 生成子密钥
    plaintext1 = segmentation(plaintext)  # 密文切片
    cipher_text = ''
    for i in plaintext1:
        pre_replacement_plaintext = pre_replacement(i)
        l_temp = pre_replacement_plaintext[0: 32]
        r_temp = pre_replacement_plaintext[32: 64]
        for j in range(16):
            l_temp, r_temp = f_function(l_temp, r_temp, ki[j])
        cipher_text = cipher_text + suffix_replacement(l_temp, r_temp)
    return cipher_text


# 解码
def decode(cipher_text, key):
    ki = produce_Ki.produce(key)  # 生成子密钥
    cipher_text_string = segmentation(cipher_text)  # 密文切片
    plain_text = ''
    for i in cipher_text_string:
        pre_replacement_cipher_text = pre_replacement(i)
        l_temp = pre_replacement_cipher_text[0:32]
        r_temp = pre_replacement_cipher_text[32:64]
        for j in range(16):
            l_temp, r_temp = f_function(l_temp, r_temp, ki[15 - j])
        plain_text = plain_text + suffix_replacement(l_temp, r_temp)
    return plain_text


def begin(text, key, category):
    if category == 0:
        myself_encode_plaintext = my_encodings.out_put(text, 0)
        myself_encode_key = my_encodings.out_put(key, 1)
        start_time = time.time()
        encode_result = encode(myself_encode_plaintext, myself_encode_key)
        end_time = time.time()
        with open('web/result.txt', 'w') as file:
            file.write(encode_result)
            file.write('\n')
            file.write('the speed time of encoding:' + str(end_time - start_time))
    else:
        my_self_encode_key = my_encodings.out_put(key, 1)
        start_time = time.time()
        decode_result = decode(text, my_self_encode_key)
        end_time = time.time()
        my_self_decode_plaintext = my_encodings.in_put(decode_result)
        with open('web/result1.txt', 'w') as file:
            file.write(my_self_decode_plaintext)
            file.write('\n')
            file.write('the speed time of decoding:' + str(end_time - start_time))

