#main.py
from EmployeeRepos import EmployeeRepos,Employee
def addEmployee():
    name = input("Введите имя работника ")
    surname = input("Введите фамилию работника ")
    position = input("Введите должность работника ")
    repos.add_employee(name=name,surname=surname,position=position)
    print("Сотрудник добавлен")

def view_all_employee():
    data = repos.get_all_employee()
    for key,value in data.items():
        print(key, '-', value.__dict__)
def get_employee_by_id():
    employe = repos.get_employee_by_id(int(input("Введите id работника ")))
    print(employe.__dict__)
def update_employee_by_id():
    flagg = True
    employee_id = int(input("Введите id работника "))
    employee= repos.get_employee_by_id(employee_id)
    print("введите имя атрибута который необходимо поменять")
    for key in employee.__dict__.keys():
        print(key)
    while flagg:
        attribute_name = input(">>")
        value = input(f"Введите новое значение(старое{employee.__dict__[attribute_name]})\n>>")
        repos.set_attr_value_by_id(employee_id,attribute_name,value)
        isNeedMoreChange = input("Хотите поменять еще один атрибут ? y/n\n>>").strip().lower()
        flagg = isNeedMoreChange == 'y'
def view_last_employee():
    print(repos.get_last_employee().__dict__)
if __name__ == '__main__':
    repos = EmployeeRepos()
    #TODO: добавить возможность просмотреть последнего добавленного работника
    commands = [
        {"name":"add","function":addEmployee,"description":"Добавить сотрудника в базу"},
        {"name": "view all", "function": view_all_employee, "description": "Просмотреть всех сотрудников"},
        {"name": "get by id", "function": get_employee_by_id, "description": "Посмотреть сотрудника по ид"},
        {"name": "update", "function": update_employee_by_id, "description": "Изменить сотрудника по id"},
        {"name": "view last", "function": view_last_employee, "description": "Посмотреть последнего добавленного сотрудника"},
    ]
    while True:
        isNeedHelp = input("Вывести список комманд y/n").strip().lower()
        if isNeedHelp == "y":
            for command in commands:
                print(command["name"],"-",command["description"])
        userChose = input(">>").strip().lower()
        for command in commands:
            if userChose == command["name"]:
                command["function"]()