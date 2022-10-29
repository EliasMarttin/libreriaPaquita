#!/usr/bin/env python3
import sys
from typing import TextIO

# Folleto en inglés es Leaflet
Leaflet = tuple[int, int, int]  # (num_folleto, anchura, altura)
LeafletPos = tuple[int, int, int, int]  # (num_folleto, num_hoja_de_imprenta, pos_x ,pos_y)


# Lee la instancia por la entrada estándar (ver apartado 1.1)
# Devuelve el tamaño del papel de la imprenta y la lista de folletos
def read_data(f: TextIO) -> tuple[int, list[Leaflet]]:
    # size = int(f.readline())
    l_uleaflets = [Leaflet(linea) for linea in f.readlines()]
    size = 0
    print(l_uleaflets)
    return size, l_uleaflets


# Devuelve tamaño del papel y lista de folletos

# Método que dice si un folleto cabe o no dentro de un caja.
def juan_alberto(este: tuple(int, int, int), folleto: tuple(int, int, int)) -> bool:
    if (folleto[2], folleto[3]) <= (este[2], este[3]):
        return True
    return False


# Recibe el tamaño del papel de la imprenta y la lista de folletos

# metodo que pasado una cajita te añade el folleto (hace la resta) y añade las hijas.
def add_create_cajitas(cajita: tuple(int, int, int), folleto: tuple(int, int, int)) -> tuple(int, int, int, int):
    # Ahora se tiene que crear los conjuntitos
    # hacerme la resta
    # crear las cajitas hijas
    posX = 0
    posY = 0
    # devolver la solucion de ese  folleto.
    return (folleto[1], cajita[1], posX, posY)


def process(paper_size: int, leaflet_list: list[Leaflet]) -> list[LeafletPos]:
    solucion = []
    sorted_index = sorted(range(len(leaflet_list)),
                          key=lambda tuple: (tuple[2] * tuple[
                              3]))  # esto no sé si me lo ordena de mayor a menor o de menor a mayor

    # Vamos a dar por hecho que hasta ahora en sortedIndex pues tenemos los índices ordenados por tamaño de folleto.
    # Esta lista tiene que estar ordenada al revés para que primero se comprueben en las cajitas mas pequeñas.
    lista_cajitas = []
    numero_hoja = 1
    cajita_inicial = (numero_hoja, paper_size, paper_size)
    lista_cajitas.append(cajita_inicial)

    for index in sorted_index:
        folleto = leaflet_list.pop(index)
        # Ahora que tengo el folleto, tengo que restar el espacio disponible y crear los conjuntos disponibles
        for este in lista_cajitas:
            if juan_alberto(este, folleto):  # cabe en alguna cajita
                # Actualizo el tamaño de este y creo las cajitas hijas
                follete = add_create_cajitas(este, folleto)  # devuelve tuple solución de ese folleto.
                # guardamos en la lista de soluciones.
                solucion.append(follete)

        # Creo nuevo conjunto del tamaño de una hoja.
        numero_hoja += 1
        nueva_cajita = (numero_hoja, paper_size, paper_size)
        follete = add_create_cajitas(este, folleto)
        solucion.append(follete)  # Añado en ese conjunto
        # guardamos en la lista de soluciones.

    return solucion


# Muestra por la salida estandar las posiciones de los folletos (ver apartado 1.2)
def show_results(leafletpos_list: list[LeafletPos]):
    for folleto in leafletpos_list:
        print(folleto)


if __name__ == '__main__':
    paper_size0, leaflet_list0 = read_data(sys.stdin)
    leafletpos_list0 = process(paper_size0, leaflet_list0)
    show_results(leafletpos_list0)
