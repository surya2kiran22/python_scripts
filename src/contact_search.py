

def contact_search():
    contact_book = {}

    while True:
        cmd = input('enter what action you want ADD,Search,Delete,View, EXIT: ')
        if cmd.upper() == 'ADD':
            name = input("enter name to add:")
            number = input("enter number:")
            if contact_book.get(name) == None:
                contact_book[name] = number
            else:
                print("name already exist")
        elif cmd.upper() == 'SEARCH':
            name = input("enter name to search:")
            if contact_book.get(name) == None:
                print("name not exist")
            else:
                print(contact_book[name])
        elif cmd.upper() == 'DELETE':
            name = input("enter name to delete:")
            if contact_book.get(name) == None:
                print("name not exist")
            else:
                del contact_book[name]
        elif cmd.upper() == 'VIEW':
            print(contact_book)
        elif cmd.upper() == 'EXIT':
            break


contact_search()




