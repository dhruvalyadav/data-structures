class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        return f"name {self.name},Age {self.age}"     
class Employee(Person):
    def __init__(self,name,age,id,salary):
        super().__init__(name,age)
        self.id=id
        self.salary=salary
    def info(self):
        return (
            f"{self.show()}\n" f"id is {self.id} salary is {self.salary}"
        )   
class Manager(Employee):
    def __init__(self,name,id,salary,dept,age):
        super().__init__(name,age,salary,id)
        self.dept=dept
    def showdept(self):
        return f"{self.info()}\n" f"department: {self.dept}"

manager=Manager('abc',10,25000,'it',30)
print(manager.showdept())