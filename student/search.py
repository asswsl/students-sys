import os.path


def search():
    while True:
        student_id = input('输入要查找的学生id')
        if os.path.exists('students.txt'):  # 判断文件路径是否正确
            with open('students.txt', 'r', encoding='UTF-8') as file:
                student_old = file.readlines()  # 逐行读取文件内容
        else:
            print('文件内容为空')
            return
        flag = False
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('查找成功')
                print(
                    'id:' + str(d['id']) + '  name:' + str(d['name']) + '  english:' + str(
                        d['english']) + '  python:' +
                    str(d['python']) + '  java:' + str(d['java']))
                flag = True
                break
            else:
                continue
        if flag:
            print('查找成功')
        else:
            print('未查找到该学生')
        answer = input('是否继续查找？y/n')
        if answer == 'y':
            continue
        else:
            break


if __name__ == '__main__':
    search()
