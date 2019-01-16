#_*_coding:utf-8_*_
# _Author : Chris
# Date :2018/11/11 15:34
# FileName : b64Plu.py

import base64,re,hashlib

def decode(content):
    try:
        result = base64.b64decode(content)
        try:
            result = result.decode('utf-8')
        except:
            result = result.decode('gb2312')
        return result
    except:
        return '该格式不为base64格式'

def encode(content):
    try:
        content = str(content)
        result=content.encode('gb2312')
        result=base64.b64encode(result)
        return result
    except:
        print('格式错误!')

def hashencode(content):
    hash = hashlib.md5()
    hash.update(bytes(content, encoding='utf-8'))
    return hash.hexdigest()

def str_to_hex(s):
    return ';'.join([hex(ord(c)).replace('0x', '&#x') for c in s])


# html格式的转换
def htmlcode(content):
    try:
        html_in_code = str(content)
        return str_to_hex(html_in_code)+';'
    except:
        return '转化错错误!'

def htmldecode(content):
    try:
        htmldecode = str(content)
        result=''
        for chars in htmldecode.split(';'): # 遍历每一个字符，将十六进制的格式进行转换
            if chars=='':break
            chars = chars.replace('&#x','')
            result +=str(chr(int(chars,16)))
        return result
    except Exception as e:
        return '转换错误!'


