import os

class Sistema:
    def Clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')