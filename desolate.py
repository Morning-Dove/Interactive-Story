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
        print()
        choices = ["Hope you don't run into anyone? ", "Make a plan? "]
        choice = self.display_options(choices)
        if choice  == "1":
            print(desolate_decisions.decisions["decision13"])
            self.inventory.append("knife")
            self.finish_the_journey()
        elif choice  == "2":
            print(desolate_decisions.decisions["decision14"])
            self.inventory.append("knife")
            pass
        else:
            self.stored_state.append(self.continue_journey)
            self.wrong_choice()

    def finish_the_journey(self):
        print("""As soon as the sun was low enough in the sky for it to begin cooling off, you begin following the map to the charging port.
You ran like you have never run before. You are on a mission to get out of here.""")
        self.next_era()

    def overthinking(self):
        print("""Your theory was correct. You overthink everything. 
Once it is cool enough to start moving agian, you stay in your head thinking about all the what if scenarios and pay no attention to where you are at.
You fall into a gully carved out by torrential down pours of rain. When you fall into the gully you break your leg.""")
        self.player_dies()


    def keep_walking(self):
        self.remote_battery -= 1
        print()
        print(desolate_decisions.decisions["decision6"],{self.remote_battery_percentage()})
        choices = ["Go out looking for supplies? ", "Continue on your journey to find a charging port? "]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            print(desolate_decisions.decisions["decision15"])
            self.player_dies()
        elif choice  == "2":
            print(desolate_decisions.decisions["decision16"])
            self.next_era()
        else:
            self.stored_state.append(self.keep_walking)
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
            self.stored_state.append(self.injury)
            self.wrong_choice() 

    def survival(self):
        print()
        print(desolate_decisions.decisions["decision8"])
        choices = ["Continue pushing to the charge station?", "Take a small break?"] 
        print()
        choice = self.display_options(choices)
        if choice == "1":
            self.next_era()
        elif choice  == "2":
            self.aloe_vera_poison()
        else:
            self.stored_state.append(self.survival)
            self.wrong_choice()

    def next_era(self):
        print("""You have made it to the charging port. 
You plug-in the remote to start charging.
You are not totally sure of where you are going next.
The remote charges quickly. You are off to your next destination! """)
        

    def aloe_vera_poison(self):
        print("""The plant you thought was aloe vera turned out to be Aloe ruspoliana.
A poisonous plant that looks similar to Aloe vera. 
You start to become extremely ill while preparing a fire and waiting for your water to boil. 
You pass out. When you wake up...""")
        self.player_dies()


    def player_dies(self):
        print("""Your remote battery ends up dying. 
You aren't fully sure of where to go from here.
You succumb to your injurys and lack of food and water.
You Die. May peace be with you.
              """)
        sys.exit(0)
        


desolate = Desolate()
desolate.arrived()