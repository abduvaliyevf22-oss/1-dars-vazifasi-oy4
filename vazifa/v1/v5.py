class Player:
    def __init__(self,ism,energiya=100):
        self.ism = ism
        self.energiya = energiya
    def use_energy(self,amount):
        self.energiya -= amount 
        
    def show_status(self):
        print(f"oyinchi:{self.ism}")
        print(f"energiya:{self.energiya}")
         
player = Player('Hero')
player.use_energy(35)
player.show_status()