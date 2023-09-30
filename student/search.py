import os.path
import show
import pymysql
def search():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='ys124126',
        database='students-sys'
    )
    cursor = db.cursor()
    show.show()
    while True:
        student_id = input('输入要查找的学生id')
        search_sql='select * from students where id=%s'
        cursor.execute(search_sql,student_id)
        student=cursor.fetchone()
        if student:
            id = student[0]
            name = student[1]
            english = student[2]
            python = student[3]
            java = student[4]
            grade = student[5]
            print(f'id:{id}  name:{name}  english:{english}  python:{python}  java:{java}  grade:{grade}')
        else:
            print('未查找到该学生信息')
        # if os.path.exists('students.txt'):  # 判断文件路径是否正确
        #     with open('students.txt', 'r', encoding='UTF-8') as file:
        #         student_old = file.readlines()  # 逐行读取文件内容
        # else:
        #     print('文件内容为空')
        #     return
        # flag = False
        # for item in student_old:
        #     d = dict(eval(item))
        #     if d['id'] == student_id:
        #         print('查找成功')
        #         print(
        #             'id:' + str(d['id']) + '  name:' + str(d['name']) + '  english:' + str(
        #                 d['english']) + '  python:' +
        #             str(d['python']) + '  java:' + str(d['java']))
        #         flag = True
        #         break
        #     else:
        #         continue
        # if flag:
        #     print('查找成功')
        # else:
        #     print('未查找到该学生')
        answer = input('是否继续查找？y/n')
        if answer == 'y':
            continue
        else:
            break
    cursor.close()
    db.close()


if __name__ == '__main__':
    search()
