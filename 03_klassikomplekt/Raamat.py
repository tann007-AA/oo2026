class Raamat:
    def __init__(self, pealkiri, lehekyljed, lugemiskiirus):
        self.pealkiri = pealkiri
        self.lehekyljed = lehekyljed
        self.lugemiskiirus = lugemiskiirus
        
class Planeerija:
    # Teeb arvutusi, kasutades Raamat-objekti andmeid
    def __init__(self, raamat):
        self.raamat = raamat
        
    def arvuta_plaan(self, paevade_arv):
        if paevade_arv <= 0 or paevade_arv > 365:
            return None
        
        lehti_paevas = self.raamat.lehekyljed / paevade_arv
        minutid_kokku = lehti_paevas * self.raamat.lugemiskiirus
        
        return {
            "lehti": round(lehti_paevas, 1),
            "tunnid": int(minutid_kokku // 60),
            "minutid": int(minutid_kokku % 60)
            }
    
# Abifunktsioon sisestuste kontrollimiseks

def kysi_numbrit(tekst, tyyp):
    # Küsib kasutajalt sisendit seni, kuni see on õiget tüüpi number.
    while True:
        try:
            return tyyp(input(tekst))
        except ValueError:
            print("Viga: See ei ole korrektne number. Palun proovi uuesti.")
            

# Põhiprogramm


nimi = input("Raamatu pealkiri: ")
# Kasutame abifunktsiooni, mis teeb tsükli ("while True"), kuni saab õige numbri
lehti = kysi_numbrit("Lehekülgede arv: ", int)
kiirus = kysi_numbrit("Lugemiskiirus (min/lk): ", float)
paevi = kysi_numbrit("Mitu päeva lugemiseks?: ", int)
    
# 1. Loome raamatu objekti
minu_raamat = Raamat(nimi, lehti, kiirus)
    
# 2. Anname raamatu planeerijale
tooriist = Planeerija(minu_raamat)
    
# 3. Arvutame
tulemus = tooriist.arvuta_plaan(paevi)
    
if tulemus:
    print(f"\nPlaan raamatule '{minu_raamat.pealkiri}':")
    print(f"- Loe {tulemus['lehti']} lehekülge päevas")
    print(f"- See võtab {tulemus['tunnid']}h {tulemus['minutid']}min päevas")
else:
    print("Viga: Sisestatud andmed ei päde")
        
            
