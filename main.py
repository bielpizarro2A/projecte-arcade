import jocs

def main():
    while True:

        print("\n--- BENVINGUT/DA AL MINI ARCADE ---")
        print("1. Jugar a Pedra, Paper, Tisora")
        print("2. Jugar a Endevinar el Número")
        print("S. Sortir")
       
        opcio = input("Tria una opció: ").strip().upper()
       
        if opcio == "1":
            print("\nIniciant Pedra, Paper, Tisora...")
            jocs.janken()
           
        elif opcio == "2":
            print("\nIniciant Endevinar el Número...")
            jocs.nana()
           
        elif opcio == "S":
            print("\nGràcies per jugar al Mini Arcade! Fins aviat!")
            break
           
        else:
            print("\n[ERROR] Opció no vàlida. Si us plau, tria 1, 2 o S.")

if __name__ == "__main__":
    main()