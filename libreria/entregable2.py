#!/usr/bin/env python3
import sys
from typing import TextIO

# Folleto en inglés es Leaflet
Leaflet = tuple[int, int, int]  # (num_folleto, anchura, altura)
LeafletPos = tuple[int, int, int, int]  # (num_folleto, num_hoja_de_imprenta, pos_x ,pos_y)
lista_cajitas = []  # Lista con las cajitas disponibles


# Lee la instancia por la entrada estándar (ver apartado 1.1)
# Devuelve el tamaño del papel de la imprenta y la lista de folletos
def read_data(f: TextIO) -> tuple[int, list[Leaflet]]:
    size = int(f.readline())
    l_uleaflets: list[Leaflet] = []

    for linea in f.readlines():
        leaf = linea.split(" ")
        folleto = (int(leaf[0]), int(leaf[1]), int(leaf[2]))
        l_uleaflets.append(folleto)

    return size, l_uleaflets


# Devuelve tamaño del papel y lista de folletos

# Método que dice si un folleto cabe o no dentro de un caja.
def juan_alberto(este: tuple[int, int, int], folleto: tuple[int, int, int]) -> bool:
    if (folleto[1], folleto[2]) <= (este[1], este[2]):
        return True
    return False


# Recibe el tamaño del papel de la imprenta y la lista de folletos

# metodo que pasado una cajita te añade el folleto (hace la resta) y añade las hijas.
def add_create_hijas(cajita: tuple[int, int, int], folleto: tuple[int, int, int]) -> tuple[int, int, int, int]:
    # Ahora se tiene que crear los conjuntitos
    cajitaDerecha = cajita[1] - folleto[1]
    cajitaArriba = cajita[2] - folleto[2]
    posicionA = cajita[2] - cajitaDerecha[2]
    posicionD = cajita[1] - cajitaArriba[1]
    nuevaHijaA = (cajita[1],posXhijaA, posYhijaA)
    lista_cajitas.remove(cajita)
    lista_cajitas.append(cajita_resto)
    lista_cajitas.append(cajitaDerecha)
    lista_cajitas.append(cajitaArriba)
    # hacerme la resta
    # crear las cajitas hijas
    return (1, 2, 3)


def add_create_folios(folleto, param):
    pass


def process(paper_size: int, leaflet_list: list[Leaflet]) -> list[LeafletPos]:
    print(leaflet_list)
    solucion = []
    sorted_index = sorted(range(len(leaflet_list)), key=lambda i: -(leaflet_list[i][1] * leaflet_list[i][2]))
    sorted_index.reverse()
    # Ordenamos los índices de los folletos según el tamaño es decir base * altura
    # Esta lista tiene que estar ordenada al revés para que primero se comprueben en las cajitas mas pequeñas.

    numero_hoja = 1
    cajita_inicial = (numero_hoja, paper_size, paper_size)
    lista_cajitas.append(cajita_inicial)
    # cajitas auxilires que todavía no se han creado.
    cajita2 = (2, 900, 333)
    cajita3 = (2, 333, 800)
    lista_cajitas.append(cajita2)
    lista_cajitas.append(cajita3)
    lista_cajitas.sort()
    listitas_ordenadas = sorted(range(len(lista_cajitas)), key=lambda i: lista_cajitas[i][1])

    for index in sorted_index:
        print("indice:")
        print(index)
        folleto = leaflet_list.pop(index)
        print(folleto)
        # Ahora que tengo el folleto, tengo que restar el espacio disponible y crear los conjuntos disponibles
        for este in listitas_ordenadas:
            if juan_alberto(lista_cajitas[este], folleto):  # cabe en alguna cajita
                add_create_hijas(folleto, lista_cajitas[este])
                print("cupo en ")
                print(lista_cajitas[este])
            else:
                add_create_folios(folleto, lista_cajitas[este])
                print("se ha creado cajita")
                # Actualizo el tamaño de este y creo las cajitas hijas
                #    follete = add_create_cajitas(este, folleto)  # devuelve tuple solución de ese folleto.
                # Guardamos en la lista de soluciones.
                # solucion.append(follete)

        # Creo nuevo conjunto del tamaño de una hoja.
        # numero_hoja += 1
        # nueva_cajita = (numero_hoja, paper_size, paper_size)
        # follete = add_create_cajitas(este, folleto)
        # solucion.append(follete)  # Añado en ese conjunto
        # # guardamos en la lista de soluciones.

    return solucion


# Muestra por la salida estandar las posiciones de los folletos (ver apartado 1.2)
def show_results(leafletpos_list: list[LeafletPos]):
    for folleto in leafletpos_list:
        print(folleto)


if __name__ == '__main__':
    paper_size0, leaflet_list0 = read_data(sys.stdin)
    leafletpos_list0 = process(paper_size0, leaflet_list0)
    show_results(leafletpos_list0)
