import csv

with open('2.csv', 'w',encoding="UTF-8" ,newline='') as csvFile:
    total_person_num = 10
    tag_num = 2
    maxnum_per_tag = int(total_person_num / tag_num)
    print(maxnum_per_tag)
    fileHeader=["*姓名/Name","*员工号/Employee Number","出生日期/Birthday（YYYY-MM-DD)","入职时间/Hiredate（YYYY-MM-DD）","联系方式/Contact","*标签/Tags（用'/'隔开）","*卡号/Card Number","*照片文件路径/Photo Path（文件夹/文件名）","备注/Notes"]
    #print(type(fileHeader))
    writer = csv.writer(csvFile)
    writer.writerow(fileHeader)
    for i in range(0, total_person_num):
        name = "name_" + str(i)
        employee_num = "id_" + str(i)
        group = int(i / maxnum_per_tag)
        tag = "tag_" + str(group)
        print(tag)
        card_no = "123" + str(i)
        writer.writerow(
            [name, employee_num, "2018-08-01", 1568266729000, "13800000000", tag, card_no, "image/duxin.jpg", "test"])
