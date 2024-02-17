from interface import Interface
from future import Vault


class Main(Interface):

    def map():
        print("You project a holographic \
    map of the vent sytem of the \
    compound surrounding the vault")
        print("From the beginning \
    of the maze of vents you need to go \
    Left, Right, Right, Left, Straight")
        
def main():
    print("""You project a holographic
map of the vent sytem of the 
compound surrounding the vault""")
    print("""From the beginning 
of the maze of vents you need to go
Left, Right, Right, Left, Straight""")
    vault = Vault()
    vault.navigate_vents()

    #Desolate.arrived()
    #Cowboy.story() 
    #Add Wizard.py
       
   


if __name__ == "__main__":
    main()