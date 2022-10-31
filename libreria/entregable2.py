#!/usr/bin/env python3
import sys
from typing import TextIO

# Folleto en inglés es Leaflet
Leaflet = tuple[int, int, int]  # (num_folleto, anchura, altura)
LeafletPos = tuple[int, int, int, int]  # (num_folleto, num_hoja_de_imprenta, pos_x ,pos_y)
lista_cajitas = []  # Lista con las cajitas disponibles
lista_posiciones = []
numero_hoja: int = 0


# Lee la instancia por la entrada estándar (ver apartado 1.1)
# Devuelve el tamaño del papel de la imprenta y la lista de folletos
def read_data(f: TextIO) -> tuple[int, list[Leaflet]]:
    size = int(f.readline())
    l_uleaflets: list[Leaflet] = []
    for linea in f.readlines():
        leaf = linea.split(" ")
        folleto = (int(leaf[0]), int(leaf[1]), int(leaf[2]))
        l_uleaflets.append(folleto)
    print("size vale: ",size)
    print("La lista vale: ", l_uleaflets)
    return size, l_uleaflets


# Devuelve tamaño del papel y lista de folletos

# Método que dice si un folleto cabe o no dentro de un caja.
def cabe(folleto: tuple[int, int, int], caja: tuple[int, int, int, int, int]) -> bool:
    if (folleto[1], folleto[2]) <= (caja[2] - caja[1], caja[4] - caja[3]):  # veo si cabe dento de la caja ese folleto.
        return True
    return False


# Recibe el tamaño del papel de la imprenta y la lista de folletos

# metodo que pasado una cajita te añade el folleto (hace la resta) y añade las hijas.
def add_create_hijas(cajita: tuple[int, int, int, int, int], folleto: tuple[int, int, int]):
    # Añado la posición donde se tiene que guardar ese folleto.
    # cajita = (nfolio[0],inicioHorizontal[1],finHorizontal[2],inicioVertical[3],finVertical[4])
    # folleto = (nfolleto[0], horizontal[1], vertical[2])
    # pos = (nfolio, inicioHorizontal, inicioVertical)
    pos = (folleto[0], cajita[0], cajita[1], cajita[3])
    lista_posiciones.append(pos)
    # Creo las nuevas cajitas
    # CA = Caja Arriba, CD = Caja derecha.
    # CA = (nfoliopadre, inicioHorizontalPadre, finHorizontalPadre - HorizontalFolleto, inicioVerticalPadre + VerticalFolleto,finVerticalPadre)
    CA = (cajita[0], cajita[1], cajita[2] - folleto[1], cajita[3] + folleto[2], cajita[4])

    # CD = (nfoliopadre, horizontalFolleto + horizontalPadre, finHorizontalPadre, inicioVerticalPadre, finVerticalPadre)
    CD = (cajita[0], folleto[1] + cajita[1], cajita[2], cajita[3], cajita[4])

    lista_cajitas.append(CA)
    lista_cajitas.append(CD)
    # lista_cajitas.remove(cajita) # Esta caja ya no existe, solo quedan los hijos por lo que


def add_create_folios(folleto, numero_hoja: int, size: int) -> int:
    numero_hoja = numero_hoja + 1
    cajitaNueva = (numero_hoja, 0, numero_hoja, size, numero_hoja)
    add_create_hijas(cajitaNueva, folleto)
    print("se tuvo que crear nuevos folios")
    return numero_hoja


def process(paper_size: int, leaflet_list: list[Leaflet]) -> list[LeafletPos]:
    sorted_index = sorted(range(len(leaflet_list)), key=lambda i: leaflet_list[i][1])
    sorted_index.reverse()
    # Ordenamos los índices de los folletos según el ancho
    numero_hoja = 1
    cajita_inicial = (numero_hoja, 0, paper_size, 0, paper_size)  # nHoja inicioAnchura finAnchura inicioAlt finalAlt
    lista_cajitas.append(cajita_inicial)




    for index in sorted_index:
        folleto = leaflet_list[index]
        # Ahora que tengo el folleto, tengo que restar el espacio disponible y crear los conjuntos disponibles

        for caja in range(len(lista_cajitas)):
            print("caja: ",lista_cajitas[caja])
            if cabe(folleto, lista_cajitas[caja]):  # cabe en alguna cajita
                add_create_hijas(lista_cajitas[caja], folleto)

            else:
                add_create_folios(folleto, numero_hoja, paper_size)
                print("se ha creado cajita")

    return lista_posiciones


# Muestra por la salida estándar las posiciones de los folletos (ver apartado 1.2)
def show_results(leafletpos_list: list[int, int, int, int]):
    print("Aqui ha llegado")
    for folleto in leafletpos_list:
        print(folleto)


if __name__ == '__main__':
    paper_size0, leaflet_list0 = read_data(sys.stdin)
    leafletpos_list0 = process(paper_size0, leaflet_list0)
    show_results(leafletpos_list0)
