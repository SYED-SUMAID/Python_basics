class student:
    def __init__(self,name,marks):
        self.name = name
        self._marks = marks

    @property
    def marks(self):
        return self._marks
  
    @marks.setter
    def marks(self,value):
        if 0>= value >= 100 :
           self._marks = value

        else:
         raise ValueError("marks must be between 0 - 100")
 

    def show (self):
       print(f"student: {self.name} and marks:{self.marks}")


s = student("sum",98) 
s.show()