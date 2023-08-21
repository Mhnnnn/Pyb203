# V 2.1.0

import books_operations as bo
#با این کار برنامه را ماژول کردیم و تابع هایی که درست کردیم را با این کد بالا در اینجا استفاده میکنیم

#-------------------main---------------------------------

while True :
    print("===================================")
    print("Press A to add a book")
    print("Press L to list all books")
    print("Press F to find a book")
    print("Press D to delete a book")
    print("Press Q to quit application")
    print("===================================")
    choice = input ("Enter Your Choice : ").upper()   # میخواهیم کاربر چه حروف کوچک چه بزرگ زد خطا ندهد
    #choice = choice.upper() این کارم میشد کرد
    print("===================================")
    if  choice == 'A':
        bo.add_book()
    elif choice == 'L':
        bo.list_books()
    elif choice == 'F':
        bo.find_book()
    elif choice == 'D':
        bo.delete_book()
    elif choice == 'Q':
        break
    else : 
        print ("Wrong choice")  # الس وایل هست نه برای ایف
        

# آپ ما فعلا سیستم ذخیره سازس ندارد که بعدا باید ایجاد کنیم

