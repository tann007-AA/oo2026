import tkinter as tk
from tkinter import messagebox

# ==========================================
# 1. SPETSIIFILINE FUNKTSIOON (Matemaatika)
# ==========================================
def arvuta_lugemisplaan(lehti, min_lehel, paevi):
    """
    Teeb puhta matemaatilise arvutuse ja teisendab minutid tundideks.
    """
    # Kogu aeg minutites
    kogu_minutid = lehti * min_lehel
    
    # Kogu aja teisendus tundideks ja minutiteks
    kogu_h = int(kogu_minutid // 60)
    kogu_min = int(kogu_minutid % 60)
    
    # Päevane koormus
    if paevi > 0:
        lehti_paevas = round(lehti / paevi, 1)
        min_paevas_kokku = kogu_minutid / paevi
    else:
        lehti_paevas = lehti
        min_paevas_kokku = kogu_minutid
        
    # Päevase aja teisendus tundideks ja minutiteks
    paeva_h = int(min_paevas_kokku // 60)
    paeva_min = int(min_paevas_kokku % 60)
    
    return {
        "kogu_h": kogu_h,
        "kogu_min": kogu_min,
        "lehti_paevas": lehti_paevas,
        "paeva_h": paeva_h,
        "paeva_min": paeva_min
    }

# ==========================================
# 2. HALDUSKLASS (Kasutajaliides ja kontroll)
# ==========================================
class LugemisKalkulaator:
    def __init__(self, aken):
        self.aken = aken
        self.aken.title("Nutikas Lugemisplaan")
        self.aken.geometry("400x450")
        self.aken.configure(bg="#f0f0f0")
        
        self.loo_liides()

    def loo_liides(self):
        # Pealkiri
        tk.Label(self.aken, text="RAAMATU LUGEMISE PLANEERIJA", 
                 font=("Arial", 12, "bold"), bg="#f0f0f0", pady=15).pack()

        # Sisendite raam parema paigutuse jaoks
        raam = tk.Frame(self.aken, bg="#f0f0f0")
        raam.pack(padx=20, pady=5)

        # Lehekülgede arv
        tk.Label(raam, text="Lehekülgede arv raamatus:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
        self.ent_lehed = tk.Entry(raam, width=10)
        self.ent_lehed.grid(row=0, column=1, padx=10)

        # Minutid leheküljele
        tk.Label(raam, text="Minutid ühe lehe kohta:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
        self.ent_minutid = tk.Entry(raam, width=10)
        self.ent_minutid.grid(row=1, column=1, padx=10)

        # Päevade arv
        tk.Label(raam, text="Mitu päevaga soovid lõpetada?", bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
        self.ent_paevad = tk.Entry(raam, width=10)
        self.ent_paevad.grid(row=2, column=1, padx=10)

        # Arvutamise nupp
        self.btn_arvuta = tk.Button(self.aken, text="ARVUTA GRAAFIK", font=("Arial", 10, "bold"),
                                    bg="#4CAF50", fg="white", padx=20, pady=10,
                                    command=self.protsessi_andmed)
        self.btn_arvuta.pack(pady=20)

        # Tulemuste paneel
        self.tulemus_raam = tk.LabelFrame(self.aken, text=" Sinu lugemisplaan ", bg="white", padx=15, pady=15)
        self.tulemus_raam.pack(padx=20, fill="both")

        self.lbl_tulemus = tk.Label(self.tulemus_raam, text="Sisesta andmed ja vajuta nuppu", 
                                    bg="white", justify="left", font=("Arial", 10))
        self.lbl_tulemus.pack()

    def protsessi_andmed(self):
        """Kogub andmed, kutsub välja funktsiooni ja uuendab ekraani."""
        try:
            lehed = int(self.ent_lehed.get())
            aeg_lehel = float(self.ent_minutid.get())
            paevad = int(self.ent_paevad.get())

            if paevad <= 0:
                raise ValueError("Päevade arv peab olema suurem kui 0")

            # Arvutus läbi spetsiifilise funktsiooni
            t = arvuta_lugemisplaan(lehed, aeg_lehel, paevad)

            # Vormistame tulemuse inimlikult loetavaks
            vastus = (
                f"KOGU AEG: {t['kogu_h']} tundi ja {t['kogu_min']} minutit\n"
                f"----------------------------------------\n"
                f"ET JÕUDA VALMIS {paevad} PÄEVAGA:\n\n"
                f"• Loe päevas: {t['lehti_paevas']} lehekülge\n"
                f"• Ajukulu päevas: {t['paeva_h']} tundi ja {t['paeva_min']} minutit"
            )
            
            self.lbl_tulemus.config(text=vastus, fg="#333", font=("Arial", 10, "bold"))

        except ValueError as e:
            messagebox.showerror("Viga sisestuses", "Palun sisesta korrektne arv!\n(Näiteks: 300, 5, 7)")

# ==========================================
# 3. KÄIVITAMINE
# ==========================================
if __name__ == "__main__":
    root = tk.Tk()
    # Käivitame haldusklassi
    rakendus = LugemisKalkulaator(root)
    root.mainloop()