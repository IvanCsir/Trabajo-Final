from ServicePartidas import ServicesPartidas
from AhorcadoService import AhorcadoService


class Ahorcado():
    def un_jugador(self):
        nombre = input("Ingrese su nombre: ")
        print("Nombre del jugador: ", nombre)

        dificultad = int(input("Ingrese la dificultad del 1 al 10: "))
        print("La dificultad es: ", dificultad)

        partida = ServicesPartidas().iniciar_partida(
                                                    nombre, dificultad, "", ""
                                                    )
        termino = False
        while not termino:
            print("El tipo de palabra es", partida.tipo_palabra)

            print("Siguiente letra:", partida.palabra_aciertos)

            letra = input("Ingrese una letra: ")
            if(letra == "salir"):
                print("Gracias por jugar!")
                return True
            result = ServicesPartidas().intentar_letra(partida, letra.upper())
            if(result != "Continua"):
                if(result == "Gano"):
                    print("\n\n\n Has ganado!! \n\n\n")
                else:
                    print(
                        "\n\n\n Se acabaron los intentos, la palabra era ",
                        partida.palabra, "\n\n\n"
                    )
                termino = True

        AhorcadoService().guardar_partida(partida, partida.nombre_jugador)
        return True

    def dos_jugadores(self):
        nombre = input("Ingrese el nombre del jugador 1: ")
        print("Nombre Jugador 1", nombre)

        dificultad = int(input("Ingrese la dificultad del 1 al 10: "))
        print("Dificultad elegida", dificultad)

        palabra = input("Ingrese la palabra para el jugador 2: ")

        tipo_palabra = input("Ingrese el tipo de palabra: ")

        partida = ServicesPartidas().iniciar_partida(
            nombre, dificultad, palabra, tipo_palabra)
        termino = False
        while not termino:
            print("El tipo de palabra es ", tipo_palabra)
            print("Sigueinte letra: ", partida.palabra_aciertos)
            letra = input("Ingrese una letra: ")
            if(letra == "salir"):
                print("Gracias por jugar!")
                return True
            result = ServicesPartidas().intentar_letra(partida, letra.upper())
            if(result != "Continua"):
                if(result == "Gano"):
                    print("\n\n\n Has acertado, Ganaste! \n\n\n")
                else:
                    print(
                        "\n\n\n Se acabaron los intentos, la palabra era: ",
                        palabra, "\n\n\n")
                termino = True
        AhorcadoService().guardar_partida(partida, partida.nombre_jugador)
        nombre = input("Jugador 2 ingrese su nombre: ")
        print("Nombre Jugador 2: ", nombre)

        dificultad = int(input("Ingrese la dificultad del 1 al 10: "))
        print("La dificultad es: ", dificultad)

        palabra = input("Ingrese la palabra para el jugador 1: ")
        tipo_palabra = input("Ingrese el tipo de palabra: ")
        partida = ServicesPartidas().iniciar_partida(
            nombre, dificultad, palabra, tipo_palabra)
        termino = False
        while not termino:
            print("El tipo de palabra es ", tipo_palabra)
            print("Siguiente letra:", partida.palabra_aciertos)
            letra = input("Ingrese una letra: ")
            if(letra == "salir"):
                print("Gracias por jugar!")
                return True
            result = ServicesPartidas().intentar_letra(partida, letra.upper())
            if(result != "Continua"):
                if(result == "Gano"):
                    print("\n\n\n Has acertado, Ganaste!\n\n\n")
                else:
                    print(
                        "\n\n\n Se acabaron los intentos, la palabra era ",
                        palabra, "\n\n\n"
                    )
                termino = True
        AhorcadoService().guardar_partida(partida, partida.nombre_jugador)
        return True
