import os.path

import show


def modify():
    show.show()
    if not os.path.exists('students.txt'):
        print('文件不存在或为空，请添加学生信息。')
        return

    while True:
        student_id = input('输入要修改的学生id: ')
        if not student_id:
            continue

        with open('students.txt', 'r', encoding='UTF-8') as file:
            student_old = file.readlines()

        flag = False
        updated_students = []

        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到信息，开始修改')
                try:
                    d['name'] = input('输入姓名: ')
                    d['english'] = int(input('输入英语成绩: '))
                    d['python'] = int(input('输入python成绩: '))
                    d['java'] = int(input('输入java成绩: '))
                    d['grade'] = d['english'] + d['python'] + d['java']
                    flag = True
                except ValueError:
                    print('输入错误，请输入有效的成绩')
                    continue

            updated_students.append(str(d) + '\n')

        if flag:
            with open('students.txt', 'w', encoding='UTF-8') as f:
                f.writelines(updated_students)
                print('修改完成')

        else:
            print('未找到该信息')

        answer = input('是否继续修改？(y/n): ').lower()
        if answer != 'y':
            break


if __name__ == '__main__':
    modify()
