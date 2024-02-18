import sys


class Interface():

    def __init__(self):
        self.inventory = []
        self.remote_battery = 2
        self.stored_state = []

    def remote_battery_percentage(self):
        return int((self.remote_battery/8)*100)
       
  
    def add_to_inventory(self, item):
        return {self.inventory.append(item)}
    

    def check_inventory(self):
        print()
        print(f"""Your inventory is currently:
            
Inventory:  {self.inventory}
Battery:    {self.remote_battery_percentage()}%
            """)
        print()
        
    def display_options(self, list_options: list):
        list_options += ["Check Inventory", "Quit"]
        while True:
            print()
            print("Options: ")
            for i in range(len(list_options)):
                print(f"{i+1}. {list_options[i]}")
            print()
            choice = input("Enter your choice: ").lower()
            print()
            if choice == str(len(list_options) - 1):
                self.check_inventory()
                continue
            elif choice ==  str(len(list_options)):
                print("Well... it's your loss. ")
                sys.exit(0)
            return choice
        
    def current_method(self):
        self.stored_state.append()
      
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

        
