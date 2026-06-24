list = []
def add_book():
    title = input("enter the book name: ").strip()
    year = int(input("year published: "))
    author = input("enter the author name")

    book = (title,year,author)
    list.append(book)
    print("book added")



def show_books():
    book_name = input("enter the book name:")

    for b in list:
        if book_name in b[0]:
            print("book found",b)
            break
        else:
            print("no book found")

def book_after_year():
    if not list:
        print("no book found")
        return
    year_limit = int(input("Enter the year limit :"))

    print(f"Books after year limit {year_limit}  ")
    found = False
    for  book in list:  
        if book[1] > year_limit:
            print("book found")
            print(f"title {book[0]} , year : {book[1]} , author : {book[2]}")
            found = True

    if not found:
        print("no books found")        

def book_author():

    if not list:
        print("no book found with this author name")
        return
    author_name =input("Enter the author name:")

    for book in list:
        if author_name in book[2]:
            print(f"book found withe this author name{book}")
            return





while True:

    choice = input("enter the number:")
    if choice == '1':
        add_book()
    if choice == '2':
        show_books()
    if choice == '3':
        book_after_year()
    if choice == '5':
        print("exit")      
    if choice == '4':
        print("TRY AGAIN")    
    if choice =='8':
        book_author()
    if choice == '9':
        print("exit")
        break
        






#def show_book():
    #for book in list:
        #if book in list:
            #print("book found")
        #else:
            #print("no books found")

#def add_book():
