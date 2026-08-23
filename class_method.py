students = []
def add_students():
    sid = int(input("Enter the student ID :"))
    name = str(input("Enter the Name :"))
    marks = float(input("Enter the marks :"))

    student = (sid,name,marks)
    students.append(student)
    print(f"Student {name} ADDED!")

def view_all_students():
    if not students:
        print("No Student record found\n")
        return
    
    print("\033[96m-----ALL STUDENTS-----\033[0m")
    for s in students:
        print(f"ID : {s[0]} , NAME {s[1]} , MARKS {s[2]}")     
    #print()

def search_student():
    sid = int(input("Enter the Student ID :"))
    for s in students:
     if s[0] == sid:
         print("\033[94mStudent Found\033[0m")
         print(f"ID :{s[0]} , NAME : {s[1]} , MARKS {s[2]}\n")

         return    
     print("\033[91mNo STUDENT FOUND WITH THIS STUDENT ID \033[0m")


def top_student():
    if not students:
      print("No Students found to Evaluate")

      return

    top = max(students, key = lambda s :s[2]) 
    print("\033[93m-----TOP STUDENT------\033[0m")
    print(f"ID {top[0]} , NAME :{top[1]} ,MARKS {top[2]}\n")

def main():

   while True:
      print("1  Add Student")
      print("2 view Students")
      print("3  Search Students")
      print("4  Top Student")
      print("5  EXIT")

      choice = input("Enter Your Choice :")

      if choice == '1':
         add_students()

      elif choice == '2':
         view_all_students()

      elif choice =='3':
         search_student()

      elif choice == '4':
         top_student()

      elif choice  == '5':
         print("STUDENT PROFILE MANAGER")

         break
      else:
         print("INVALID CHOICE")       

main()

       
    
