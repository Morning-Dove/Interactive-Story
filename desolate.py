
from interface import Interface
import desolate_decisions


class Desolate(Interface):

  
    def lonely(self):
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
            self.stored_state.append(self.lonely)
            self.wrong_choice()
    
    
    def make_camp(self):
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
        print(desolate_decisions.decisions["decision6"])
        self.survival()
        

    def injury(self):
        print("You have seriously injured your arm in the fire. ")


    def survival(self):
        print()
        choices = ["Go out looking for supplies? ", "Continue on your journey to find a charging port? "]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            self.make_camp()
        elif choice  == "2":
            self.keep_walking()
        else:
            self.stored_state.append(self.survival)
            self.wrong_choice()


desolate = Desolate()

desolate.lonely()