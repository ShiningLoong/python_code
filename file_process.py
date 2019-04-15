 # The argument mode points to a string beginning with one of the following
 # sequences (Additional characters may follow these sequences.):
 #
 # ``r''   Open text file for reading.  The stream is positioned at the
 #         beginning of the file.
 #
 # ``r+''  Open for reading and writing.  The stream is positioned at the
 #         beginning of the file.
 #
 # ``w''   Truncate file to zero length or create text file for writing.
 #         The stream is positioned at the beginning of the file.
 #
 # ``w+''  Open for reading and writing.  The file is created if it does not
 #         exist, otherwise it is truncated.  The stream is positioned at
 #         the beginning of the file.
 #
 # ``a''   Open for writing.  The file is created if it does not exist.  The
 #         stream is positioned at the end of the file.  Subsequent writes
 #         to the file will always end up at the then current end of file,
 #         irrespective of any intervening fseek(3) or similar.
 #
 # ``a+''  Open for reading and writing.  The file is created if it does not
 #         exist.  The stream is positioned at the end of the file.  Subse-
 #         quent writes to the file will always end up at the then current
 #         end of file, irrespective of any intervening fseek(3) or similar.
         
         
with open(r".\1.txt", "r+") as f:
    f.write("12345")
    f.write("6789999999999999999999")


with open(r".\1.txt", "w+") as f:
    f.write("2222222222222")


with open(r".\1.txt", "r+") as f:
    f.write("33333333333")

with open(r".\1.txt", "r+") as f:
    f.write("33333333333")

# with open(r".\1.txt", "rb+") as f:
#     f.write(b"33333333333")
#     print(b"333333333333", file=f)

# with open(r".\1.txt", "rb+") as f:
#     f.write("简体繁體\r".encode('utf-8'),)

with open(r".\1.txt", "r+") as f:
    print("简体繁體", file=f)
    # f.write("简体繁體")

with open(r".\1.txt", "r+") as f:
    print(f.tell())
    data = f.read()
    print(data)
    f.seek(0)
    data = data.replace('\r', "")
    print(bytes(data, encoding='gbk'))  # 这里没有\r
    f.truncate()
    f.write(data)  # 这里自动添加了\r

with open(r".\1.txt", "rb+") as f:
    data = f.read()
    print(data)   # 这里有\r
    print(data.decode('gbk'))


# 打开文件进行操作时需要注意：
# 1. 打开时position的值，是开头还是末尾;打开文件时文件不存在会怎么样，文件已存在会怎么样
# 2. 打开读取时采取什么编码读入，写入时采取什么编码写入
# 3. 使用b参数读入和写入的值都是明确的和可控的,不用考虑编码（或者说编码都已明确指出）
# 4. 不使用b参数， 读取和写入的值都经过了默认的编码转换，需要考虑使用的到底是什么编码, \r\n的换行符也不受控制，有时会被篡改。
# 5. python3 的str 是以unicode编码方式存储

