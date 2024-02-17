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
            pass
        elif choice  == "2":
            pass
        else:
            self.wrong_choice()



cowboy = Cowboy()
cowboy.story()
