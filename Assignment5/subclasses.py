from device import Device
class Smartphone(Device):
    def __init__(self,  name, price, stock, warranty_period, screen_size, battery_life):
        super().__init__( name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Warranty Period: {self.warranty_period} Screen Size: {self.screen_size} Battery Life: {self.battery_life}'

    def display_info(self):
        return f'Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Warranty Period: {self.warranty_period} Screen Size: {self.screen_size} Battery Life: {self.battery_life}'
    
    def make_call(self):
        print('Make a call')
        return

    def install_app(self):
        return f'Install an app'

class Laptop(Device):
    
    def __init__(self, name, price, stock, warranty_period, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size =  ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Warranty Period: {self.warranty_period} RAM size: {self.ram_size} Processor Speed: {self.processor_speed}'

    def display_info(self):
          return f'Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Warranty Period: {self.warranty_period} RAM size: {self.ram_size} Processor Speed: {self.processor_speed}'
        
    def run_program(self):
        return f'Run Program '

    def use_keyboard(self):
        return f'Use Keyboard'

class Tablet(Device):
    def __init__(self, name, price, stock, warranty_period, screen_resolution, weight):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def display_info(self):
         return f'Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Warranty Period: {self.warranty_period} Screen Resolution {self.screen_resolution} Weight: {self.weight}'
        
    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Warranty Period: {self.warranty_period} Screen Resolution {self.screen_resolution} Weight: {self.weight}'

    def browse_internet(self):
        return f'Browse Internet'

    def use_touchscreen(self):
        return f'Use touchscreen'