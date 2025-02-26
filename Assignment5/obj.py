from subclasses import Smartphone
from subclasses import Tablet
from subclasses import Laptop
from cart import Cart 
if __name__=='__main__':
    
    devices = [
    Smartphone("iPhone 13", 999, 10, 24, 6.1, 20),
    Smartphone("Samsung Galaxy S22", 899, 8, 24, 6.2, 18),
    Laptop("MacBook Pro", 1999, 5, 36, 16, 3.2),
    Laptop("Dell XPS 13", 1299, 7, 24, 8, 3.0),
    Tablet("iPad Air", 799, 12, 12, "2360x1640", 460),
    Tablet("Samsung Galaxy Tab S8", 699, 15, 12, "2560x1600", 500),
    
    Smartphone("Google Pixel 7", 799, 9, 24, 6.3, 19),
    Smartphone("OnePlus 10 Pro", 899, 10, 24, 6.7, 21),
    Smartphone("Xiaomi 12 Pro", 849, 12, 24, 6.73, 22),
    Smartphone("Sony Xperia 1 IV", 1199, 5, 24, 6.5, 17),
    Smartphone("ASUS ROG Phone 6", 999, 7, 24, 6.78, 24),
    Smartphone("Motorola Edge 30 Ultra", 899, 8, 24, 6.7, 20),
    Smartphone("Realme GT 2 Pro", 749, 10, 24, 6.7, 23),

    Laptop("HP Spectre x360", 1599, 6, 36, 14, 3.1),
    Laptop("Lenovo ThinkPad X1 Carbon", 1899, 4, 36, 14, 3.5),
    Laptop("Microsoft Surface Laptop 5", 1399, 9, 36, 13.5, 3.2),
    Laptop("Razer Blade 15", 2499, 3, 36, 15.6, 4.1),
    Laptop("Acer Swift 5", 1299, 8, 24, 14, 3.0),
    Laptop("Gigabyte Aorus 15", 1799, 6, 24, 15.6, 4.0),

    Tablet("Microsoft Surface Pro 9", 1099, 10, 12, "2880x1920", 450),
    Tablet("Lenovo Tab P12 Pro", 699, 12, 12, "2560x1600", 400),
    Tablet("Amazon Fire HD 10", 199, 20, 12, "1920x1200", 224),
    Tablet("Huawei MatePad Pro", 799, 15, 12, "2560x1600", 460),
    Tablet("Apple iPad Pro 12.9", 1299, 8, 12, "2732x2048", 460),
    Tablet("Samsung Galaxy Tab A8", 329, 18, 12, "1920x1200", 380),
    Tablet("Xiaomi Pad 5", 499, 16, 12, "2560x1600", 400)
]

    cart = Cart()

    def main():
        
        while True:
            print("\n1. Show Devices\n2. Show Cart\n3. Exit")
            choice = input("Enter your choice:(write only number of choice)")
    
            if choice == "1":
                for index, device in enumerate(devices):
                    print(f"{index + 1}. {device}")
                device_choice = int(input("Select a device to add to cart (or 0 to go back): ")) - 1
                if 0 <= device_choice < len(devices):
                    quantity = int(input("Enter quantity: "))
                    print(cart.add_device(devices[device_choice], quantity))
            elif choice == "2":
                print("\nCart Items:")
                print(cart.print_items())
                print(cart.get_total_price())
                if input("Proceed to checkout? (y/n): ").lower() == "y":
                    print(cart.checkout())
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")
    main()