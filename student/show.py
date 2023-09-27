import os.path


def show():
    while True:
        if os.path.exists('students.txt'):
            with open('students.txt', 'r', encoding='UTF-8') as f:
                student_old = f.readlines()
        else:
            print('路径错误')
            return
        for item in student_old:
            d = dict(eval(item))
            print(
                'id:' + str(d['id']) + '  name:' + str(d['name']) + '  english:' + str(
                    d['english']) + '  python:' +
                str(d['python']) + '  java:' + str(d['java']))
        break


if __name__ == '__main__':
    show()
