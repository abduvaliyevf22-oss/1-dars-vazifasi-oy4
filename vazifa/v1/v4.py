from matplotlib.pylab import tri


class Ticket:
    def __init__(self,nomi,soni,narxi):
        self.nom =nomi
        self.soni = soni
        self.narx = narxi

    def total_cost(self):
        return self.narx * self.soni
        
    
    
    def show_info(self):
        print(f"kino nomi:{self.nom}")
       

ticket = Ticket('Avatar', 40000, 3)
print(ticket.total_cost())
