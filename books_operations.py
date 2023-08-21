
# برای ارطبات بین فایل های این پروژه کار زیر را انجام میدهم

books = []    #این بوکسی که اینجا تعریف کردیم نباید در حلقه وایل باشد ضمنن این بوکس لیتسی از دیکت کتاب ها را در خود دارد که کاربر 
                #آن را اضافه کرده است پس خیلی مهم است
def add_book():
    global books    #optional code کد اختیاری جهت یادآوری
    book = {}
    book["title"] = input("Enter title of the book : ")
    book["author"] = input ("Enter author of the book : ")
    book["pages"] = int(input ("Enter number of pages : "))
    book["price"] = float(input ("Enter price of the book : "))
    book["isbn"] = input("Enter ISBN of the book : ")
    books.append(book)

def list_books():
    for book in books :
        print(f"Title of book : {book['title']}")
        print(f"Author of book : {book['author']}")    #از متد اف استرینگ استفاده شده است
        print(f"Number of pages : {book['pages']}")
        print(f"Price of book : {book['price']}")
        print(f"ISBN of book : {book['isbn']}")
        print("----------------------------------")


def find_book():
    isbn = input("Enter ISBN to find book : ")
    for book in books : 
        if book["isbn"] == isbn : 
            print(f"Title of book : {book['title']}")
            print(f"Author of book : {book['author']}")
            print(f"Number of pages : {book['pages']}")
            print(f"Price of book : {book['price']}")
            print(f"ISBN of book : {book['isbn']}")
            print("----------------------------------")
            break  #یعنی به محض اینکه کتاب را پیدا کرد همانجا حلقه متوقف شود و بیخود کل تابع را نگردد
    else : 
        print("This book Is Not in books database ! ")

def find_by_title():  #optional
    pass 

def delete_book():
    isbn = input("Enter ISBN to delete book : ")
    for book in books :
        if book["isbn"] == isbn :
            books.remove(book)
            print("The book has been delete successfully")
            break
    else : 
        print("This book Is Not in books database ! ")
