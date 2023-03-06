def dic(my_id):
    new_dic = {}
    file_read = open("my_id", "r")
    for line in file_read:
        lst = line.split()
        for word in lst:
            if word in new_dic:
                new_dic[word] = new_dic[word] + 1
            else:
                new_dic[word] = 1
            for key in list(new_dic.keys()):
                new_dic.update({word: new_dic[key]})
    print(new_dic)


dic("my_id")
