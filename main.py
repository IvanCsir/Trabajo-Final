from Ahorcado import Ahorcado
from AhorcadoService import AhorcadoService


class Menu():
    def seleccion_jugadores(self):
        print("El juego ha comenzado: ")
        print("1) 1 jugador")
        print("2) 2 jugadores")
        print("3) Ver resultados")
        print("4) Salir")
        return int(input("Seleccione una opcion: "))


if __name__ == "__main__":

    while True:
        cant_jugadores = Menu().seleccion_jugadores()
        if cant_jugadores == 1:
            result = Ahorcado().un_jugador()
        elif cant_jugadores == 2:
            result = Ahorcado().dos_jugadores()
        elif cant_jugadores == 3:
            AhorcadoService().ver_partida_guardada()
        elif cant_jugadores == 4:
            break
