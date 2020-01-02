import pymysql
import os
import prettytable
import colorama

def menu():
    print("(0) 離開程式")
    print("(1) 顯示會員列表")
    print("(2) 新增會員資料")
    print("(3) 更新會員資料")
    print("(4) 刪除會員資料")
    print("(5) 新增會員的電話")
    print("(6) 刪除會員的電話")

def display_data():
    cur.execute("SELECT * FROM `member` LEFT JOIN `tel` ON `member`.`id`=`tel`.`member_id`")
    ret = cur.fetchall()
    # print(ret)
    t = prettytable.PrettyTable(["Id", "Name", "Birthday", "Address", "Tel"], encoding="utf8")
    t.align["Id", "Name", "Birthday", "Address", "Tel"] = "l"
    for d in ret:
        t.add_row([d[0], d[1], d[2], d[3], d[6]])
    print(t)

link=pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    db="python_ai_2018",
    charset="utf8",
    port=3306
 )
cur=link.cursor()
while True:
    menu()
    select = int(input("指令: "))

    # 指令 == 0,離開程式
    if select == 0:
        print("離開此程式!!")
        break

    # 指令 == 1 , 顯示會員列表
    elif select == 1:
        display_data()

    elif select == 2:
    # 指令 == 2 , 新增會員資料
        name = input("請輸入會員姓名:")
        birthday = input("請輸入會員生日:")
        address = input("請輸入會員地址:")

        cur.execute(
            "INSERT INTO `member` (`name`,`birthday`,`address`)" +
            "VALUES(%s,%s,%s)",
            (name,birthday,address)
        )
        link.commit()
        print("資料新增成功, 資料的ID", cur.lastrowid)
        os.system("pause")

    # 指令 == 3 , 更新會員資料
    elif select == 3:
        display_data()

        ida = input("請選擇你要修改的資料編號:")
        name = input("請輸入會員姓名:")
        birthday = input("請輸入會員生日:")
        address = input("請輸入會員地址:")

        cur.execute(
            "UPDATE `member` SET `name`=%s,`birthday`=%s,`address`=%s" +
            "WHERE `id`=%s" ,
            (name,birthday,address,ida)
        )
        link.commit()

    # 指令 == 4 , 刪除會員資料
    elif select == 4:
        display_data()

        ida = input("請輸入你要刪除的資料ID:")

        cur.execute(
            "DELETE FROM `member` WHERE `id`=%s ", (ida)
        )
        link.commit()

    # 指令 == 5 , 新增會員的電話
    elif select == 5:
        display_data()
        # cur.execute("SELECT * FROM `member` LEFT JOIN `tel` ON `member`.`id`=`tel`.`member_id`")
        # ret = cur.fetchall()
        # # print(ret)
        # t = prettytable.PrettyTable(["Id", "Name", "Birthday", "Address", "Tel"], encoding="utf8")
        # t.align["Id", "Name", "Birthday", "Address", "Tel"] = "l"
        # for d in ret:
        #     t.add_row([d[0], d[1], d[2], d[3], d[6]])
        # print(t)

        member_id = input("請選擇要添加電話的會員編號:")
        tel = input("請輸入電話:")

        cur.execute(
            "INSERT INTO `tel` (`member_id`,`tel`) VALUES(%s,%s)", (member_id,tel)
        )
        link.commit()

        print("電話新增成功!!")
        os.system("pause")

    # 指令 == 6 , 刪除會員的電話
    elif select == 6:
        display_data()
        member_id = input("請選擇要刪除電話的會員編號:")

        cur.execute(
            "DELETE FROM `tel` WHERE `member_id`=%s", (member_id)
        )
        link.commit()

        print("刪除電話成功!!")

    else:
        print("超出指令範圍!!")
        break

link.close()