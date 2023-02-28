# this is an inventory code
# started by creating a class shoe and then initialized is using a constructor
class Shoes:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    # def get cost that returns the cost
    def get_cost(self):
        return self.cost
    # def get quantity that returns quantity
    def get_quantity(self):
        return self.quantity
    # represintation in a str format
    def __repr__(self):
        return (f"{self.country} {self.code} {self.product} {self.cost} "
                f"{self.quantity}")

# def read shoes data that adds shoes to a list
def read_shoes_data():
    
    shoes_list = []
    with open("inventory.txt", "r", encoding="UTF-8") as f:
        
        try: 
            inventory = open("inventory.txt", "r")
        except FileNotFoundError:
            print("The file cannot be found.")
        else:
            pass
        
        # added all stock into a list
        for i in f:
            line = i.strip()  
            log_shoe = line.split(",")  
            
            try:
                # made shoe an object and used the try - except method for an index erros 
                log_shoe = Shoes(log_shoe[0], log_shoe[1], log_shoe[2],
                            log_shoe[3], log_shoe[4])
            
            
            except IndexError:
                print(f"There was an error found in the file "
                    f" the inventory.txt file. Line {i} has an error")
            
            
            else:
                shoes_list.append(log_shoe)
            
    return shoes_list

# def view all that shows all the inventory when called using a for loop and list
def view_all():
    
    shoes_list = read_shoes_data()

    for i in range(0,len(shoes_list)-1):
        display_data = ("{:<15} {:<11} {:<22} {:<10} {:<15}"\
                        .format(shoes_list[i].country,
                                shoes_list[i].code,
                                shoes_list[i].product,
                                ("$" + str(shoes_list[i].cost)),
                                shoes_list[i].quantity))
        print(display_data)  

# def restock that gets the lowest shoe quantity and asks if you would like to update it using a for loop, indexing and list
def re_stock():                         
   
    shoes_list = read_shoes_data()

    low_stock = []  
    for item in range(1,len(shoes_list)):
        quantity_number = (shoes_list[item].quantity)
        low_stock.append(int(quantity_number))

    # Finds the index that has the lowest amount of shoes
    index = [index for index, low in enumerate(low_stock) 
                if low == min(low_stock)]

              
    index = int(index[0]) + 1  

    # shows the country with lowest amount of shoes
    print("The country with the lowest stock of inventory:")
    
    display = ("{:<15} {:<15} {:<22} {:<15} {:<15}"\
                .format("Country",
                    "Code",
                    "Product",
                    "Cost",
                    "Quantity"))
    print(display)  

    # finds the lowest quatity and displays it 
    display_data = ("{:<15} {:<15} {:<22} {:<15} {:<15}"\
                    .format(shoes_list[index].country,
                            shoes_list[index].code,
                            shoes_list[index].product,
                            ("$"+shoes_list[index].cost),
                            shoes_list[index].quantity))
    print(display_data)  
    print()

    # using a while loop it asks user if they would like to update the stock
    while True:
        add_choice = input("Would you like to update the stock quantity ?"
                    "\n yes - yes, add stock."
                    "\n no - no, go back to menu\n").lower()  
        
        
        if add_choice == "yes":
            
            add = int(input("Enter the quanity of the shoes "
                        "to update the stock.\n"))
            
            # Adds the new quantity to the shoe
            stock_update = int(shoes_list[index].quantity) + add

            # Reads all lines and updates the data
            new_inventory = []
            replace_inventory = []
            with open('inventory.txt', 'r+', encoding='utf-8') as file:
                
                data = file.read().splitlines()

                # used a for loop to add the replaced inventory to the shoes
                for items in data:
                    line = items.strip() 
                    log_shoe = line.split(",")           
                    replace_inventory.append(log_shoe)
                
                
                replace_inventory[index][4] = str(stock_update)
                
                # wrote the new inventory to the shoes which updates in inventory.txt
                for the_items in replace_inventory:
                    inventory_replace = ",".join(the_items)
                    new_inventory.append(inventory_replace)

             
            with open('inventory.txt', 'w', encoding='utf-8') as file:
                file.write("\n".join(new_inventory))
            
            
            print("\nYour stock has being updated in inventory.txt")
            break

        # Returns to menu
        elif add_choice == "no":
            break

        # 
        else:
            print("Incorrect choice")
            continue

# def search shoe that finds a product by entering the product code using indexing 
def search_shoe():
   
    shoes_list = read_shoes_data()

    
    search_code = input("Enter the product code: ")

    
    index = [index for index, item in enumerate(shoes_list) 
                if item.code == search_code]
    
    
    
    display = ("{:<15} {:<15} {:<22} {:<15} {:<15}"\
                .format("Country",
                    "Code",
                    "Product",
                    "Cost",
                    "Quantity"))
    print(display)  

    # finds the product and displays it
    display_data = ("{:<15} {:<15} {:<22} {:<15} {:<15}"\
                    .format(shoes_list[index[0]].country,
                            shoes_list[index[0]].code,
                            shoes_list[index[0]].product,
                            ("$"+shoes_list[index[0]].cost),
                            shoes_list[index[0]].quantity))
    print(display_data)  # Data.

    
    input("Press enter to return to the menu.")

# def hughest quantity that finds the highest quantity shoe in stock using for loops,indexing.list and increments
def highest_qty(): 
   
    shoes_list = read_shoes_data()
    highest_stock = []  

     
    for item in range(1, len(shoes_list)):
        quantity_number = (shoes_list[item].quantity)
        highest_stock.append(int(quantity_number))

    # finds the index of the stock with the largest amount
    index = [index for index, high in enumerate(highest_stock) 
                if high == max(highest_stock)]

               
    index = int(index[0]) + 1  

    # displays the info
    print(f"{shoes_list[index].product} in "
        f"{shoes_list[index].country} IS ON SALE!"
        f"\nThe code is: {shoes_list[index].code}! "
    )

    
    input("Press enter to return to the menu.")

# def value per item that calculates the total value of each shoe using a formular
def value_per_item():
   
    shoes_list = read_shoes_data()

    # created a list that gets appended the shoe list
    cost_list = []  

    # once it is appened it gets the cost from the shoe list
    [cost_list.append(shoes_list[i].get_cost())    
        for i in range(1, len(shoes_list))]

    # Converted it to int
    cost_list = [int(cost) for cost in cost_list]

    # created another list that gets the quntity for the calculation
    qty_list = []  # Quantity values list

    # appened the quanitities to the empty list
    [qty_list.append(shoes_list[i].get_quantity()) 
        for i in range(1, len(shoes_list))]

    
    qty_list = [int(quanity) for quanity in qty_list]

    # calculation for the value
    value_list = []
    for i in range(0, len(qty_list)):
        value_value = qty_list[i] * cost_list[i]
        value_list.append(value_value)  

    
    display = ("{:<15} {:<11} {:<22} {:<15}"\
                .format("Country",
                    "Code",
                    "Product",
                    "Value"))
    print(display)  

    # prints all the info including calculation
    for i in range(0,len(shoes_list)-1):
        display_data = ("{:<15} {:<11} {:<22} {:<15}"\
                        .format(shoes_list[i+1].country,
                                shoes_list[i+1].code,
                                shoes_list[i+1].product,
                                ("$"+str(value_list[i]))))
        print(display_data)  # Data.

    
    input("Press enter to return to the menu.")

# created a menu using a while loop that is useer friendly
print("Inventory.")
menu = ""
while menu != "q":
    menu = input("\nChoose a menu item:"
                "\n view    - view all in stock"
                "\n restock - restrock the lowest quantity in inventory"
                "\n search  - search for shoe using code"
                "\n sale    - look at the items on sale"
                "\n value   - get the total value of item"
                "\n exit    - exits the program \n").lower()

    # prints out all items in stock
    if menu == "view":
        print()
        view_all()

    # user can restcock quantites if they would like
    elif menu == "restock":
        print()
        re_stock()
    
    # Searchs for shoe using code
    elif menu == "search":
        print()
        search_shoe()

    # checks all items on sale
    elif menu == "sale":
        print()
        highest_qty()
    
    # displays total value of stock for each item
    elif menu == "value":
        print()
        value_per_item()
    
    # exits the programe
    elif menu == "e":
        print()
        print("Goodbye.")
        exit()

    # incorrection option promt
    else:
        print("Incorrect entry. Try again.")
        break