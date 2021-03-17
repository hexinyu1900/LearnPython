file_read = open("new.txt", 'r', encoding="utf-8")
file_write = open("renew.txt", 'w', encoding="utf-8")

while True:
  line_text = file_read.readline()
  file_write.write(line_text)
  if len(line_text)==0:
      break

file_write.close()
file_read.close()