import pymysql
import show
# import save


def insert():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='ys124126',
        database='students-sys'
    )
    cursor = db.cursor()
    insert_sql = 'insert into students(id,name,english,python,java,grade) values (%s,%s,%s,%s,%s,%s)'
    student_list = []
    while True:
        show.show()
        id = input('输入id')
        if not id:  # 如果为空，结束循环
            break
        name = input('输入姓名')
        if not name:
            break
        try:
            english = int(input('输入英语成绩'))
            python = int(input('输入python成绩'))
            java = int(input('输入java成绩'))
            grade = english + python + java
        except:
            print('输入有误')
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java, 'grade': grade}
        insert_data = (
        student['id'], student['name'], student['english'], student['python'], student['java'], student['grade'])
        cursor.execute(insert_sql, insert_data)
        db.commit()
        # student_list.append(student)
        answer = input('是否继续输入?y/n')
        if answer == 'y':
            continue
        else:
            cursor.close()
            db.close()
            break
    # 在停止输入以后，统一写入文件中
    # save.save(student_list)
    print('插入信息完毕')
    show.show()


if __name__ == '__main__':
    insert()
