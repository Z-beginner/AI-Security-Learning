gpa_dict = {
    "student1" : 3.245 ,
    "student2" : 3.869 ,
    "student3" : 3.379
}
for name , gpa in gpa_dict.items():
    print(name ,'你好，你的当前gpa为',gpa) #断断续续
    print('{0}你好，你的当前gpa为：{1:.2f}'.format(name ,gpa))