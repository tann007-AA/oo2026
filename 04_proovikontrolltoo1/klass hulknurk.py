import math
import matplotlib.pyplot as plt

class Hulknurk:
    def __init__(self, nimi):
        
        self.nimi = nimi
        self.x_coords = []
        self.y_coords = []
        

    def lisa_punkt(self, x, y):
        
        self.x_coords.append(x)
        self.y_coords.append(y)
        
        
    def arvuta_umbermoot(self):
        n = len(self.x_coords)
        if n < 2: return 0.0
        umbermoot = 0.0
        for i in range(n):
            j = (i + 1) % n
            dx = (self.x_coords[j] - self.x_coords[i])**2
            dy = (self.y_coords[j] - self.y_coords[i])**2
            
            kaugus = math.sqrt(dx + dy)
            
            umbermoot += kaugus
        
        return umbermoot
            
    def joonista(self):
        x_plot = self.x_coords + [self.x_coords[0]]
        y_plot = self.y_coords + [self.y_coords[0]]
        
        plt.plot(x_plot, y_plot, marker = 'o')
        plt.show()

    def nihuta(self, dx, dy):
        self.x_coords = [x + dx for x in self.x_coords]
        self.y_coords = [y + dy for y in self.y_coords]
        
    def suurenda(self, faktor):
        self.x_coords = [x * faktor for x in self.x_coords]
        self.y_coords = [y * faktor for y in self.y_coords]
    
    def prindi_kulgede_pikkused(self):
        n = len(self.x_coords)
        if n < 2:
            print("Liiga vähe punkte")
            return
        
        print("\n---Külgede pikkused---")
        for i in range(n):
            j = (i + 1) % n
            dx = (self.x_coords[j] - self.x_coords[i])**2
            dy = (self.y_coords[j] - self.y_coords[i])**2
            pikkus = math.sqrt(dx + dy)
            print(f"Külg {i+1} (punktist {i} punkti {j}): {round(pikkus, 2)}")


def main():
    while True:
        nimi = input("\nSisesta kujundi nimi (või 'välju' lõpetamiseks): ")
        if nimi.lower() == 'välju': break
        
        kujund = Hulknurk(nimi)
        
        # Punktide sisestamine
        print("Sisesta koordinaadid (näiteks: 0 0). Kui oled valmis, kirjuta 'valmis'")
        while True:
            sisend = input("Punkt (x y): ")
            if sisend.lower() == 'valmis': break
            try:
                x, y = map(float, sisend.split())
                kujund.lisa_punkt(x, y)
            except ValueError:
                print("Palun sisesta koordinaadid arvudena (nt: 1 2)")

        # Menüü
        while True:
            print(f"\nValitud kujund: {kujund.nimi}")
            print("1) Arvuta ümbermõõt ja kuva küljed")
            print("2) Nihuta kujundit")
            print("3) Suurenda kujundit")
            print("4) Joonista kujund")
            print("5) Tekita uus kujund")
            valik = input("Vali tegevus (1-5): ")

            if valik == '1':
                print(f"Ümbermõõt: {round(kujund.arvuta_umbermoot(), 2)}")
                kujund.prindi_kulgede_pikkused()
            elif valik == '2':
                dx = float(input("Nihuta x võrra: "))
                dy = float(input("Nihuta y võrra: "))
                kujund.nihuta(dx, dy)
            elif valik == '3':
                f = float(input("Suurendusfaktor (nt 1.5): "))
                kujund.suurenda(f)
            elif valik == '4':
                kujund.joonista()
            elif valik == '5':
                break # Läheb tagasi uue kujundi loomise juurde
            else:
                print("Vale valik, proovi uuesti.")

# Käivitame programmi
if __name__ == "__main__":
    main()

        