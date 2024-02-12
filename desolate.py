from abc import ABC, abstractmethod
#from main import Main


class Desolate:


    def __init__(self):
        self.remote_battery = 2
    
    @abstractmethod
    def inventory(self, water: str, knife: bool):
        self.water = water
        self.knife = knife


    def desolate():
        print()
        print("""You have arrived to a desolate wasteland.
You must find ways to survive in this land of nothing.
Each time you arrive to a new destination you must find a charging port.
Time is of the essance.... 
The remote will point you in the right direction, but once it dies you will be on your own.
Find the charging port before the battery dies and you could still make it out of here with your life.
    """)
        print()
        print("""You can see mountains off in the distance. You are currently standing with sand all around you.
There is a Juniper Berry Bush 50 meters away. You see a tipped over empty fishing boat hull a few meters away from the tree.
The remote is telling you the charging port will take 2 days of walking to get to. You have a quarter charge worth of battery left.
Depending on how often the remote is used 1/8 of charge will keep the remote on for two days.""")
        print()
        decision1 = input(print("""Do you want to make camp for the night (1) 
                or 
continue walking to the charging port (2)?"""))
        print()
        
        if decision1 == "1":
            Desolate.make_camp()

        elif decision1 == "2":
            Desolate.keep_walking()

        else:
            Desolate.wrong_choice()
    
    
    def make_camp():
        print("""You have decided to make camp for the night.""")

    def keep_walking():
        print("""You have decided to continue walking through the night.""")

    def wrong_choice(self):
        self.remote_battery -= 1
        print(f"""You have made the wrong choice and ended up in a precarious situation. 
Your remote is down to {self.remote_battery}""")


    desolate()
