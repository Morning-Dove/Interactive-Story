import sys
from colorama import Fore, Style, init
from interface import Interface
import desolate_decisions


class Desolate(Interface):

    init(autoreset=True)

    def arrived(self):
        print()
        print(desolate_decisions.decisions["decision1"])
        print()
        print(desolate_decisions.decisions["decision2"])
        choices  = ["Make camp for the night?", "Continue walking?"]
        self.add_to_inventory("rope")
        print()
        self.stored_state.append(self.arrived)
        choice = self.display_options(choices)
        if choice == "1":
            self.make_camp()
        elif choice  == "2":
            self.keep_walking()
        else:
            self.wrong_choice()
    
    
    def make_camp(self):
        print()
        print(desolate_decisions.decisions["decision3"])
        print()
        choices = ["Fire for the night?", "See how bright all the stars are?"]
        choice = self.display_options(choices)
        if choice  == "1":
            print(desolate_decisions.decisions["decision4"])
            self.injury()
        elif choice  == "2":
            print(desolate_decisions.decisions["decision5"])
            self.continue_journey()

        else:
            self.stored_state.append(self.make_camp)
            self.wrong_choice()


    def continue_journey(self):
        print()
        print(desolate_decisions.decisions["decision9"])
        print()
        choices = ["Travel at night? ", "Move slowly and take more breaks? "]
        choice = self.display_options(choices)
        if choice  == "1":
            print(desolate_decisions.decisions["decision10"])
            self.keep_the_kinfe()
        elif choice  == "2":
            print(desolate_decisions.decisions["decision11"])
            self.player_dies()
        else:
            self.stored_state.append(self.continue_journey)
            self.wrong_choice()


    def keep_the_kinfe(self):
        print()
        print(desolate_decisions.decisions["decision12"])
        self.add_to_inventory("knife")
        print()
        choices = ["Hope you don't run into anyone? ", "Make a plan? "]
        choice = self.display_options(choices)
        if choice  == "1":
            print(desolate_decisions.decisions["decision13"])
            self.next_era()
        elif choice  == "2":
            print(desolate_decisions.decisions["decision14"])
            self.player_dies()
        else:
            self.stored_state.append(self.continue_journey)
            self.wrong_choice()


    def keep_walking(self):
        self.remote_battery -= 1
        if self.remote_battery_percentage == 0:
            self.player_dies()
        print()
        print(desolate_decisions.decisions["decision6"])
        choices = ["Go out looking for supplies? ", "Continue on your journey to find a charging port? "]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            print(desolate_decisions.decisions["decision15"])
            self.add_to_inventory("broken pottery")
            self.add_to_inventory("fishing line") 
            print(desolate_decisions.decisions["decision18"])
            print()
            print(*self.inventory, sep=", ")
            print()
            self.player_dies()
        elif choice  == "2":
            print(desolate_decisions.decisions["decision16"])
            self.next_era()
        else:
            self.stored_state.append(self.keep_walking)
            self.wrong_choice() 


    def injury(self):
        self.remote_battery -= 1
        if self.remote_battery_percentage == 0:
            self.player_dies()
        print()
        print(desolate_decisions.decisions["decision7"])
        choices = ["Walk through the night? ", "Stop and make camp? "]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            self.survival()
        elif choice  == "2":
            self.player_dies()
        else:
            self.stored_state.append(self.injury)
            self.wrong_choice() 


    def survival(self):
        print()
        print(desolate_decisions.decisions["decision8"])
        choices = ["Continue pushing to the charge station?", "Take a small break?"] 
        self.add_to_inventory("water")
        print()
        choice = self.display_options(choices)
        if choice == "1":
            self.next_era()
        elif choice  == "2":
            print(desolate_decisions.decisions["decision17"])
            self.player_dies()
        else:
            self.stored_state.append(self.survival)
            self.wrong_choice()


    def next_era(self): 
        next_world = """You have made it to the charging port. 
You plug-in the remote to start charging.
You are not totally sure of where you are going next.
The remote charges quickly. You are off to your next destination! 
              
________________________________NEW_WORLD________________________________________
                         
                    """
        
        print(Fore.CYAN + Style.BRIGHT + next_world)


    def player_dies(self):
        print_statement = """Your remote battery ends up dying. 
You aren't fully sure of where to go from here.
You succumb to your injurys and lack of food and water.
You Die. May peace be with you.
              """
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + print_statement)
        sys.exit(0)
        

desolate = Desolate()
desolate.arrived()