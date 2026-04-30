from kalkulaator import Calculator

def main():
    calc = Calculator()
    print("--- Minu Pythoni Kalkulaator ---")
    print("Kasutamine: Sisesta number, siis märk (+, -, *, /), siis number ja lõpuks '='")
    print("Väljumiseks trüki 'q'\n")

    while True:
        print(f"Ekraan: [{calc.display}]")
        choice = input("Vajuta nuppu: ").strip().lower()

        if choice == 'q':
            break
        elif choice in ('+', '-', '*', '/'):
            calc.press_operator(choice)
        elif choice == '=':
            calc.press_equal()
        elif choice.isdigit():
            calc.press_number(choice)
        else:
            print("Tundmatu nupp! Kasuta numbreid, märke või '='.")

if __name__ == "__main__":
    main()