import random

titulo = "¡Bienvenido al casino online!"
linea = "*" * (len(titulo) + 8)

print(linea)
print("*" + " " * (len(titulo) + 6) + "*")
print("*" + " " * 3 + titulo + " " * 3 + "*")
print("*" + " " * (len(titulo) + 6) + "*")
print(linea)

base_de_datos = {}

def registrar_usuario():
    usuario = input(f"\nIngresa un nombre de usuario: ")
    if usuario not in base_de_datos:
        contrasena = input("Ingresa una contraseña: ")
        saldo = 0  
        base_de_datos[usuario] = {"contrasena": contrasena, "saldo": saldo}
        print(f"\nRegistro exitoso.")
    else:
        print("El usuario ya existe. Por favor, elige otro nombre de usuario.")

def iniciar_sesion():
    usuario = input("Ingresa tu nombre de usuario: ")
    contrasena = input("Ingresa tu contraseña: ")
    if usuario in base_de_datos and base_de_datos[usuario]["contrasena"] == contrasena:
        print(f"\nInicio de sesión exitoso. ¡Bienvenido,", usuario, "!")
        menu_juegos(usuario) 
    else:
        print("Nombre de usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")

def menu_juegos(usuario):
    while True:
        print(f"\n1. Ver saldo")
        print("2. Agregar saldo")
        print("3. Jugar Ruleta")
        print("4. Jugar Mayor/Menor")
        print("5. Jugar Yeti")
        print("6. Jugar Blackjack")
        print("7. Salir")

        opcion = input(f"\nSelecciona una opción: ")

        if opcion == "1":
            print("Saldo actual:", base_de_datos[usuario]["saldo"])
        elif opcion == "2":
            agregar_saldo(usuario)
        elif opcion == "3":
            base_de_datos[usuario]["saldo"] = jugar_ruleta(base_de_datos[usuario]["saldo"])
        elif opcion == "4":
            base_de_datos[usuario]["saldo"] = jugar_mayor_menor(base_de_datos[usuario]["saldo"])
        elif opcion == "5":
            base_de_datos[usuario]["saldo"] = yeti(base_de_datos[usuario]["saldo"])
        elif opcion == "6":
            base_de_datos[usuario]["saldo"] = jugar_blackjack(base_de_datos[usuario]["saldo"])
        elif opcion == "7":
            print(f"\n¡Muchas Gracias por jugar, hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

def agregar_saldo(usuario):
    try:
        cantidad = float(input("Ingresa la cantidad de saldo a agregar: "))
        if cantidad > 0:
            base_de_datos[usuario]["saldo"] += cantidad
            print("Saldo agregado exitosamente.")
        else:
            print("La cantidad debe ser mayor que cero.")
    except ValueError:
        print("Entrada no válida. Ingresa un número válido.")

def jugar_ruleta(saldo):
    
    print("")
    print("-"*29)
    print("|  Bienvenido a la ruleta!  |")
    print("-"*29)
    print("")
    
    
    dejarDeApostar = False
    matrizCasino = []
    n = 3
    numerosParticularesLista = []
    imparparLista = []
    docenasLista = []

    for f in range(3):
        matrizCasino.append([])
        if f == 1:
            n = 2
        if f == 2:
            n = 1
        for c in range(12):
            matrizCasino[f].append(n)
            n = n + 3

    for f in range(3):
        print()
        for c in range(12):
            print("%5d" % matrizCasino[f][c], end="")
        print()

    print("   " + "_" * 18 + "  " + "_" * 18 + "  " + "_" * 18)
    print()
    print("      1era Docena" + "          2da Docena" + "          3era Docena")
    print("\nLa ruleta funciona de la siguiente manera:")
    print("\n1- Se puede apostar a un numero en particular, paga x36.")
    print("2- Se puede apostar numero par o impar, paga x2")
    print("3- Se puede apostar por docenas, primera, segunda, tercera. Paga x2")
    print("4- La jugada mínima debe ser de $50")
    print(f"\nSu saldo es: {saldo}")

    if saldo >= 50:
        apuesta = int(input("\nIngrese la cantidad que desea apostar: "))
        while apuesta > saldo or apuesta < 50:
            apuesta = int(input("Error, cantidad no válida ingresada, por favor, vuelva a intentar: "))

        while dejarDeApostar == False:
            print("\n1- Numero particular.")
            print("2- Impar/Par.")
            print("3- Docenas.")
            print("4- Dejar de apostar.")

            jugada = int(input("\nIngrese donde desea realizar la apuesta: "))
            dejarDeApostar = True

            if jugada == 1:
                numeros = input("Ingrese los números a los que desea apostar (separados por espacios): ")
                for num in map(int, numeros.split()):
                    while num < 1 or num > 36:
                        print(f"Número {num} no válido. Debe estar entre 1 y 36.")
                        num = int(input("Ingrese a qué número desea apostar: "))

                    numerosParticularesLista.append(num)

                apuesta_por_numero = apuesta / len(numerosParticularesLista)
                saldo = saldo - apuesta
            elif jugada == 2:
                imparpar = input("Ingrese la palabra par o impar:")
                imparparCorreccion = imparpar.capitalize()
                while imparparCorreccion != "Par" and imparparCorreccion != "Impar":
                    imparpar = input("Ingrese la palabra par o impar:")
                    imparparCorreccion = imparpar.capitalize()
                imparparLista.append(imparparCorreccion)
                apuesta_por_imparpar = apuesta / len(imparparLista)
                saldo = saldo - apuesta
            elif jugada == 3:
                docenas = int(input("Ingrese el numero de la docena que desea apostar (1, 2 o 3): "))
                while docenas < 1 or docenas > 3:
                    docenas = int(input("Ingrese el numero de la docena que desea apostar (1, 2 o 3): "))
                docenasLista.append(docenas)
                apuesta_por_docena = apuesta / len(docenasLista)
                saldo = saldo - apuesta
            elif jugada == 4:
                dejarDeApostar = True
            
            seguirApostando = 0
            if saldo > 50:
                seguirApostando = int(input("Para seguir apostando ingrese 1, en caso contrario ingrese 0: "))
            
            if seguirApostando == 1:
                dejarDeApostar = False
                apuesta = int(input("\nIngrese la cantidad que desea apostar: "))
                while apuesta > saldo or apuesta < 50:
                    apuesta = int(input("Error, cantidad no válida ingresada, por favor, vuelva a intentar: "))
            else:
                dejarDeApostar = True

    else:
        print("No es posible jugar a la ruleta, saldo insuficiente.")

    premioAcumulado = 0
    ruletaResultado = random.randint(1, 36)

    if imparparLista != []:
        if ruletaResultado % 2 == 0:
            if "Par" in imparparLista:
                premioAcumulado = premioAcumulado + (apuesta_por_imparpar * 2)
        if ruletaResultado % 2 != 0:
            if "Impar" in imparparLista:
                premioAcumulado = premioAcumulado + (apuesta_por_imparpar * 2)

    if ruletaResultado in numerosParticularesLista:
        premioAcumulado = premioAcumulado + (apuesta_por_numero * 36)

    if docenasLista != []:
        if ruletaResultado < 13 and 1 in docenasLista:
            premioAcumulado = premioAcumulado + (apuesta_por_docena * 2)
        if 12 < ruletaResultado < 25 and 2 in docenasLista:
            premioAcumulado = premioAcumulado + (apuesta_por_docena * 2)
        if ruletaResultado > 25 and 3 in docenasLista:
            premioAcumulado = premioAcumulado + (apuesta_por_docena * 2)

    saldo = premioAcumulado + saldo
    
    print("")
    print("-"*29)
    print("")
    print(f"El número que salió fue el: {ruletaResultado}")
    print("")
    print("-"*29)
    print("")
    print(f"\nSu saldo final es de: {saldo}")

    return saldo

def jugar_mayor_menor(saldo):
    print("")
    print("-"*31)
    print("|  Bienvenido a Mayor/Menor!  |")
    print("-"*31)
    print("")
    
    if saldo < 50:
        print("Saldo insuficiente para jugar (Mínimo 50).")
        return saldo
    else:
        dejarDeJugar = False
        while not dejarDeJugar:
            while True:
                try:
                    apuesta = int(input("Ingrese la cantidad que desea apostar: "))
                    probarSaldoSuf = saldo - apuesta
                    while apuesta < 50:
                        apuesta = int(input("La apuesta mínima es de 50: "))
                    while probarSaldoSuf < 0:
                        probarSaldoSuf = saldo + apuesta
                        apuesta = int(input("Saldo insuficiente: "))
                    saldo = saldo - apuesta
                    break
                except ValueError:
                    print("Dato no válido, por favor ingresar de nuevo.")
                except:
                    print("Error desconocido.")

            multiplicador = 1.3
            
            #Se crea el mazo
            palos = ["♣", "♠", "♦", "♥"]
            mazo = []

            while len(mazo) < 52:
                numeroCarta = random.randint(1, 13)
                if numeroCarta == 11:
                    numeroCarta = "J"
                elif numeroCarta == 12:
                    numeroCarta = "Q"
                elif numeroCarta == 13:
                    numeroCarta = "K"
                elif numeroCarta == 1:
                    numeroCarta = "A"
                carta = (numeroCarta, palos[random.randint(0, 3)])
                if carta not in mazo:
                    mazo.append(carta)
                    
            elegirCarta = random.randint(0, 51)
            cc = mazo[elegirCarta]



            print(" _______")
            print("|       |")
            print(f"|   {cc[0]}   |")
            print("|       |")
            print(f"|   {cc[1]}   |")
            print("|       |")
            print(" -------")

            cartaAnterior = cc[0]
            if cartaAnterior == "J":
                cartaAnterior = 11
            elif cartaAnterior == "Q":
                cartaAnterior = 12
            elif cartaAnterior == "K":
                cartaAnterior = 13
            elif cartaAnterior == "A":
                cartaAnterior = 1

            elegirCarta = random.randint(0, 51)
            cc = mazo[elegirCarta]

            jugada = input("Ingrese si la próxima carta será mayor o menor: ")

            print(" _______")
            print("|       |")
            print(f"|   {cc[0]}   |")
            print("|       |")
            print(f"|   {cc[1]}   |")
            print("|       |")
            print(" -------")

            cartaComparar = cc[0]
            if cartaComparar == "J":
                cartaComparar = 11
            elif cartaComparar == "Q":
                cartaComparar = 12
            elif cartaComparar == "K":
                cartaComparar = 13
            elif cartaComparar == "A":
                cartaComparar = 1

            if (jugada == "mayor" and cartaAnterior < cartaComparar) or (jugada == "menor" and cartaAnterior > cartaComparar):
                print("¡Ganaste!")
                ganado = apuesta * multiplicador
                saldo += ganado
                print(f"Has ganado {ganado}. Tu nuevo saldo es {saldo}.")
            else:
                print("Perdiste 😞")
                print(f"Has perdido {apuesta}. Tu nuevo saldo es {saldo}.")
                if saldo < 50:
                    dejarDeJugar = True
            continuar = input("¿Desea seguir jugando? (s/n): ")
            if continuar.lower() != 's':
                dejarDeJugar = True

    return saldo

def yeti(saldo):
    
    print("")
    print("-"*29)
    print("|  Bienvenido al Icefield!  |")
    print("-"*29)
    print("")
    
    if saldo < 50:
        print("Saldo insuficiente para jugar.")
        return saldo 
    apuesta_inicial = int(input("Ingresa su apuesta: "))
    num_jugadas_max = 5
    casilla1_valores = []
    casilla2_valores = []
    casilla3_valores = []
    apuesta_actual = apuesta_inicial
    jugadas_realizadas = 0
    while apuesta_inicial > saldo:
        print("Saldo insuficiente")
        apuesta_inicial = int(input("Ingresa su apuesta: "))
    while jugadas_realizadas < num_jugadas_max and apuesta_actual > 0 :
        casilla_elegida = int(input(f"Elige la casilla 1,2 o 3 para la jugada {jugadas_realizadas +1}: "))
        
        casilla1 = random.randint(0,1)
        casilla2 = random.randint(0,1)
        casilla3 = random.randint(0,1)
        
        casilla1_valores.append(casilla1)
        casilla2_valores.append(casilla2)
        casilla3_valores.append(casilla3)
        
        multiplicador = 0
        
        if jugadas_realizadas == 0:
            multiplicador = 1.2
        elif jugadas_realizadas == 1:
            multiplicador = 2.4
        elif jugadas_realizadas == 2:
            multiplicador = 3.6
        elif jugadas_realizadas == 3:
            multiplicador = 4.8
        elif jugadas_realizadas == 4:
            multiplicador = 6
        
        print(f"Jugada {jugadas_realizadas +1}: {casilla1} {casilla2} {casilla3}")
        
        if apuesta_actual > 0:
            if casilla_elegida == 1 and casilla1 ==1:
                print("Ganaste! los puntos se multiplican por 1.2")
                apuesta_actual = apuesta_actual * multiplicador
            elif casilla_elegida == 2 and casilla2 == 1:
                print("Ganaste! los puntos se multiplican por 1.2")
                apuesta_actual = apuesta_actual * multiplicador
            elif casilla_elegida == 3 and casilla3 == 1:
                print("Ganaste! los puntos se multiplican por 1.2")
                apuesta_actual = apuesta_actual * multiplicador
            else:
                print("Perdiste, Segui intentando")
                apuesta_actual = 0
                saldo = saldo - apuesta_inicial
                break
            
            print(f"Tus puntos actuales: {apuesta_actual}")
            jugadas_realizadas = jugadas_realizadas + 1
            if apuesta_actual > 0:
                continuar = input("Quieres seguir jugando? Si/No: ")
                if continuar.lower() != "si":
                    break
    
    print("Resultado del juego")
    print("Mapa:")
    print(f"-"*(2 + len(casilla1_valores)))
    print(*casilla1_valores, sep=" ")
    print(*casilla2_valores, sep=" ")
    print(*casilla3_valores, sep=" ")
    print(f"-"*(2 + len(casilla1_valores)))
    
    if apuesta_actual > 0:
        ganancia = apuesta_actual - apuesta_inicial
        print(f"Ganaste: {apuesta_actual - apuesta_inicial}")
        saldo = saldo + ganancia
    print(f"Tus nuevos puntos serian: {saldo}")
    return saldo
def crear_baraja():
    """Crea una baraja de cartas."""
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baraja = [{'valor': valor, 'palo': palo} for valor in valores for palo in palos]
    random.shuffle(baraja)
    return baraja
 
def calcular_puntos(mano):
    """Calcula la puntuación de una mano de Blackjack."""
    puntos = 0
    ases = 0
 
    for carta in mano:
        if carta['valor'] in ['J', 'Q', 'K']:
            puntos += 10
        elif carta['valor'] == 'A':
            ases += 1
            puntos += 11
        else:
            puntos += int(carta['valor'])
 
    while puntos > 21 and ases:
        puntos -= 10
        ases -= 1
 
    return puntos
 
def mostrar_mano(mano, ocultar_primera_carta=False):
    """Muestra las cartas en la mano."""
    for i, carta in enumerate(mano):
        if i == 0 and ocultar_primera_carta:
            print('Carta oculta')
        else:
            print(f"{carta['valor']} de {carta['palo']}")

def jugar_blackjack(saldo):
    
    if saldo < 50:
        print("Saldo insuficiente, tiene que depositar para apostar.")
        return saldo
    print("")
    print("-"*30)
    print("|  Bienvenido al BlackJack!  |")
    print("-"*30)
    print("")
    
    apuesta = int(input("Ingrese el valor que desea apostar: "))
    while apuesta > saldo:
        apuesta = int(input("Saldo insuficiente, ingrese el valor que desea apostar: "))
    baraja = crear_baraja()
    mano_jugador = [baraja.pop(), baraja.pop()]
    mano_dealer = [baraja.pop(), baraja.pop()]
    juego_terminado = False
 
    while not juego_terminado:
        puntos_jugador = calcular_puntos(mano_jugador)
        puntos_dealer = calcular_puntos(mano_dealer)
 
        print('\n--- Jugador ---')
        mostrar_mano(mano_jugador)
        print(f"Puntos: {puntos_jugador}")
 
        print('\n--- Dealer ---')
        mostrar_mano(mano_dealer, ocultar_primera_carta=True)
 
        if puntos_jugador == 21:
            print("¡Blackjack! ¡Ganaste!")
            juego_terminado = True
        elif puntos_jugador > 21:
            print("Has perdido. ¡Te pasaste de 21!")
            juego_terminado = True
        else:
            eleccion = input("¿Quieres tomar otra carta? (s/n): ")
            if eleccion.lower() == 's':
                mano_jugador.append(baraja.pop())
            else:
                juego_terminado = True
 

    while puntos_dealer < 17:
        mano_dealer.append(baraja.pop())
        puntos_dealer = calcular_puntos(mano_dealer)
 
    print('\n--- Resultado ---')
    print('\n--- Jugador ---')
    mostrar_mano(mano_jugador)
    print(f"Puntos del Jugador: {puntos_jugador}")
 
    print('\n--- Dealer ---')
    mostrar_mano(mano_dealer)
    print(f"Puntos del Dealer: {puntos_dealer}")
 
    if puntos_dealer > 21:
        print("El dealer se pasó de 21. ¡Ganaste!")
        saldo += apuesta  
    elif puntos_jugador > puntos_dealer:
        print("¡Ganaste!")
        saldo += apuesta  
    elif puntos_jugador < puntos_dealer:
        print("Perdiste. ¡El dealer gana!")
        saldo -= apuesta  
    else:
        print("Es un empate.")

    print(f"\nTu saldo actual es: {saldo}")
    return saldo

def main():
    while True:
        print(f"\n1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input(f"\nSelecciona una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
