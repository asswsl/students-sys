import pymysql


def show():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='ys124126',
        database='students-sys'
    )
    cursor = db.cursor()
    select_sql = 'select * from students'
    cursor.execute(select_sql)
    student_old = cursor.fetchall()
    # if os.path.exists('students.txt'):
    #     with open('students.txt', 'r', encoding='UTF-8') as f:
    #         student_old = f.readlines()
    # else:
    #     print('路径错误')
    #     return
    for item in student_old:
        # d = dict(eval(item))
        id = item[0]
        name = item[1]
        english = item[2]
        python = item[3]
        java = item[4]
        grade = item[5]
        print(f'id:{id}  name:{name}  english:{english}  python:{python}  java:{java}  grade:{grade}')
        # print(
        #     'id:' + str(['id']) + '  name:' + str(d['name']) + '  english:' + str(
        #         d['english']) + '  python:' +
        #     str(d['python']) + '  java:' + str(d['java'])+' grade:'+str(d['grade']))


if __name__ == '__main__':
    show()
