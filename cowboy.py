import sys
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
            self.blend_in()
        elif choice  == "2":
            print(cowboy_decisions.decisions["decision3"])
            pass
        else:
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
            self.wrong_choice()


    def become_the_bartender(self):
        print()
        print(cowboy_decisions.decisions["decision7"])
        choices = ["Befriend the Saloon patrons?", "Continue to sneak away?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            print(cowboy_decisions.decisions["decision8"])
            self.break_in()
        elif choice  == "2":
            print(cowboy_decisions.decisions["decision9"])
            self.the_end()
        else:
            self.wrong_choice()

    def break_in(self):
        print()
        print(cowboy_decisions.decisions["decision10"])
        choices = ["Convince your new friends?", "Break in alone?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            print(cowboy_decisions.decisions["decision11"])
            self.break_in()
        elif choice  == "2":
            print(cowboy_decisions.decisions["decision12"])
            self.the_end()
        else:
            self.wrong_choice()
 

    def do_not_shoot(self):
        print()
        print(cowboy_decisions.decisions["decision"])
        choices = [""]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            print(cowboy_decisions.decisions["decision"])
            pass
        elif choice  == "2":
            print(cowboy_decisions.decisions["decision"])
            pass
        else:
            self.wrong_choice() 


    def the_end(self):
        print("You don't make it to the charging port. You never make it out of this world.")
        sys.exit(0)

cowboy = Cowboy()
cowboy.story()



