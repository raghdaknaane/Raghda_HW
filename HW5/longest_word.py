def long(file):

    file_read = open("my_id", "r")
    for line in file_read:
        lst = line.split()
        long_word = lst[0]
        for i in lst:
            if len(i) >= len(long_word):
                long_word = i
    print(long_word)


long("my_id")
