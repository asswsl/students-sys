def save(list):
    try:
        stu_text = open('students.txt', 'a', encoding='UTF-8')
    except:
        stu_text = open('students.txt', 'w', encoding='UTF-8')
    for item in list:
        stu_text.write(str(item) + '\n')
    stu_text.close()


if __name__ == '__main__':
    my_list = [1, 2, 3]
    save(my_list)
