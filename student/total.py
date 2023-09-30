import pymysql


def total():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='ys124126',
        database='students-sys'
    )
    cursor = db.cursor()
    total_sql = 'select count(*) from students'
    cursor.execute(total_sql)
    len = cursor.fetchone()[0]  # 返回一个元组类型，取其中第一个元素
    # if os.path.exists('students.txt'):
    #     with open('students.txt', 'r', encoding='UTF-8') as f:
    #         student_old = f.readlines()
    # else:
    #     print('路径错误')
    #     return
    # len = 0
    # for item in student_old:
    #     len += 1
    print(f'当前学生总人数：{len}')


if __name__ == '__main__':
    total()
