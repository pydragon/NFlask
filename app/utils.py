__author__ = 'yangziling'

import hashlib

def hash_fun_1(str1):
    #创建一个hahsh对象并对str1加密
    m=hashlib.md5(str1.encode('utf-8'))
    print('获取加密的密文，16进制，无参数',m.hexdigest())
    print('获取加密的密文，二进制，无参数:',m.digest())
    print('获取hash块的大小:',m.block_size)
    print('hash密钥占多少个字节:',m.digest_size)
    print('查看当前获得的hash对象的加密算法',m.name)

    #更新密文
    m.update(str1.encode('utf-8'))
    print('获取加密的密文，16进制，无参数', m.hexdigest())
    print('获取加密的密文，二进制，无参数:', m.digest())
    print('获取hash块的大小:', m.block_size)
    print('hash密钥占多少个字节:', m.digest_size)
    print('查看当前获得的hash对象的加密算法', m.name)


def generate_hash(string):
    new_string = string.encode('ascii')
    sha256 = hashlib.sha256()
    sha256.update(new_string)
    return sha256.hexdigest()