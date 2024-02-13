from abc import ABC, abstractmethod
from fractions import Fraction

#from main import Main

           
class Desolate: #(Main)

    def __init__(self):
        pass
   

    def inventory(self):
        self.remote_battery = 4.0


    def lonely(self):
        decision1 = input("""Do you want to make camp for the night (1) 
                or 
Continue walking to the charging port (2)?
                """)
        print()
        if decision1 == "1":
            self.make_camp()

        elif decision1 == "2":
            self.keep_walking()

        else:
            self.wrong_choice()
    
    
    def make_camp(self):
        print("""You have decided to make camp. 
You pull the boat hull over to the tree to make a shelter for the night.
You lean the boat against the tree to help provide a wind break and shelter from any potential rain.""")
        print()
        decision2 = input("""Do you make a fire for the night (1)
                        or 
Do you enjoy seeing how bright all the stars are(2)?
                """)
    
        if decision2 == "1":
            print("""You made a fire. You fall asleep with the fire still going. 
A few embers blew up into the dried up juniper berry tree and lit the whole tree on fire. 
You wake up and have to get out quickly. While springing out of your makeshift bed, 
you almost forgot the remote in the shelter. When you turn back for the remote the wind blows the fire directly towards you.
You are able to get the remote, but not without injury. You burn your arm right arm and right hand.
                """)
    
        elif decision2 == "2":
            print("""You are staring at the stars for the night. 
You begin to think about what you need to do to survive. 
You think you will be able to figure it out long enough to charge your remote and
hopefully make it to another place that it will be easier to survive in.
                """)
        
        else:
            self.wrong_choice()


    def keep_walking(self):
        self.remote_battery -= 1
        print(f"""You have decided to continue walking through the night. 
The remote GPS is pointing you towards the mountain. You begin making the dangerous and trecherous walk to continue your travels. 
You are grateful there is a full moon tonight and you are able to walk in the brightly lit starry night sky. 
Since you had to light the remote up so many times you notice the battery is draining faster than you expected. 
By early morning the remote battery is down {Fraction(self.remote_battery/8)}
                """)

    def wrong_choice(self):
        self.remote_battery -= 2
        print(f"""You have made the wrong choice and ended up in a precarious situation. 
Your remote is down to {Fraction(self.remote_battery/8)}.
                """)



def main():
        desolate = Desolate()
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
Depending on how often the remote is used 1/4 of charge will keep the remote on for two days.
                """)
        desolate.lonely()
      


if __name__ == "__main__":
    main()
