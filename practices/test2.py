import io
import sys
with open('tttt.text', 'wb') as f:
    f.write("漢字".encode('gbk'))
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# print(b'\xc2\xbb'.decode('gb18030'))

# with open('tttt.text', 'rb') as f:
#     d = f.read()

# print(d.decode('utf8'))
