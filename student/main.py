import delete, insert, modify, search, show, sort, total


def menum():  # 菜单
    print("===========================学生信息管理系统==========================")
    print('-------------------------------功能菜单----------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.对学生成绩排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出系统')
    print('-----------------------------------------------------------------------')


def main():
    while True:
        menum()
        choice = int(input('请选择功能'))
        if choice in range(0, 8):
            if choice == 0:
                answer = input('确定退出系统？y/n')
                if answer == 'y':
                    print('感谢使用')
                    break
                else:
                    continue
            elif choice == 1:
                insert.insert()
            elif choice == 2:
                search.search()
            elif choice == 3:
                delete.delete()
            elif choice == 4:
                modify.modify()
            elif choice == 5:
                sort.sort()
            elif choice == 6:
                total.total()
            elif choice == 7:
                show.show()
        else:
            print('输入错误，请重新输入')
            main()


if __name__ == '__main__':
    main()
