import os.path
import show
import pymysql

def sort():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='ys124126',
        database='students-sys'
    )
    cursor = db.cursor()
    show.show()
    select_sql='select * from students'
    cursor.execute(select_sql)
    students_nld=list(cursor.fetchall())
    # if os.path.exists('students.txt'):
    #     with open('students.txt', 'r', encoding='UTF-8') as f:
    #         students_old = f.readlines()
    #         students_nld = []
    #         for item in students_old:
    #             d = dict(eval(item))
    #             students_nld.append(d)
    # else:
    #     return
    while True:
        jud = int(input('请选择排序方式【0 升序| 1 降序】'))
        if jud == 0:
            jud_bool = False
        else:
            jud_bool = True
        mode = int(input('选择排序目标：【1：英语 | 2：python | 3：java | 4： 总成绩】'))
        if mode == 1:
            students_nld.sort(key=lambda x: int(x[2]), reverse=jud_bool)
        elif mode == 2:
            students_nld.sort(key=lambda x: int(x[3]), reverse=jud_bool)
        elif mode == 3:
            students_nld.sort(key=lambda x: int(x[4]), reverse=jud_bool)
        else:
            students_nld.sort(key=lambda x: int(x[5]), reverse=jud_bool)
        for item in students_nld:
            print(f'id:{item[0]}  name:{item[1]}  english:{item[2]}  python:{item[3]}  java:{item[4]}  grade:{item[5]}')
        answer = input('是否继续排序？y/n')
        if answer == 'n':
            break
        else:
            continue
    cursor.close()
    db.close()

if __name__ == '__main__':
    sort()
