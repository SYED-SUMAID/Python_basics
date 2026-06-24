book_list = []
def add_book():
    title = input("Enter the book name: ")
    author = input("Enter the name of the author: ")
    year = int(input("Enter the year(the book is published: )"))
    rating = float(input("Enter the rating"))
    book = (title,author,year,rating)

    book_list.append(book)
    print("book added")
def book_after_year():
    if not book_list:
        print("no book found")

    year_limit = int(input("Enter the year : "))

    print(f"---------Books after {year_limit} ")
    found = False

    for book in book_list:
        if book[2] > year_limit:
            print("book found")
            print(f"title{book[0]}:author{book[1]}:year{book[2]}:rating{book[3]}")

        if not found:
            print("no books found")

        print()

def find_by_author_name():
    if not book_list:
        print("no books found by this author")
        return 

    name = input("Enter the name of the author:")

    print(f"\nbooks by {name}:")
        
    for book in book_list:
        if name in book[1]:
            if len (book_list) == 1:
                print("book found")
            if len == 2:
                print("books found")
            print(f"title:{book[0]:<5}|author:{book[1]:<5}|year:{book[2]:<5}|rating{book[3]:<5}")
            

    print()    
def book_rating():
    if not book_list:
        print("no book found")
        return
    found = False

    best = max(book_list,key = lambda a:a[3]) 
    print("book found")
    
    print(f"title:{best[0]}|Author:{best[1]}|year:{best[2]}|rating:{best[3]}")
    if not found:
        print("No books availible")

    print()         

    

def main():
    while True:
        print("1 : Add book")
        print("2 : Author name")
        print("3 : book rating")
        print("4 : Exit")
        choice = input("Enter the choice :")
        if choice == '1':
            add_book()
        if choice == '2':
            find_by_author_name()
        if choice == '3':
            book_rating()
        if choice == '4':
            print("Exit")    
        if not choice:
            print("Enter a valid choicee") 

        
main()









           