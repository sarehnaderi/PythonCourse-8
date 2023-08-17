
products = []

def read_data():
    f = open("text.txt","r")
    for line in f:
        product = line.split(",") 
        dic = {"id":product[0],"name":product[1],"price":product[2],"count":product[3]}
        products.append(dic)
    # print(products)
def show_menu():
    print("*Menu*")
    print("1-add")
    print("2-delete")
    print("3-search")
    print("4-buy")
    print("5-edit")
    print("6-exit")
    print("7-show products")
    
def add():
    id = input("Enter id:")
    name = input("Enter name:")
    price = input("Enter price:")
    count = input("Enter count:")
    dic = {'id':id, 'name':name, 'price':price, 'count':count}
    products.append(dic) 
    print (products)
def delete():
    product_id = int(input("Enter the ID of product that you want to delete: "))
    for product in products:
        if product_id == product['id']:
            print("Are you sure you want to delete this item?", product)
            allow = int(input("Enter 1 to confirm or 2 to start again: "))
            if allow == 1:
                products.remove(product)
                print("You successfully deleted the item.")
                break
            elif allow == 2:
                return
           
def search():
    key_word = input("Enter key word:")
    for product in products:
        if key_word == product['id'] or key_word == product['name']:
            print(product)
            break
    else: 
        print("Not found")
def buy():
    pass
def edit():
    product_id = int(input("Enter the ID of product that you want to edit:"))
    for product in products:
        if product_id == product['id']:
            print("Which item do you want to edit?")
            print("1-Name")
            print("2-Price")
            print("3-Count")
            choice = int(input("Enter the number:"))
            if choice == 1:
                edit_name = input("Enter new name:")
                product['name'] = edit_name
                print("Your list is updated")
            elif choice == 2:
                edit_price = int(input("Enter updated price:"))
                product['price'] = edit_price
            elif choice == 3:
                edit_count = int(input("Enter updated count:"))
                product['count'] = edit_count
            else:
                print("Error! Enter a valid number.")
            print(products)
                
            
def exit():
    pass

def show_products():
    print("id \t name \t price \t count")
    for product in products:
        print(product['id'],'\t',product['name'],'\t',product['price'],'\t',product['count'])
read_data()
show_menu()

user_choice = int(input("Enter your choise:"))

if user_choice == 1:
    add()
elif user_choice == 2:
    delete()
elif user_choice == 3:
    search()
elif user_choice == 4:
    buy()
elif user_choice == 5:
    edit()
elif user_choice == 6:
    exit()
else:
    show_products()
