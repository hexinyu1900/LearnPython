# 拆分
info_str = "hello,python,java"
print(info_str.split(','))  # 返回列表['hello', 'python', 'java']
print(info_str.split(',', 1))  # 指定切分次数1次，返回列表['hello', 'python,java']
print(info_str.split('python'))  # 返回列表['hello,', ',java']

# 转义字符：具有特殊功能的字符串
# \r 回车符    \t tab键       \n 换行符（linux和unix操作系统中换行符）        \r\n 换行符（Windows系统中换行符）
info_str = "hel\rlo,py\tth\non,ja va"
print(info_str.split())  # 返回列表['hel', 'lo,py', 'th', 'on,ja', 'va']

# 拓展：string.splitlines()按照行('\r'、'\n'、'\r\n')分隔，返回一个包含各行作为元素的列表
info_str = "he\rllo,py\rthon,j\r\nava"
print(info_str.splitlines())  # 返回列表['he', 'llo,py', 'thon,j', 'ava']

# 常用的字符串拼接
# string.join(seq)以string作为分隔符，将seq中所有的元素合并为一个新的字符串
my_str = "0123456789"
print('#'.join(my_str))
print('$'.join(my_str))
print(' '.join(my_str))
print(''.join(my_str))
print(my_str.join('####'))

# 字符串加法拼接+
str1 = "hello"
str2 = "eyes"
print(str1 + str2)
