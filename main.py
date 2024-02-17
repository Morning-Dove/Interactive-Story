from interface import Interface
from future import Vault
from desolate import Desolate
from cowboy import Cowboy


class Main(Interface):

    def __init__(self):
        self.vault = Vault()
        self.desolate = Desolate()
        self.cowboy = Cowboy()

    def map():
        print("You project a holographic \
    map of the vent sytem of the \
    compound surrounding the vault")
        print("From the beginning \
    of the maze of vents you need to go \
    Left, Right, Right, Left, Straight")
        
    def run(self):
        print("""You project a holographic
    map of the vent sytem of the 
    compound surrounding the vault""")
        print("""From the beginning 
    of the maze of vents you need to go
    Left, Right, Right, Left, Straight""")
        self.vault.navigate_vents()
        self.desolate.arrived()
        self.cowboy.story()
    #Add Wizard.py
       
   


if __name__ == "__main__":
    main = Main()
    main.run()