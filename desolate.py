
import sys
from interface import Interface
import desolate_decisions


class Desolate(Interface):

  
    def arrived(self):
        print()
        print(desolate_decisions.decisions["decision1"])
        print()
        print(desolate_decisions.decisions["decision2"])
        choices  = ["Make camp for the night?", "Continue walking?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            self.make_camp()
        elif choice  == "2":
            self.keep_walking()
        else:
            self.stored_state.append(self.arrived)
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
            self.survival()
        elif choice == "3":
            self.display_options()
        else:
            self.stored_state.append(self.make_camp)
            self.wrong_choice()


    def keep_walking(self):
        self.remote_battery -= 1
        print()
        print(desolate_decisions.decisions["decision6"],{self.remote_battery_percentage()})
        choices = ["Go out looking for supplies? ", "Continue on your journey to find a charging port? "]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            pass
        elif choice  == "2":
            pass
        else:
            self.stored_state.append(self.survival)
            self.wrong_choice() 

    def injury(self):
        self.remote_battery -= 1
        print()
        print(desolate_decisions.decisions["decision7"],{self.remote_battery_percentage()})
        choices = ["Walk through the night? ", "Stop and make camp? "]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            self.survival()
        elif choice  == "2":
            self.player_dies()
        else:
            self.stored_state.append(self.survival)
            self.wrong_choice() 

    def survival(self):
        print(desolate_decisions.decisions["decision8"])
        choices = [""] 
        print()
        choice = self.display_options(choices)
        if choice == "1":
            self.next_era()
        elif choice  == "2":
            pass
        else:
            self.stored_state.append(self.survival)
            self.wrong_choice()

    def next_era(self):
        pass

    def player_dies(self):
        print("""You chose to stop and make camp for the night. 
Your remote battery ends up dying. 
You aren't fully sure of where to go from here.
You succumb to your injurys and lack of food and water.
You Die. May peace be with you.
              """)
        sys.exit(0)
        


desolate = Desolate()
desolate.arrived()