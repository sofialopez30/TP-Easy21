############################# NO TOCAR ESTE CÓDIGO ############################
from random import randint

def sacar_carta():
    '''
    Esta función toma una carta de un mazo de forma aleatoria. La carta está numerada del 1 al 10 (inclusive).

    params:
        Esta función no tiene parámetros de entrada.
    out:
        carta: int. El número de la carta sacada.
    '''
    carta = randint(1,10)
    return carta


######################## EJEMPLO DE USO DE SACAR_CARTA ########################
#c = sacar_carta()
#print(c)
#En la consola se vería:    8

########################### AQUÍ COMIENZA TU CÓDGIO ###########################

jugar = input("¿Quiere jugar a Easy21? ")

while jugar == "Si" or jugar == "si":

    print("Bienvenid@ a la mesa de Easy 21")
    print("Empieza la partida")

    cartasacada = [sacar_carta()]

    print(f'El groupier saca un {cartasacada[0]}')
    print(f'Por el momento sacó las cartas {cartasacada}')

    dinero = 500 
    print(f'Su dinero es ${dinero}')

    apuesta = input("¿Quieres apostar?: ")

    if apuesta == "Si" or apuesta == "si":
        apostar = int(input("¿Cuánto desea apostar?: "))
        if apostar >500:
            print("No tiene el dinero suficiente")
        else: 
            print("Su apuesta ha sido aceptada")
            print(f'Ha apostado ${apostar}')
    elif apuesta == "No" or apuesta == "no":
            print ("Usted no ha apostado")
    else: 
        print("Ingrese un valor válido")

############### TURNO DEL JUGADOR #################

    carta_jugador = [sacar_carta()]
    print(f'Usted saca {carta_jugador[0]}')
    print(f'Por el momento sacó las cartas: {carta_jugador}')
    print("¿Desea sacar otra carta?")
    turnojugador = input()

    while turnojugador == "Si" or turnojugador == "si" and sum(carta_jugador) <= 21:
        carta_jugador += [sacar_carta()]
        print(f"Saco un {carta_jugador[-1]}, su total es {sum(carta_jugador)}")
        print(f"Por el momento sacó las cartas {carta_jugador}")
        if sum(carta_jugador) > 21:
            print("La suma de sus cartas superó 21, el croupier gana")
            if apuesta == "Si" or apuesta == "si":
                dinero = dinero - apostar 
                print(f"Ha perdido su dinero apostado, le quedan $ {dinero}")
        else: 
            print("¿Desea sacar otra carta?")
            otra_carta = input()