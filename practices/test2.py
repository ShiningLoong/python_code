# import requests

# response = requests.get("https://www.baidu.com/")
# print(response.content.decode("utf-8"))
response = b'\xc2\xbb'

with open("ccc.text", "w", encoding='utf8') as r:
    r.write(response.decode("utf-8"))
print(response.decode('utf8'))


# 1. in windows cmd/pycharm,  print() cannot print out some UTF char such as b'\xc2\xbb'
# error info : UnicodeEncodeError: 'gbk' codec can't encode character '\xbb' in position 0: illegal multibyte sequence
# But in python IDLE it can print out those characters normally
# in b'\xc2\xbb' , for a bytes string, it can only contain ASCII char inside the quotes, or use \xXX
# �ַ����������ڲ�ֻ��\x��ͷ��ʮ�����ƣ�����ʶ\o��
# �ַ����ڵ� \xXX ������ʮ�����ƣ�һ�ֽڣ�Ϊ�ָ����ʶ�� \x66\x77\x88
# �ַ����ڵ� \uXXXX ���ĸ�ʮ�����ƣ����ֽڣ�Ϊ�ָ�

