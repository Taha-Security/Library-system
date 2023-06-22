import sre_parse
from unicodedata import name
from colorama import Fore , Back , Style
import os , platform , sys , time , keyboard

def clear():
    if "Windows" in platform.uname():
        os.system("cls")
    else:
        os.system("clear")
clear()

def add_new_book():
    clear()
    book_name = input(Fore.LIGHTGREEN_EX + "\nEnter The Name Of The Book : ").lower()
    while True:
        book_location = input(Fore.LIGHTGREEN_EX + "\nEnter In Which Library is : ").upper()
        libraris  = ["A1","A2","A3","A4","B1","B2","B3","B4"]
        if book_location in libraris:
            break
        else:
            print(Fore.LIGHTRED_EX + "\n [!] Library Not Found")
            time.sleep(2)

    book_price = input(Fore.LIGHTGREEN_EX + "\nEnter The Price : ")
    book_type = input(Fore.LIGHTGREEN_EX + "\nEnter The Kind Of The Book : ")
    print("\n")
    book_info = f"name:{book_name},price:{book_price},location:{book_location},type:{book_type}"
    write_data = open("database/books.txt", "a+").write(f"\n{book_info}")
    print(Fore.LIGHTYELLOW_EX + " + Book Added")
    time.sleep(3)

def find_a_book():
    clear()
    book_name = input(Fore.LIGHTGREEN_EX + "\nEnter The Name Of The Book : ").lower()
    database = open("database/books.txt","r").read()

    book_names = []

    for info in database.split(sep="\n"):
        for b_info in info.split(sep=","):
            book_names.append(b_info.split(sep=":")[1])    

    if book_name in book_names:
        book_info = ""
        for book in database.split("\n"):
            for i in book.split(sep=","):
                if book_name == i.split(sep=":")[1]:
                    book_info += book
                else:
                    None
                    
        def str_to_dict(book:str):
                result = {}
                for i in book.split(sep=","):
                    result.update({i.split(sep=":")[0]:i.split(sep=":")[1]})
                return result
        book_information = str_to_dict(book_info) 
            
        name = book_information["name"]
        price = book_information["price"]
        location = book_information["location"]
        type = book_information["type"]

        data = (Fore.LIGHTYELLOW_EX + f"""
    + Book Found

    Name\t:   {name}
    Price\t:   {price}$
    Location\t:   {location}
    Genre\t:   {type}
            """)

        for line in data.split(sep="\n"):
            print(line)
            time.sleep(0.155)
        
        input(Fore.LIGHTBLUE_EX + "    Enter For The Menu")
    else:
        clear()
        print(Fore.LIGHTRED_EX + "[!] Book Not Found !")
        options_menu = (Fore.LIGHTWHITE_EX + f"""
    1. Try Again
    2. Back To Menu
        """)
        for line in options_menu.split(sep="\n"):
            print(line)
            time.sleep(0.155)
        select = input("    Select One Option : ")
        if select == "1":
            find_a_book()
        else:
            None


def remove_book():
    clear()
    book_name = input(Fore.LIGHTGREEN_EX + "\nEnter The Name Of The Book : ").lower()
    database = open("database/books.txt","r").read()
    clear()
    if book_name in database:
        warning = input((Fore.LIGHTRED_EX + f"\n[!] Are You Sure To Delete {book_name} [ Yes , No ] ").lower())
        if warning == "yes":
            for book in database.split(sep="\n"):
                if book_name in book:
                    database_update = database.replace(book , "")
                    update = open("database/books.txt","w").write(database_update)
                    print(Fore.LIGHTGREEN_EX + "\n[+] Book Is Deleted :)")
                    time.sleep(3)
        else:
            print(Fore.LIGHTGREEN_EX + "\n[!] Ok")
            time.sleep(2)
    else:
        print(Fore.LIGHTRED_EX + f"\n[!] There is no book called {book_name} in library")
        time.sleep(5)


def edit_book():
    clear()
    book_name = input(Fore.LIGHTGREEN_EX + "\nEnter The Name Of The Book : ").lower()
    database = open("database/books.txt","r").read()
    if book_name in database:
        clear()
        print(Fore.LIGHTYELLOW_EX + f"\nEdit The Information Of The {book_name} Now , Only Enter If dont want to change anything\n")
        data = ""
        for book in database.split(sep="\n"):
            if book_name in book:
                data += book
            else:
                pass
        def str_to_dict(book:str):
            result = {}
            for i in book.split(sep=","):
                result.update({i.split(sep=":")[0]:i.split(sep=":")[1]})
            return result
        book_info = str_to_dict(data)
        name = input(Fore.LIGHTYELLOW_EX + "\nEnter The New Name : ")
        if name == "":
            name = book_info["name"]
        price = input(Fore.LIGHTYELLOW_EX + "\nEnter The New Price : ")
        if price == "":
            price = book_info["price"]
        location = input(Fore.LIGHTYELLOW_EX + "\nEnter The New Location : ")
        if location == "":
            location = book_info["location"]
        type = input(Fore.LIGHTYELLOW_EX + "\nEnter The New Type : ")
        if type == "":
            type = book_info["type"]
        result = f"name:{name},price:{price},location:{location},type:{type}"
        make_ready = database.replace(data , result)
        update = open("database/books.txt","w").write(make_ready)
        clear()
        print(Fore.LIGHTGREEN_EX + "\n [+] Information Edited")
        time.sleep(3)
    else:
        clear()
        print(Fore.LIGHTRED_EX + "[!] Book Not Found !")
        options_menu = (Fore.LIGHTWHITE_EX + f"""
    1. Try Again
    2. Back To Menu
        """)
        for line in options_menu.split(sep="\n"):
            print(line)
            time.sleep(0.155)
        select = input("    Select One Option : ")
        if select == "1":
            edit_book()
        else:
            None


def search():
    clear()
    print(Fore.LIGHTCYAN_EX + """
Choose a Genre : [ Drama , Story , Adventure , Motivational , Novel , Business , Mystrey , Educational ] 
    """)
    book_genre = input(Fore.LIGHTGREEN_EX + "\nEnter The Genre Of The Book : ").lower()
    database = open("database/books.txt","r").read()
    genres = ["drama","story","adventure","motivational","novel","business","mystrey" , "educational"]
    if book_genre in genres and book_genre in database:
        clear()
        print(Fore.LIGHTGREEN_EX + f"\nResult of {book_genre} books :")
        data = []
        for book in database.split(sep="\n"):
            if book_genre in book:
                data.append(book)
            else:
                pass
        def data_to_str(data:str):
            def str_to_dict(book:str):
                result = {}
                for i in book.split(sep=","):
                    result.update({i.split(sep=":")[0]:i.split(sep=":")[1]})
                return result
            book_information = str_to_dict(data)
            name = book_information["name"]
            price = book_information["price"]
            location = book_information["location"]
            type = book_information["type"]

            data = (Fore.LIGHTCYAN_EX + f"""
Name\t :   {name}
Price\t :   {price}$
Location :   {location}
type\t :   {type}
________________________ """)     
            return data
        for info in data:
            print(data_to_str(info))
            time.sleep(0.7)
        input(Fore.LIGHTBLUE_EX + "\nEnter For The Menu")

    else:
        clear()
        print(Fore.LIGHTRED_EX + f"\n[!] No Book Found With {book_genre} genre !")
        options_menu = (Fore.LIGHTWHITE_EX + f"""
    1. Try Again
    2. Back To Menu
        """)
        for line in options_menu.split(sep="\n"):
            print(line)
            time.sleep(0.155)
        select = input("    Select One Option : ")
        if select == "1":
            search()
        else:
            None       

def exit_():
    clear()
    warning = input(Fore.LIGHTRED_EX + "\n [?] Do You Want To Exit ? [ yes , no ] ").upper()
    if warning == "YES" or warning == "Y":
        clear()
        print(Fore.LIGHTCYAN_EX + """

[+] Have a nice Day...

        """ + Style.RESET_ALL)
        sys.exit()
    else:
        pass

def menu():
    clear()
    time.sleep(0.1)
    print(Fore.LIGHTYELLOW_EX + "\n  Please Choose One Options ")
    menu_ = (Fore.LIGHTWHITE_EX + """
  1. Find a book
  2. Add New Book
  3. Remove a Book
  4. Edit a Book
  5. Search
  0. Exit
    """)
    for line in menu_.split(sep="\n"):
        print(line)
        time.sleep(0.1)

while True:
    menu()
    select = input(Fore.LIGHTCYAN_EX + "  Enter The Number : ")
    if select == "1":
        find_a_book()
    elif select == "2":
        add_new_book()
    elif select == "3":
        remove_book()
    elif select == "4":
        edit_book()
    elif select == "5":
        search()
    elif select == "0":
        exit_()