import os.path
import show
import pymysql
def delete():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='ys124126',
        database='students-sys'
    )
    cursor = db.cursor()
    show.show()
    while True:
        student_id = input('输入要删除的学生id')
        selcet_sql = 'select * from students where id=%s'
        cursor.execute(selcet_sql, student_id)
        student = cursor.fetchone()
        delete_sql='delete from students where id=%s'
        if student:
            cursor.execute(delete_sql,student_id)
            db.commit()
            show.show()
        else:
            print('没有查找到该学生信息')
        # if student_id != '':
        #     if os.path.exists('students.txt'):  # 判断文件路径是否正确
        #         with open('students.txt', 'r', encoding='UTF-8') as file:
        #             student_old = file.readlines()  # 逐行读取文件内容
        #             # print(student_old)
        #     else:
        #         student_old = []
        # flag = False
        # if student_old:  # 当读取到文件内容
        #     with open('students.txt', 'w', encoding='UTF-8') as f:  # 以覆写方式打开文件
        #         d = {}
        #         for item in student_old:
        #             d = dict(eval(item))  # eval 将文件内容转换为python代码 dict 将代码转为字典格式
        #             # print(d)
        #             if d['id'] != student_id:  # 不等于要删除的id 则写入文件
        #                 f.write(str(d) + '\n')
        #             else:
        #                 flag = True  # id为删除id时 标记为True
        #         if flag:
        #             print(f'{student_id}已删除')
        #         else:
        #             print(f'未找到{student_id}的学生')
        # else:  # 写入的文件路径中不存在对应文件 无法读取到信息
        #     print('未读取到学生信息')
        #     break
        answer = input('是否继续删除？y/n')
        if answer == 'y':
            continue
        else:
            break
    cursor.close()
    db.close()

if __name__ == '__main__':
    delete()
