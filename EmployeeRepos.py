#EmployeeRepos.py
from Employee import Employee
class EmployeeRepos:
    def __init__(self):
        self._repos = {}
        self.lastId = 0


    def add_employee(self,**kwargs):
        if "employee" in kwargs.keys():
            #Добавляем сущность
            self._repos.update({self.lastId:kwargs["employee"]})
            self.lastId += 1
        elif "name" in kwargs.keys() and "surname" in kwargs.keys() and "position" in kwargs.keys():
            tempEmployee = Employee(kwargs['name'],kwargs['surname'],kwargs['position'])
            self.add_employee(employee=tempEmployee)
    def get_all_employee(self):
        return self._repos
    def _is_attr_exsist(self,id:int,attribute_name:str):
        if id >= self.lastId:
            return False
        tmp = self._repos[id].__dict__
        if attribute_name not in tmp.keys():
            return False
        return True
    def get_attr_value_by_id(self,id:int,attribute_name:str):
        if self._is_attr_exsist(id,attribute_name):
            return self._repos[id].__dict__[attribute_name]

    def set_attr_value_by_id(self,id:int,attribute_name:str,value):
        if self._is_attr_exsist(id,attribute_name):
            self._repos[id].__dict__[attribute_name] = value
    def get_employee_by_id(self,id:int):
        if id >= self.lastId:
            return
        return self._repos[id]

    def get_last_employee(self):
        return self._repos[self.lastId-1] if self.lastId != 0 else None
    def get_first_employee(self):
        return self._repos[0] if self.lastId != 0 else None
    def update_employee(self,id:int,employee:Employee):
        if id >= self.lastId:
            return
        self._repos.update({id:employee})

