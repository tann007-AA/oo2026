import tkinter as tk

class UlesandeObjekt:
    def __init__(self, master, tekst, reas_nr, haldur):
        self.tekst = tekst
        self.tehtud = False
        self.haldur = haldur  # Objekt teab, kes on tema haldur
        
        # Graafiline raam
        self.raam = tk.Frame(master, pady=5, cursor="hand2")
        self.raam.grid(row=reas_nr, column=0, sticky="w", padx=10)
        
        # Silt, millele saab klikkida
        self.silt = tk.Label(self.raam, text=f"☐ {self.tekst}", font=("Arial", 12))
        self.silt.pack(side=tk.LEFT)
        
        # SEOSTAMINE: Kui raamile või sildile klikitakse, käivitub meetod
        self.raam.bind("<Button-1>", lambda e: self.marki_tehtuks())
        self.silt.bind("<Button-1>", lambda e: self.marki_tehtuks())

    def marki_tehtuks(self, valine_kutse=False):
        """Muudab olekut. 'valine_kutse' näitab, kas käsk tuli haldurilt või klikist."""
        self.tehtud = not self.tehtud
        uue_tekst = f"☑ {self.tekst}" if self.tehtud else f"☐ {self.tekst}"
        uue_varv = "gray" if self.tehtud else "black"
        self.silt.config(text=uue_tekst, fg=uue_varv)
        
        if not valine_kutse:
            print(f"Objekt '{self.tekst}' muudeti kasutaja poolt.")

class NimekirjaHaldur:
    def __init__(self, aken):
        self.aken = aken
        self.ulesanded = []
        self.aktiivne_indeks = 0
        
        self.pealkiri = tk.Label(aken, text="Minu Ülesanded", font=("Arial", 14, "bold"))
        self.pealkiri.grid(row=0, column=0, pady=10)

    def lisa_uus_ulesanne(self, tekst):
        # Anname objektile kaasa viite haldurile (self)
        reas = len(self.ulesanded) + 1
        uus_obj = UlesandeObjekt(self.aken, tekst, reas, self)
        self.ulesanded.append(uus_obj)

    def muuda_jargmist(self):
        """Halduri funktsioon kordamööda tegelemiseks."""
        if self.ulesanded:
            # Kutsume välja meetodi märkmega, et see on 'väline' (halduri) kutse
            self.ulesanded[self.aktiivne_indeks].marki_tehtuks(valine_kutse=True)
            self.aktiivne_indeks = (self.aktiivne_indeks + 1) % len(self.ulesanded)

# Programmi käivitamine
root = tk.Tk()
root.title("Interaktiivne Haldur")
root.geometry("350x300")

haldur = NimekirjaHaldur(root)

# Lisame objektid
tood = ["Pese nõud", "Kirjuta koodi", "Söö õuna", "Loe raamatut"]
for too in tood:
    haldur.lisa_uus_ulesanne(too)

# Halduri kontrollnupp
nupp = tk.Button(root, text="Haldur: Muuda järgmist", command=haldur.muuda_jargmist, bg="#e1e1e1")
nupp.grid(row=10, column=0, pady=20, padx=10)

tk.Label(root, text="(Võid ka otse tekstile klikkida)", font=("Arial", 8), fg="gray").grid(row=11, column=0)

root.mainloop()