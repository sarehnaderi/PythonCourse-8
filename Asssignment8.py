products = []
def read_data():
    f = open("text.txt","r")
    for line in f:
        product = line.split(",") 
        dic = {"id":product[0],"name":product[1],"unit price":product[2],"count":product[3]}
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
    dic = {'id':id, 'name':name, 'unit price':price, 'count':count}
    products.append(dic) 
    print (products)

def delete():
    product_id = input("Enter the ID of product that you want to delete: ")
    for product in products:
        if product_id == product['id']:
            print("Are you sure you want to delete this item?", product)
            allow = input("Enter 1 to confirm or 2 to start again: ")
            if allow == '1':
                products.remove(product)
                print("You successfully deleted the item.")
                print(products)
            elif allow == '2':
                show_menu()
           
def search():
    key_word = input("Enter key word:")
    for product in products:
        if key_word == product['id'] or key_word == product['name']:
            print(product)
            break
    else: 
        print("Not found")
        
def buy():
    receipt = []
    total_price = 0
    while True:
        print(" ")
        print("** Choose your required service(1-3):")
        print("1-Add a new product to your buy list")
        print("2-Recieve your receipt")
        print("3-Show menu")
        print(" ")
        option = int(input("Enter your choice:"))
        if option == 1:
            product_id = int(input("Enter product ID::"))
            for product in products:
                    if product_id == int(product['id']):
                        wanted_count = int(input("Enter the count of the product that you need:"))
                        pro_count = int(product['count'])
                        if wanted_count <= pro_count:
                            remain = pro_count - wanted_count
                            product['count'] = wanted_count
                            print(product)
                            print("**Your item(s) added to your buy list**")
                            print("Remaining count:",remain)
                            receipt.append(product)
                            subtotal = int(product['count']) * int(product['unit price'])
                            total_price += subtotal
                        else:
                            print("__Sorry! There is not enough of this item available__")
                            print("__Available count of your required item is:",product['count'])
                        break
            else:
                print("The ID is not defined.")

        elif option == 2:
            print("**Here is your receipt**")
            print("id \t name \t unit price \t count")
            for product in receipt:
                print(product['id'],'\t',product['name'],'\t',product['unit price'],'\t',product['count'])
            print(">>>Total price:",total_price)
            break

        elif option == 3:
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
            elif user_choice == 7:
                show_products()
            else:
                print("Error! Enter a valid number(1-7).")
            break
        
def edit():
    product_id = input("Enter the ID of product that you want to edit:")
    for product in products:
        if product_id == product['id']:
            print(product)
            print("Which item do you want to edit?")
            print("1-Name")
            print("2-Price")
            print("3-Count")
            choice = input("Enter the number:")
            if choice == '1':
                edit_name = input("Enter new name:")
                product['name'] = edit_name
                print("Your list is updated")
                print("Done! Your updated product info:",product)
            elif choice == '2':
                edit_price = input("Enter updated price:")
                product['unit price'] = edit_price
                print("Done! Your updated product info:",product)
            elif choice == '3':
                edit_count = input("Enter updated count:")
                product['count'] = edit_count
                print("Done! Your updated product info:",product)
            else:
                print("Error! Enter a valid number(1-3).")
                print(products)
                
def exit():
    pass

def show_products():
    print("id \t name \t unit price \t count")
    for product in products:
        print(product['id'],'\t',product['name'],'\t',product['unit price'],'\t',product['count'])
       
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
elif user_choice == 7:
    show_products()
else:
    print("Error! Enter a valid number(1-7).")
