import os.path
def modify():
    while True:
        student_id = input('输入要修改的学生id')
        if student_id != '':
            if os.path.exists('students.txt'):  # 判断文件路径是否正确
                with open('students.txt', 'r', encoding='UTF-8') as file:
                    student_old = file.readlines()  # 逐行读取文件内容
                    # print(student_old)

            else:
                print('文件内容为空')
                return
        flag=False
        with open('students.txt', 'w', encoding='UTF-8') as f:
            for item in student_old:
                d = dict(eval(item))
                if d['id'] == student_id:
                    print('找到信息，开始修改')
                    while True:
                        try:
                            d['name'] = input('输入姓名')
                            d['english'] = input('输入英语成绩')
                            d['python'] = int(input('输入python成绩'))
                            d['java'] = int(input('输入java成绩'))
                            flag=True
                            break
                        except:
                            print('输入错误')
                            continue

                f.write(str(d)+'\n')
        if flag==False:
            print('未找到该信息')

        answer = input('是否继续修改？y/n')
        if answer == 'y':
            continue
        else:
            break


if __name__ == '__main__':
    modify()
