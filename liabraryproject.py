library = []
def add_book():
    Tittle = input("Enter the tittle :").strip()
    Author = input("Enter the Name of The Author :").strip()
    year = int(input("Enter the year :"))
    Rating = float(input("Enter the rating :"))

    book = (Tittle,Author,year,Rating)
    library.append(book)
    print("Book Added!")

def book_after_year():
    if not library:
        print("No books found\n")
        return

    year_limit = int(input("Show the books publishes after the year :"))

    print(f"\n----BOOKS AFTER {year_limit}----")
    found = False
    for book in library:
        if book[2] > year_limit:
           print(f"Tittle : {book[0]} , Author : {book[1]} , year:{book[2]} , Rating:{book[3]}")
           found = True   
     
    if not found:
        print("NO Books found")

    print()

def book_author():
    if not library:
        print("\nNo Book found by this author")
        return
    
    name = input("Enter The Name of the Author :").lower()

    print(f"\n-----BOOKS WITH {name}-----")
    found =False
    for book in library:
        if name in book[1].lower():
            print("BOOK FOUND")
            print(f"\033[95mTittle : {book[0]} | Author : {book[1]} | year:{book[2]} | Rating : {book[3]}\033[0m")
            found = True

        if not found:
               print("NO book found With this Author")

    print()

def book_rating():
    if not library:
        print("No BOOK Found\n")
        return
    
    best = max(library,key = lambda b:b[3])
    print("\n-----HIGHEST RATED BOOK------")
    print(f"Tittle: \033[91m{best[0]} | Author: ({best[1]}) | year: {best[2]} | Rating: {best[3]}\033[0m")

    print()  


def main():
    while True:
        print("1  ADD BOOK")
        print("2  SHOW BOOK AFTER YEAR")
        print("3  SEARCH BY AUTHOR")
        print("4  HIGHEST_RATED BOOK")
        print("5  EXIT")    
 
        choice = (input("Enter the choice :"))

        if choice == '1':
          add_book()

        elif choice == '2':
          book_after_year()
 
        elif choice == '3':
          book_author()

        elif choice == '4':
          book_rating()

        elif choice == '5':
          print("This is my Library")
          break
    

        else:
              print("Not a valid choice") 

                         
main()




