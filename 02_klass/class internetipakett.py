class Lugemisplaan:
    def __init__(self, raamatu_lehed, min_lehekylje_kohta, paevade_arv):
        #Konstruktor: Määratleb objekti andmeid.
        self.raamatu_lehed = raamatu_lehed
        self.min_lehekylje_kohta = min_lehekylje_kohta
        self.paevade_arv = paevade_arv
        
    def arvuta(self):
        #Meetod: Objekt arvutab oma andmete põhjal tulemuse.
        if self.paevade_arv <= 0 or self.paevade_arv > 365:
            return None
        
        lehti_paevas = self.raamatu_lehed / self.paevade_arv
        minutid_kokku = lehti_paevas * self.min_lehekylje_kohta
        
        return {
            "lehti": round(lehti_paevas, 1),
            "tunnid": int(minutid_kokku // 60),
            "minutid": int(minutid_kokku % 60),
        }
    
    
    #Kasutajaliides (sama try-except loogikaga)
try:
    l = int(input("Raamatu lehekülhede arv: "))
    k = float(input("Kiirus (min/lk): "))
    p = int(input("Mitme päeva jooksul?: "))
        
        
        #Loome objekti(instantsi)
    plaan = Lugemisplaan(l, k, p)
        
        #Käsime objektil arvutada
    tulemus = plaan.arvuta()
        
    if tulemus:
        print(f"\nLugemisplaan:")
        print(f"- Pead lugema {tulemus['lehti']} lk/päevas.")
        print(f"- See võtab {tulemus['tunnid']}h {tulemus['minutid']}min päevas")
    else:
        print("Viga. Sisestatud andmed ei päde")
            
except ValueError:
    print("Viga. Palun sisesta ainult numbrid.")
        
        
