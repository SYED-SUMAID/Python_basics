class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        last =  self.name.split(" ")[0]
        return last
 
    @first_name.setter
    def first_name(self,parts):
       split_name= self.name.split(" ")
       new_name = f"{parts} {split_name[1]}"
       self.name = new_name

e = Employee("Jhon Doe",30000000)
print(e.first_name)
e.first_name = "Sum"
print(e.name)


                
      