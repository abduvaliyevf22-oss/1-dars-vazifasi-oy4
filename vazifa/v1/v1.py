class Athlete:
    def __init__(self,ism,sport_turi,yoshi):
        self.ism = ism
        self.tur = sport_turi
        self.yosh = yoshi
    def show_info(self):
        print(f"ism:{self.ism}")
        print(f"sport turi:{self.tur}")
        print(f"yoshi:{self.yosh}")

athlete = Athlete('Ali', 'Futbol', 20)
athlete.show_info()
