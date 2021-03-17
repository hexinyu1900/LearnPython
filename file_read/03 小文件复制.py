file_read = open("new.txt", 'r', encoding="utf-8")
file_write = open("renew.txt", 'w', encoding="utf-8")

text = file_read.read()
file_write.write(text)

file_write.close()
file_read.close()