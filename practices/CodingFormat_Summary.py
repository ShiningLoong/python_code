import sys
import io
import chardet
print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 不建议使用
print(b'\xc2\xbb'.decode('utf8'))
# with open('bbb.txt', 'w') as f:
#     f.write('\xc2\xbb')

# unicode码位 U+000000 - U+10FFFF ,它是一般性指导原则，为每个字符分配一个码位  总共1,114,112 个code point 17*2**16
# unicode 有17个码平面（plane）,0~16，每个包含65536个码位，最最常用的是第一个，称为BMP（Basic Multilingual Plane）
# utf8,utf16,utf32 是 unicode的具体实现
# UTF-8 可变长编码，1,112,064 个码位 , 17*2**16 - 2048,汉字一般为3个字节
# UTF-16 是对UCS-2的扩展，引入了代理码位surrogate code point,是可变长的(2字节或4字节)，1,112,064 个码位
# gb2312 gbk gb18030 是国内的汉字编码标准，从旧到新逐步扩展，GB标准的汉字码位与unicode没有对应关系，不能兼容
# GB 的标准能向下兼容，gb2312和gbk是两字节，gb18030包含一些更为罕见的字符，这些字符为4字节，其它与前两者兼容
# UCS 是ISO的标准，UNICODE是美国的标准，目前两套标准是同步的（可以视为一个标准）
# 由于 代理码位surrogate code point 的存在，UTF-16编码中的码位并不一定与unicode中的代码号 U+000000 - U+10FFFF对应
# UTF-32为了兼容UTF-16, 也受到了约束，许多码位不允许被使用
# UCS-4最早是ISO提出的32位编码标准，UTF-32原本是UCS-4的子集，但是由于历史原因，UCS-4也有诸多限制使用的码位
# 目前来看UCS-4可以视为和UTF-32等同
# 对于双字节和四字节的编码方式而言，UTF-16，UTF-32 等都需要考虑字节序的问题,所以要有字节序标记(BOM)
# BOM放在文档开头，UTF-8 不需要 BOM 来表明字节顺序，但可以用 BOM 来表明编码方式，UTF-8的BOM为EF BB BF
# UCS 规范建议我们在传输字节流前，先传输字符 "Zero Width No-Break Space"。这样如果接收者收到 FEFF
# ，就表明这个字节流是 Big-Endian 的；如果收到FFFE，就表明这个字节流是 Little- Endian 的。
