import robot

def janken():
    bot = robot.robot()
   
    punts_jugador = 0
    punts_robot = 0
    ronda_actual = 1
   
    print("\n--- PEDRA, PAPER, TISORA ---")
    print("Tria la modalitat de joc:")
    print("1. El primer que arribi a 3 victòries")
    print("2. Jugar un total de 5 rondes")
   
    mode = ""
    while mode not in ["1", "2"]:
        mode = input("Selecciona modalitat (1 o 2): ").strip()
        if mode not in ["1", "2"]:
            print("Opció incorrecta. Introdueix 1 o 2.")

    partida_en_curs = True
    while partida_en_curs:
        print(f"\n--- Ronda {ronda_actual} ---")
        print(f"Marcador actual -> Tu: {punts_jugador} | Robot: {punts_robot}")
       
        jugada_usuari = input("Tria (pedra, paper, tisora): ").strip().lower()
        while jugada_usuari not in ["pedra", "paper", "tisora"]:
            print("Jugada invàlida! Has d'escriure: pedra, paper o tisora.")
            jugada_usuari = input("Tria (pedra, paper, tisora): ").strip().lower()
           
        jugada_bot = bot.playing()
        print(f"El robot ha tret: {jugada_bot}")
       
        if jugada_usuari == jugada_bot:
            print("-> Empat en aquesta ronda!")
           
        elif (jugada_usuari == "pedra" and jugada_bot == "tisora") or \
             (jugada_usuari == "paper" and jugada_bot == "pedra") or \
             (jugada_usuari == "tisora" and jugada_bot == "paper"):
            print("-> Has guanyat aquesta ronda!")
            punts_jugador += 1
           
        else:
            print("-> El robot guanya aquesta ronda!")
            punts_robot += 1
           
        ronda_actual += 1

        if mode == "1":
            if punts_jugador == 3 or punts_robot == 3:
                partida_en_curs = False
               
        elif mode == "2":
            if ronda_actual > 5:
                partida_en_curs = False

    print("\n===============================")
    print(f"RESULTAT FINAL: Tu {punts_jugador} - {punts_robot} Robot")
    if punts_jugador > punts_robot:
        print("Felicitats! Has guanyat la partida!")
    elif punts_robot > punts_jugador:
        print("El robot guanya la partida...")
    else:
        print("La partida ha acabat en empat!")
    print("===============================\n")



# Joc d'endevinar el número

import random  

def nana():
    numero_secret = random.randint(1, 100)
    intents = 0
    endevinat = False
   
    print("\n--- ENDEVINA EL NÚMERO ---")
    print("He pensat un número entre 1 i 100. Pots endevinar quin és?")
   
    while not endevinat:
        entrada = input("\nIntrodueix el teu número: ").strip()
       
        try:
            intent_usuari = int(entrada)
        except ValueError:
            print("[AVÍS] Has d'introduir un número enter vàlid!")
            continue 
           
        intents += 1
       
        if intent_usuari < numero_secret:
            print("Massa baix! El número secret és més gran.")
        elif intent_usuari > numero_secret:
            print("Massa alt! El número secret és més petit.")
        else:
            endevinat = True
            print("\nFelicitats! Has endevinat el número!")
            print(f"Número secret: {numero_secret}")
            print(f"Has necessitat un total de {intents} intents.")

    print("------------------------------------------\n")