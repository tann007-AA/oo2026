class Raamat:
    def __init__(self, pealkiri, lehti, kiirus):
        self.pealkiri = pealkiri
        self.lehti = lehti
        self.kiirus = kiirus

class Planeerija:
    def arvuta(self, raamat, paevi):
        if paevi <= 0 or paevi > 365: return None
        lehti_paevas = raamat.lehti / paevi
        minutid = lehti_paevas * raamat.kiirus
        return {"lehti": round(lehti_paevas, 1), "tunnid": int(minutid // 60), "minutid": int(minutid % 60)}

# --- Graafiline objekt (Vaade) ---
class GraafilineKaart:
    """Vastutab info visuaalse esitamise eest."""
    def kuva(self, raamat, tulemus):
        print("\n" + "="*30)
        print(f" RAAMAT: {raamat.pealkiri.upper()}")
        print("-" * 30)
        print(f" Päevane norm: {tulemus['lehti']} lk")
        print(f" Ajaline kulu: {tulemus['tunnid']}h {tulemus['minutid']}min")
        print("="*30 + "\n")

# --- Haldusklass (Kontroller) ---
class RaamatukoguHaldur:
    def __init__(self):
        self.nimekiri = [] # Siin hoiame kõiki objekte koos

    def lisa_uus_plaan(self):
        nimi = input("Raamatu nimi: ")
        lehti = int(input("Lehekülgi: "))
        kiirus = float(input("Kiirus (min/lk): "))
        paevi = int(input("Päevi lugemiseks: "))

        raamat = Raamat(nimi, lehti, kiirus)
        tulemus = Planeerija().arvuta(raamat, paevi)

        if tulemus:
            # Salvestame selle komplekti oma listi
            self.nimekiri.append({"raamat": raamat, "tulemus": tulemus})
            print("Lisatud!")
        else:
            print("Viga: Ebarealistlik tähtaeg.")

    def kuva_koik(self):
        kaart = GraafilineKaart() # Loome vaate-objekti
        for item in self.nimekiri:
            # Graafiline objekt tegeleb nüüd printimisega
            kaart.kuva(item['raamat'], item['tulemus'])

# --- Käivitamine ---
haldur = RaamatukoguHaldur()

while True:
    valik = input("Vali: [1] Lisa uus, [2] Kuva kõik, [3] Välju: ")
    if valik == "1": haldur.lisa_uus_plaan()
    elif valik == "2": haldur.kuva_koik()
    elif valik == "3": break