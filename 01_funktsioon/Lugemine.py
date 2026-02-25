def arvuta_lugemisplaan():
    print("--- RAAMATU LUGEMISE KALKULAATOR ---")
    
    try:
        # 1. Kysime sisendid
        lehed = int(input("Mitu lehekülge on raamatus? "))
        min_lehel = float(input("Mitu minutit loed ühte lehte? "))
        paevad = int(input("Mitu päevaga soovid raamatu läbi saada? "))

        # 2. Arvutame koguaja
        kogu_minutid = lehed * min_lehel
        kogu_h = int(kogu_minutid // 60)
        kogu_min = int(kogu_minutid % 60)

        # 3. Arvutame päevase koormuse
        min_paevas_kokku = kogu_minutid / paevad if paevad > 0 else kogu_minutid
        paeva_h = int(min_paevas_kokku // 60)
        paeva_min = int(min_paevas_kokku % 60)
        lehti_paevas = round(lehed / paevad, 1) if paevad > 0 else lehed

        # 4. Väljastame tulemuse
        print("\n" + "="*30)
        print(f"Kogu lugemisaeg: {kogu_h} tundi ja {kogu_min} minutit.")
        print(f"Et jõuda valmis {paevad} päevaga:")
        print(f" -> Loe päevas: {lehti_paevas} lehekülge")
        print(f" -> See võtab: {paeva_h} tundi ja {paeva_min} minutit")
        print("="*30)

    except ValueError:
        print("Viga! Palun sisesta ainult numbreid.")

# Käivitame funktsiooni
arvuta_lugemisplaan()