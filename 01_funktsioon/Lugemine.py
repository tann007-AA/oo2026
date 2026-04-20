def arvuta_lugemisplaan(raamatu_lehed, min_lehekylje_kohta, paevade_arv):
    # Veakontroll: kas päevade arv on loogiline?
    if paevade_arv <= 0:
        return "Viga: Päevade arv peab olema suurem kui 0."
    if paevade_arv > 365:
        return "Viga: 365 päeva on raamatu lugemiseks liiga pikk aeg. Palun vali realistlikum tähtaeg."
    
    # Arvutame lehekülgede arvu päevas
    lehti_paevas = raamatu_lehed / paevade_arv
    
    # Arvutame kogu vajaliku aja minutites
    kokku_minutid = lehti_paevas * min_lehekylje_kohta
    
    # Teisendame minutid tundideks ja minutiteks
    tunnid = int(kokku_minutid // 60)
    minutid = int(kokku_minutid % 60)
    
    return lehti_paevas, tunnid, minutid

# --- Kasutajaliides ---
try:
    kokku_lehti = int(input("Sisesta raamatu lehekülgede arv: "))
    minutit_lehe_kohta = float(input("Sinu lugemiskiirus (mitu minutit 1 leht?): "))
    aega_paevades = int(input("Mitme päevaga soovid raamatu loetud saada?: "))

    # Kutsume funktsiooni
    tulemus = arvuta_lugemisplaan(kokku_lehti, minutit_lehe_kohta, aega_paevades)

    # Kontrollime, kas funktsioon tagastas veateate (teksti) või tulemused (tuple)
    if isinstance(tulemus, str):
        print(tulemus)
    else:
        lehti, tunnid, minutid = tulemus
        print(f"\nLugemisplaan:")
        print(f"- Pead lugema {round(lehti, 1)} lehekülge päevas.")
        print(f"- See võtab sul aega {tunnid}h ja {minutid}min päevas.")

except ValueError:
    print("Viga: Palun sisesta ainult numbreid.")
