# import os.path
# import show
import pymysql

def modify():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='ys124126',
        database='students-sys'
    )
    cursor = db.cursor()
    # show.show()
    # if not os.path.exists('students.txt'):
    #     print('文件不存在或为空，请添加学生信息。')
    #     return

    while True:
        student_id = input('输入要修改的学生id: ')
        if not student_id:
            continue

        # with open('students.txt', 'r', encoding='UTF-8') as file:
        #     student_old = file.readlines()
        selcet_sql='select * from students where id=%s'
        cursor.execute(selcet_sql,student_id)
        student=cursor.fetchone()
        # flag = False
        if student:
            print('查找到对应学生信息，开始修改')
            try:
                name = input('输入姓名: ')
                english = int(input('输入英语成绩: '))
                python = int(input('输入python成绩: '))
                java = int(input('输入java成绩: '))
                grade = english + python+ java
                modify_sql='update students set name=%s,english=%s,python=%s,java=%s,grade=%s'
                modify_data=(name,english,python,java,grade)
                cursor.execute(modify_sql,modify_data)
                db.commit()
            except ValueError:
                print('输入信息错误')
        else:
            print('未找到学生信息')
        # updated_students = []
        # for item in student_old:
        #     d = dict(eval(item))
        #     if d['id'] == student_id:
        #         print('找到信息，开始修改')
        #         try:
        #             d['name'] = input('输入姓名: ')
        #             d['english'] = int(input('输入英语成绩: '))
        #             d['python'] = int(input('输入python成绩: '))
        #             d['java'] = int(input('输入java成绩: '))
        #             d['grade'] = d['english'] + d['python'] + d['java']
        #             flag = True
        #         except ValueError:
        #             print('输入错误，请输入有效的成绩')
        #             continue
        #
        #     updated_students.append(str(d) + '\n')
        #
        # if flag:
        #     with open('students.txt', 'w', encoding='UTF-8') as f:
        #         f.writelines(updated_students)
        #         print('修改完成')
        #
        # else:
        #     print('未找到该信息')
        answer = input('是否继续修改？(y/n): ')
        if answer != 'y':
            break
    cursor.close()
    db.close()


if __name__ == '__main__':
    modify()
