class internetipakett:
    def __init__(self, nimi, alla, ules, hind):
        self.nimi = nimi
        self.alla = alla
        self.ules = ules
        self.hind = hind
    
        # Eeldus: inimese kohta kulub 25Mbps
        self.varu_kasutaja_kohta = 25
    
    def kas_sobib_perele(self, inimeste_arv):
        vajaminev_kiirus = inimeste_arv * self.varu_kasutaja_kohta
        # Arvutame jäägi kohe alguses ära
        jaak = self.alla - vajaminev_kiirus
        
        print(f"ANALÜÜS {inimeste_arv} kasutaja puhul:")
        
        if jaak > 0:
            print(f"[OK] pakett '{self.nimi}' sobib. Varu jääb veel {jaak} Mbps")
            
        elif jaak == 0:
            print(f"[ENAM-VÄHEM] pakett '{self.nimi}' võib sobida, aga tõenäoliselt muutub see tüütuks :)")
            
        else:
            puudu = abs(jaak)
            print(f"[HOIATUS] pakett '{self.nimi}' jääb aeglaseks. Puudu jääb u {puudu} Mbps")
            
        print("-" * 40)
        
#Eksemplarid
pakett_mini = internetipakett("Väike kodu", 50, 30, 15)
pakett_keskmine = internetipakett("Keskmine kodu", 100, 60, 40)
pakett_max = internetipakett("Suur kodu", 300, 100, 60)

pakett_mini.kas_sobib_perele(4)
pakett_keskmine.kas_sobib_perele(4)
pakett_max.kas_sobib_perele(4)
            