__author__ = 'yangziling'

import hashlib

def hash_fun_1(str1):
    #����һ��hahsh���󲢶�str1����
    m=hashlib.md5(str1.encode('utf-8'))
    print('��ȡ���ܵ����ģ�16���ƣ��޲���',m.hexdigest())
    print('��ȡ���ܵ����ģ������ƣ��޲���:',m.digest())
    print('��ȡhash��Ĵ�С:',m.block_size)
    print('hash��Կռ���ٸ��ֽ�:',m.digest_size)
    print('�鿴��ǰ��õ�hash����ļ����㷨',m.name)

    #��������
    m.update(str1.encode('utf-8'))
    print('��ȡ���ܵ����ģ�16���ƣ��޲���', m.hexdigest())
    print('��ȡ���ܵ����ģ������ƣ��޲���:', m.digest())
    print('��ȡhash��Ĵ�С:', m.block_size)
    print('hash��Կռ���ٸ��ֽ�:', m.digest_size)
    print('�鿴��ǰ��õ�hash����ļ����㷨', m.name)


def generate_hash(string):
    new_string = string.encode('ascii')
    sha256 = hashlib.sha256()
    sha256.update(new_string)
    return sha256.hexdigest()