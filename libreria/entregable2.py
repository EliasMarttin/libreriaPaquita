#!/usr/bin/env python3
import sys
from typing import TextIO

# Folleto en inglés es Leaflet
Leaflet = tuple[int, int, int]  # (num_folleto, anchura, altura)
LeafletPos = tuple[int, int, int, int]  # (num_folleto, num_hoja_de_imprenta, pos_x ,pos_y)
listaHojas = []  # Lista con las cajitas disponibles
listaX = []


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


def process(paper_size: int, leaflet_list: list[Leaflet]) -> list[LeafletPos]:
    sorted_index = sorted(range(len(leaflet_list)), key=lambda i: leaflet_list[i][1])
    sorted_index.reverse()
    nhoja = 1
    hojay = [nhoja, 0, 0]
    listaHojas.append(hojay)
    hojax = [nhoja, 0, 0]
    listaX.append(hojax)
    listRes = []

    for index in sorted_index:
        folleto = leaflet_list[index]
        insertado = False
        ini = 0
        # hoja = (npagina, inicioHorizontal, inicioVertical)
        # folleto =  (nFolleto[0], horizontal[1], Vertical[2] )
        if len(listaHojas) > 1500:
            ini = 1000
        for i in range(ini, len(listaHojas)):

            # print("HojaY:",listaHojas[i])
            # print("HojaX:",listaX[i])
            if folleto[2] + listaHojas[i][2] <= paper_size:
                if listaHojas[i][1] == 0 and listaHojas[i][2] == 0:  # ahora se modifican de manera distinta
                    listaX[i][1] = folleto[1]
                res = (folleto[0], listaHojas[i][0], listaHojas[i][1], listaHojas[i][2])
                listRes.append(res)
                listaHojas[i][1] = 0
                listaHojas[i][2] = folleto[2] + listaHojas[i][2]
                insertado = True
                break

            elif folleto[1] + listaX[i][1] <= paper_size:
                res = (folleto[0], listaX[i][0], listaX[i][1], listaX[i][2])
                listRes.append(res)
                listaX[i][1] = folleto[1] + listaX[i][1]
                listaX[i][2] = 0
                listaHojas[i][2] = folleto[2] + listaHojas[i][2]
                listaHojas[i][1] = folleto[1] + listaX[i][1]
                insertado = True
                break

        if insertado is False:
            nhoja += 1
            res = [folleto[0], nhoja, 0, 0]
            hoja = [nhoja, 0, 0 + folleto[2]]
            listaHojas.append(hoja)
            hojaX = [nhoja, folleto[1], 0]
            listaX.append(hojaX)
            listRes.append(res)


    # print(listRes)
    return listRes


def show_results(leafletpos_list: list[int, int, int, int]):
    for folleto in leafletpos_list:
        print(folleto[0], folleto[1], folleto[2], folleto[3])
        continue


if __name__ == '__main__':
    paper_size0, leaflet_list0 = read_data(sys.stdin)
    leafletpos_list0 = process(paper_size0, leaflet_list0)
    show_results(leafletpos_list0)
