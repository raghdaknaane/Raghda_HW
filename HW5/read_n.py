def read(n):

    file_read = open("my_id", "r")
    file_read = file_read.readlines()
    for text in (file_read[:n]):
        print(text)


read(1)
