import sys
import time


class Interface():

    def __init__(self):
        self.inventory = []
        self.remote_battery = 2
        self.stored_state = []

    def remote_battery_percentage(self):
        remote_battery = int((self.remote_battery/8)*100)   
        if remote_battery <= 0 or remote_battery == None:
            remote_battery = 0
            Interface.print_slow("You no longer have any battery left in your remote. You are on your own.")
            print()
            return remote_battery
        return remote_battery
  
    def add_to_inventory(self, item):
        return {self.inventory.append(item)}

    def check_inventory(self):
        print()
        Interface.print_slow(f"""Your inventory is currently:
            
Inventory:  {self.inventory}
Battery:    {self.remote_battery_percentage()}%
            """)
        print()
        
    def display_options(self, list_options: list):
        list_options += ["Check Inventory", "Quit"]
        while True:
            print()
            Interface.print_slow("Options: ")
            print()
            for i in range(len(list_options)):
                Interface.print_slow(f"{i+1}. {list_options[i]}"'\n')
            print()
            choice = input("Enter your choice: ").lower()
            print()
            if choice == str(len(list_options) - 1):
                self.check_inventory()
                continue
            elif choice ==  str(len(list_options)):
                Interface.print_slow("Well... it's your loss. ")
                sys.exit(0)
            return choice
      
    def previous_method(self):
        previous_method = self.stored_state.pop()
        previous_method()

    def wrong_choice(self):
        self.remote_battery -= 1
        print()
        print(f"""You have made the wrong choice and ended up in a precarious situation. 
Your remote is down to {self.remote_battery_percentage()}%. Try Again...
                """)
        self.previous_method()

    def print_slow_color(text, color_code):
        for char in text:
            print(f"\033[{color_code}m{char}\033[0m", end='', flush=True)
            time.sleep(0.2)

    def print_color(text, color_code):
        for char in text:
            print(f"\033[{color_code}m{char}\033[0m", end='', flush=True)
            time.sleep(0.01)
            
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.01) 

        
