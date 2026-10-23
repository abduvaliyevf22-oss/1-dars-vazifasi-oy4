class Contact:
    def __init__(self, ism, telefon):
        self.ism = ism
        self.telefon = telefon

    def update_phone(self, new_phone):
        self.telefon = new_phone

    def show_info(self):
        print(f"ism: {self.ism}")
        print(f"telefon: {self.telefon}")

contact = Contact('Malika', '901234567')
contact.update_phone('931112233')
contact.show_info()