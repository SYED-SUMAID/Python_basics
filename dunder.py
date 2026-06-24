class Vector:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def __add__(self,other):
    return Vector(self.x + other.x , self.y + other.y)
  def __sub__(self,other):
    return Vector(self.x - other.x,self.y - other.y)
  def __str__(self):
    return f"Vector {self.x} , {self.y}"
  def __mul__(self,other):
    return Vector(self.x * other.x,self.y * other.y)
  def __truediv__(self,other):
    new_x = self.x/other.x
    new_y = self.y/other.y
    return Vector(new_x ,new_y)
    
  

v1 = Vector(6, 4)
v2 = Vector(8, 9)  
v3 = v1 + v2
print(v3)
v4 = Vector(56,78)
v5 = Vector(5,71)
v6 = v4 - v5
print(v6)
v7 = Vector(5,8)
v8 = Vector(5,71)
v9 = v7 * v8
print(v9)
v10 = Vector(80,60)
v11 = Vector(5,3)
v12 = v10 / v11
print(v12)
