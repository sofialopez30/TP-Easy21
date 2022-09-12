from random import randint
from signal import siginterrupt

def sacar_carta():
    carta = randint(1,10)
    return carta


######################## EJEMPLO DE USO DE SACAR_CARTA ########################
#c = sacar_carta()
#print(c)
#En la consola se vería:    8

########################### AQUÍ COMIENZA TU CÓDGIO ###########################

print("¿Quiere jugar a Easy21?")
jugar = input()

dinero = 500 
while jugar == 'no'or jugar== "No": 
    print('Gracias igual')
    break

while jugar == "Si" or jugar == "si":

    print("Bienvenid@ a la mesa de Easy 21")
    print("Empieza la partida")

    cartasacada = [sacar_carta()]

    print(f'El groupier saca un {cartasacada[0]}')
    print(f'Por el momento el crupier sacó las cartas {cartasacada}')

    print(f'Su dinero es ${dinero}')

    apuesta = input("¿Quieres apostar?: ")
 
    if apuesta == "Si" or apuesta == "si":
        apostar = int(input("¿Cuánto desea apostar?: "))
        if apostar > dinero:
            print("No tiene el dinero suficiente")
        else: 
            print("Su apuesta ha sido aceptada")
            print(f'Ha apostado ${apostar}')
    elif apuesta == "No" or apuesta == "no":
            print ("Usted no ha apostado")

############### TURNO DEL JUGADOR #################

    carta_jugador = [sacar_carta()]
    print(f'Usted saca {carta_jugador[0]}')
    print(f'Por el momento sacó las cartas: {carta_jugador}')
    print("¿Desea sacar otra carta?")
    turnojugador = input()

    while (turnojugador == "Si" or turnojugador == "si") and sum(carta_jugador) <= 21:
        carta_jugador += [sacar_carta()]
        print(f"Saco un {carta_jugador[-1]}, su total es {sum(carta_jugador)}")
        print(f"Por el momento sacó las cartas {carta_jugador}")
        if sum(carta_jugador) > 21:
            turnojugador == "No"
        else: 
            print("¿Desea sacar otra carta?")
            turnojugador = input()
    
############## TURNO DEL GRUPIER ##############

    if sum(carta_jugador) > 21:
        print("La suma de sus cartas superó 21, el croupier gana")
        # print("¿Quiere jugar de vuelta?")
        # jugar = input()
        if apuesta == "Si" or apuesta == "si":
            dinero = dinero - apostar 
            print(f"Ha perdido su dinero apostado, le quedan $ {dinero}")
    else: 
        cartasacada += [sacar_carta()]
        print(f"El crupier saca un {cartasacada[-1]}, su total es {sum(cartasacada)}")
        print (f'Por el momento sacó las cartas: {cartasacada}')

        while sum(cartasacada) < 16: 
            print("El croupier pide otra carta")
            cartasacada += [sacar_carta()]
            print(f"El crupier saca un {cartasacada[-1]}, su total es {sum(cartasacada)}")
    
        if sum(cartasacada) > 21: 
            print("La suma de las cartas del crupier superó 21, ¡usted gana!")
            dinero = dinero + apostar
            print(f"Le quedan $ {dinero}")
        else: 
            if sum(cartasacada) >= sum(carta_jugador):
                print("La partida termina, el crupier gana")
                dinero = dinero - apostar
                print(f"Le quedan $ {dinero}")
            else:
                print("La partida termina, usted gana")
                dinero = dinero + apostar 
                print(f"Le quedan $ {dinero}")

    if dinero <= 0:
        print("Se quedó sin dinero, no puede jugar")
        jugar = "no"
    else:
        print("¿Quiere jugar de vuelta?")
        jugar = input()

    while jugar == "no" or jugar == "No":
        print("Gracias por jugar Easy21")
        break