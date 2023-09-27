import os.path
def total():
    while True:
        if os.path.exists('students.txt'):
            with open('students.txt', 'r', encoding='UTF-8') as f:
                student_old = f.readlines()
        else:
            print('路径错误')
            return
        len=0
        for item in student_old:
            len+=1
        print(f'当前学生总人数：{len}')
        break
if __name__ == '__main__':
    total()