from abc import ABC, abstractmethod

class Toode(ABC):
    
    @abstractmethod
    def arvuta_hind(self):
        pass
    
    @abstractmethod
    def kuva_info(self):
        pass
    
class Elektroonika(Toode):
    
    def __init__(self, nimi, baashind, garantiiaasta):
        self.nimi = nimi
        self.baashind = baashind
        self.garantiiaasta = garantiiaasta
        
    def arvuta_hind(self):
        return self.baashind * 1.22
    
    def kuva_info(self):
        return f"{self.nimi} (Garantii:{self.garantiiaasta} aastat), Hind {self.arvuta_hind()} EUR"
    
class Riietus(Toode):
    
    def __init__(self, nimi, baashind, suurus):
        self.nimi = nimi
        self.baashind = baashind
        self.suurus = suurus
        
    def arvuta_hind(self):
        return self.baashind
    
    def kuva_info(self):
        return f"{self.nimi} (Suurus:{self.suurus}), Hind {self.arvuta_hind()} EUR"
    
ostukorv = [
    Elektroonika("Sülearvuti", 1100, 2),
    Riietus("T-särk", 25, "L"),
    Elektroonika("Kõrvaklapid", 60, 0.6)
]

for toode in ostukorv:
    print(toode.kuva_info())