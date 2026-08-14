def person_info(first_name,last_name,age=None):
    person = {
        'first_name':first_name,
        'last_name':last_name,
    }
    if age:
        person['age'] = age
    person_age = {'age':age}
    return person, person_age  #返回tuple,组成(a,b)
person = person_info("John", "Doe", 20)
person1 = person_info("John", "Doe")
print(person)
print(type(person))
#tuple:元组
print(person1)