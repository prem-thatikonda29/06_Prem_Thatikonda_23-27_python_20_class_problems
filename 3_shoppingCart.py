class ShoppingCart:
    def __init__(self):
        self.cart = []

    
    def add_items(self):
        item = input("Enter the name of the item you want to add: ").capitalize()
        quantity = int(input("How many would you like: "))
        price = float(input("Enter price of item: Rs."))
        self.cart.append({'item': item, 'quantity': quantity, 'price': price})
    

    def remove_items(self):     
        if len(self.cart) == 0: 
            print("Your cart is empty.")
        else:
            print("\nItems in your shopping cart:\n")
            for i in range(len(self.cart)):
                print(f"{i+1}. {self.cart[i]['item']} - Rs.{self.cart[i]['price']} ({self.cart[i]['quantity']})")

            selection = int(input('\nEnter number of item you wish to remove: '))
            if (selection > 0 and selection <= len(self.cart)+1) :
                del self.cart[selection-1]
            elif selection == 0:
                self.clear_all()
                return
    
    def clear_cart(self):
        self.cart.clear()


    def view_cart(self):
        if len(self.cart) == 0: 
            print("Your cart is empty.")
        else:
            for i in range(len(self.cart)):
                print(f"{i+1}. {self.cart[i]['item']} - Rs.{self.cart[i]['price']} ({self.cart[i]['quantity']})")

            
    def calculate_price(self):
        total = sum([item['price'] * item['quantity'] for item in self.cart])
        return total

def main():
    shop = ShoppingCart()
    while True:
        print("\n1)Add Items")
        print("2)Remove Items")
        print("3)Clear Cart")
        print("4)View Cart")
        print("5)Calculate Price")
        print("6)Checkout")
        print('7)Exit shop\n')
        choice = int(input("What do you want to do? "))
        if choice == 1:
            shop.add_items()
        elif choice == 2:
            shop.remove_items()
        elif choice == 3:
            shop.clear_cart()
        elif choice==4:
            shop.view_cart()
        elif choice == 5:
            print("Total:" ,shop.calculate_price())
        elif choice == 6:
            print(f"Checking out...\nRs. {shop.calculate_price()} credited from your account\nYour items will be delivered shortly.")
            shop.clear_cart()
        elif choice == 7:
            exit()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()