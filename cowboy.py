import sys
from colorama import Fore, Style
from interface import Interface
import cowboy_decisions


class Cowboy(Interface):

    def story(self):
        print()
        print(cowboy_decisions.decisions["decision1"])
        choices = ["Blend in with everyone else? ", "Jump out from behind the counter?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            print(cowboy_decisions.decisions["decision2"])
            self.add_to_inventory("random person's clothes")
            self.blend_in()
        elif choice  == "2":
            print(cowboy_decisions.decisions["decision3"])
            self.do_not_shoot()
        else:
            self.stored_state.append(self.story)
            self.wrong_choice()


    def blend_in(self):
        print()
        print(cowboy_decisions.decisions["decision4"])
        choices = ["Stop and get them a drink?", "Keep walking out?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            print(cowboy_decisions.decisions["decision5"])
            self.become_the_bartender()
        elif choice  == "2":
            print(cowboy_decisions.decisions["decision6"])
            self.the_end()
        else:
            self.stored_state.append(self.blend_in)
            self.wrong_choice()


    def become_the_bartender(self):
        print()
        print(cowboy_decisions.decisions["decision7"])
        choices = ["Befriend the Saloon patrons?", "Continue to sneak away?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            print(cowboy_decisions.decisions["decision8"])
            self.add_to_inventory("new friends")
            self.break_in()
        elif choice  == "2":
            print(cowboy_decisions.decisions["decision9"])
            self.the_end()
        else:
            self.stored_state.append(self.become_the_bartender)
            self.wrong_choice()

    def break_in(self):
        print()
        print(cowboy_decisions.decisions["decision10"])
        choices = ["Convince your new friends?", "Break in alone?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            print(cowboy_decisions.decisions["decision11"])
            self.to_the_vault()
        elif choice  == "2":
            print(cowboy_decisions.decisions["decision12"])
            self.the_end()
        else:
            self.stored_state.append(self.break_in)
            self.wrong_choice()

    def to_the_vault(self):
        print()
        print(cowboy_decisions.decisions["decision13"])
        choices = ["Let everyone else in behind you?", "Quickly lock the window behind you?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            print(cowboy_decisions.decisions["decision14"])
            self.fully_charged()
        elif choice  == "2":
            print(cowboy_decisions.decisions["decision15"])
            self.fully_charged()
        else:
            self.stored_state.append(self.break_in)
            self.wrong_choice() 
 

    def do_not_shoot(self):
        print()
        print(cowboy_decisions.decisions["decision16"])
        choices = ["Will you survive to tell the tale?", "Will this be the end?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            print(cowboy_decisions.decisions["decision17"])
            self.the_end()
        elif choice  == "2":
            print(cowboy_decisions.decisions["decision18"])
            self.fully_charged()
        else:
            self.stored_state.append(self.do_not_shoot)
            self.wrong_choice() 

    def fully_charged(self):

        next_world = """You have made it to the charging port. 
You plug-in the remote to start charging.
You are not totally sure of where you are going next.
The remote charges quickly. You are off to your next destination!
              
________________________________NEW_WORLD________________________________________
              """
        print(Fore.CYAN + Style.BRIGHT + next_world)


    def the_end(self):
        print_statement = "You don't make it to the charging port. You never make it out of this world." 
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + print_statement)
        sys.exit(0)

cowboy = Cowboy()
cowboy.story()



