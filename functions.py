from typing import List, Dict
import pickle

#set to none to avoid call before creation error
data = {"all_trollies": [], "incoming_products": [], "num_trolly": 0}

def load():
    # loads all the saved data from previous runs
    global data
    with open("data.p", "rb") as f:
        data = pickle.load(f)

def reset():
    # sets the variables within 'data.p' into a blank list or 0
    global data
    Trolly.all_trollies = []
    Product.incoming_products = []
    Trolly.num_trolly = 0

    data = {"all_trollies": Trolly.all_trollies, "incoming_products": Product.incoming_products, "num_trolly": Trolly.num_trolly}
    with open("data.p", 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

        
class Compartment:
    """Storage for the products

        Attrs:
            compartments (Dict): Storage for products organized by category
            category (str): category of the item (food, book, games etc.)
            shelf (List): shelf of a compartment to further organize products
                            into alphabetical order
    """
    compartments = {"food": [], "electronics": [], "clothing": [], "books": [], "games": [], "movies/music": [], "health/beauty": [], "sports": []}
    
    def __init__(self, category):
        self.category = category
        self.shelf = []

    def add_product(self, category, Product):
        if Product.category in compartments.keys():
            compartments[f"{Product.category}"] = f"{Product.name}"
        else:

            compartments.add(f"{Product.category}", f"{Product.name}")

            
class Trolly:
    """ thing that transfers products
    attrs:
        all_trollies(List[Trolly]) = list of objects containing all created trollies
        num_trolly(int) = number of trollies that have been created
        storage(List[Product]) = list of objects containg all the products within a trollies' storage 
        weight_capacity(int) = the maximum amount of weight a trollies' storage can contain
        id(int) = creation number of the trolly
    """
    all_trollies = data["all_trollies"]
    num_trolly = data["num_trolly"]

    def __init__(self):
        # creates the trolly
        self.storage = []
        self.weight_capacity = 100
        self.id = Trolly.num_trolly
        Trolly.num_trolly += 1
        Trolly.all_trollies.append(self)
    
    def calculate_weight(self):
        # calculates the amount of weight currently being held by the trollies' storage
        total_weight = 0
        for product in self.storage:
            total_weight += product.weight
        return total_weight

    def __str__(self):
        return f"ID: {self.id}"


class Product:
    """ cant put in words do 4 me :D?
        attrs:
            incoming_products(List[Product]): products ready to be loaded
            name(str) = name of the product
            weight(int) = weight of the product
            barcode(int) = product's barcode
            loc(int) = where the product currently is)
    """
    incoming_products = data["incoming_products"]
    
    def __init__(self, name: str, weight: int, barcode: int):
        """ creates the product
        args:
            name(str) = name of the product
            weight(int) = weight of the product
            barcode(int) = product's barcode
        """
        self.name = name
        self.weight = weight
        self.barcode = barcode
        self.loc = -1
        Product.incoming_products.append(self)
    
    def __str__(self):
        return f"Name: {self.name} Code: {self.barcode}"

    """
    def package(self, address: str, warning: str=None):
        "" prepares the product for shipping (shipping has not been implemented yet)
        args:
            address = where the product will be sent
            warning = any hazards the product poses
        ""
        self.address = address
        self.warning = warning
    """

    @staticmethod
    def empty_incoming():
        """ removes all incoming_products"""
        Product.incoming_products = []


class Shipment:
    """ write 4 me. i am lazy!!!!!!!
    attrs:
        name(str): name of the shipment
        products(List[Product]): products within the shipment
    """
    def __init__(self, name: str, products: List[Product]):
        """ creates the shipment
        args:
            name = name of the shipment
            products = products within the shipment
        """
        self.name = name
        self.products = products
    
    def load_to_trolly(self):
        # transfer the all the products in the shipment into the available trollies
        for i, product in enumerate(self.products):
            for trolly in Trolly.all_trollies:
                if (trolly.calculate_weight() + product.weight) > trolly.weight_capacity:
                    continue
                else:
                    print(f"{product.name} was transfered.")
                    trolly.storage.append(product)
                    product.loc = trolly.id
                    Product.incoming_products[i] = 'empty'
                    break
        i = 0
        while True:
            if Product.incoming_products[i] == 'empty':
                Product.incoming_products.pop(i)
            else:
                i += 1
            
            if i == len(Product.incoming_products):
                break
        del i

        # Product.empty_incoming()
    
    def check_remaining_products(self):
        # prints out the products in the shipment
        for product in Product.incoming_products:
            print(product)
    
    def __str__(self):
        for product in self.products:
            return str(product)

def save():
    # saves changed data to the data.p file
    data = {"all_trollies": Trolly.all_trollies, "incoming_products": Product.incoming_products, "num_trolly": Trolly.num_trolly}
    with open("data.p", "wb") as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def main():
    """if you are not using the program, you have to access the Trolly.all_trollies
    via the dictionaries in data.p file. Otherwise, printing the trollies in Trolly.all_trollies
    will return a blank list, since they have been yet to be declared.
    """

    leave = False
    action = ""
    input_message = "What would you like to do? "

    input_actions = {
        'options': ["options", "ops", "option"],
        'mean': ['mean', "i hate you", "you suck", 'die', 'kys', 'no u'],
        'exit': ["leave", "exit", "goodbye", "bye", "quit", "quit"],
        'make trolly': ['make trolly', 'trolly', 'mt'],
        'make product': ['make product', 'product', 'mp']

    }

    while True:
        print()
        save()
        load()
        
        # Asks person what they want
        action = input(input_message)
        action = action.lower()

        # Action: Prints out the options
        if action in input_actions["options"]:
            for action in input_actions.keys():
                if action == "mean":
                    continue
                print(action)
            continue
        
        # Action: Mean action
        if action in input_actions["mean"]:
            print("Is this what you wanted?")
            reset()
            save()
            load()
            continue

        # Action: Exit
        if action in input_actions["exit"]:
            print()
            print("Thank you for your time here at the " + '\u0336'.join("Mind Control Marketplace") + '\u0336' + " The Amazon Grim Reaper Marketplace")
            print("We " + '\u0336'.join("WILL") + '\u0336' + " hope to see you again!")
            break
        

        print("That was an invalid response.")
        print()



    '''
    for kkk in range(5):
        Product('Pineapple Pizza' + str(kkk), 5, 234234)
    Product('Horse Sushi', 6, 342324)
    Trolly()

    box = Shipment('Shipment 1', Product.incoming_products)

    box.load_to_trolly()

    print(Product.incoming_products)

    save()
    '''
    
if __name__ == '__main__':
    load()
    main()
