import os
import time
import matplotlib.pyplot as plt
import networkx as nx

graph1 = {}
used_colors = {}

def clear_screen():
    os.system("cls")

def print_header(header_text):
    print(f"{header_text:^80}")

def get_vertex(graph):
    return list(graph.keys())


def validate_input():
    print()
    tanya = input('Tekan 1 untuk kembali: ')
    while tanya not in ['1', 'satu']:
        print('Input tidak valid')
        time.sleep(1)
        tanya = input('Tekan 1 untuk kembali: ')
    menu()

vertex = get_vertex(graph1)


def get_edges(graph):
    edges = []
    for v in graph:
        for e in graph[v]:
            if {v, e} not in edges:
                edges.append({v, e})
    return edges

def add_item(graph):
    clear_screen()
    print("\n")
    print_header("Menu Menambahkan Zat\n")
    print(f'{"-"*40}')
    for key in graph:
        print(f'|{" "*4}{key}{" "*4}|', end="")
        for _ in key:
            print(f' |{" "*7}{graph[key]}')
    print(f'{"-"*40}')
    banyak = input("\nIngin menginputkan berapa Zat Kimia = ")
    if banyak.isdigit():
        for i in range(int(banyak)):
            while True:
                vertex = input(f"{i+1}. Inputkan Zat Kimia = ")
                not_in = input(f"   Zat kimia {vertex} tidak boleh digabung dengan = ")
                if vertex in graph:
                    print(f"Zat Kimia {vertex} sudah ada dalam graf. Mohon masukkan zat kimia yang berbeda.")
                    continue
                if not_in:
                    not_in_list = list(not_in.replace(" ", ""))
                    if vertex in not_in_list:
                        print(f"Zat Kimia {vertex} tidak boleh digabung dengan dirinya sendiri. Mohon masukkan zat kimia yang berbeda.")
                        continue
                    if vertex in graph.values():
                        print(f"Zat Kimia {vertex} tidak boleh diinputkan kembali sebagai 'not_in'. Mohon masukkan zat kimia yang berbeda.")
                        continue
                    graph[vertex] = not_in_list
                else:
                    graph[vertex] = []
                break
    else:
        print('inputan harus berupa angka')
        time.sleep(1)
        add_item(graph1)
    validate_input()


def remove_item(graph):
    clear_screen()
    print("\n")
    print_header("Menu Pengahapusan Zat\n")
    print("|Zat Kimia| |Tidak dapat digabung dengan|")
    print(f'{"-"*40}')
    for key in graph:
        print(f'|{" "*4}{key}{" "*4}|', end="")
        for _ in key:
            print(f' |{" "*7}{graph[key]}')
    print(f'{"-"*40}')
    banyak = input("\nIngin menghapus berapa banyak Zat Kimia? ")
    if banyak.isdigit():
        for i in range(int(banyak)):
            vertex = input(f"Masukkan Zat Kimia ke-{i+1} yang ingin dihapus: ")
            if vertex in graph:
                del graph[vertex]
                for v in graph:
                    if vertex in graph[v]:
                        graph[v].remove(vertex)
                print(f"Zat Kimia {vertex} berhasil dihapus dari graph.")
                used_colors.pop(vertex, None)  #    
            else:
                print(f"Zat Kimia {vertex} tidak ditemukan dalam graph.")
                time.sleep(1)
                remove_item(graph)
    else:
        print('inputan harus berupa angka')
        time.sleep(1)
        remove_item(graph1)
    validate_input()


def displayZat(graph):
    clear_screen()
    print("\n")
    print_header("Menu display zat kimia")
    print('\nberikut zat zat yang baru anda tambahkan\n')
    print("|Zat Kimia| |Tidak dapat digabung dengan|")
    print(f'{"-"*40}')
    for key in graph:
        print(f'|{" "*4}{key}{" "*4}|', end="")
        for _ in key:
            print(f' |{" "*7}{graph[key]}')
    print(f'{"-"*40}')
    validate_input()


def get_degree(edges, vertex):
    degree = 0
    for edge in edges:
        if vertex in edge:
            degree += 1
    return degree


def display_degree(graph):
    print("\n")
    print("derajat vertex")
    edges = get_edges(graph)
    for vertex in graph1:
        degree = get_degree(edges, vertex)
        print(f"d({vertex}) : {degree}")


def bubble_sort_by_degree(vertices, edges):
    n = len(vertices)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if get_degree(edges, vertices[j]) < get_degree(edges, vertices[j + 1]):
                vertices[j], vertices[j + 1] = vertices[j + 1], vertices[j]
    return vertices


def fill_color(graph):
    edges = get_edges(graph1)
    print("\n")
    colors = [
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "pink",
    ]
    sorted_vertices = bubble_sort_by_degree(get_vertex(graph1), edges)
    print(f'pengurutan vertex = {sorted_vertices}')
    for vertex in sorted_vertices:
        available_colors = set(colors)
        for neighbor in graph[vertex]:
            if neighbor in used_colors:
                used_color = used_colors[neighbor]
                available_colors.discard(used_color)
        color = next(iter(available_colors))
        used_colors[vertex] = color
    print("\nPewarnaan Vertex:")
    for vertex, color in used_colors.items():
        print(f"Simpul {vertex}: Warna {color}")


def define_room(colors):
    clear_screen()
    print_header("menu menampilkan hasil ruangan")
    display_degree(graph1)
    fill_color(graph1)
    color_vertices = {}
    for vertex, color in colors.items():
        if color in color_vertices:
            color_vertices[color].append(vertex)
        else:
            color_vertices[color] = [vertex]

    room_number = 1
    print("\n")
    print('---Hasil ruangan---')
    for color, vertices in color_vertices.items():
        print(f"Room {room_number} ({color}): {vertices}")
        room_number += 1
    validate_input()



def result_graph():
    clear_screen()
    G = nx.Graph()
    G.add_nodes_from(vertex)
    for node, neighbors in graph1.items():
        G.add_edges_from((node, neighbor) for neighbor in neighbors)
    node_colors = [used_colors.get(node, "black") for node in G.nodes()]
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, node_color=node_colors, with_labels=True)
    plt.show()
    menu()


def print_menu():
    clear_screen()
    print("\n")
    print_header("Program Penyimpanan Zat Kimia menggunakan algoritma Welch Powell")
    print_header("Menu Program")


def menu():
    print_menu()
    print(
        """
[1] Menambahkan Zat Kimia
[2] Menghapus Zat Kimia
[3] Menampilkan Zat
[4] Menampilkan Hasil Ruangan
[5] Menampilkan Graph
[6] Keluar
"""
    )


def main():
    menu()
    while True:
        pilih_menu = int(input("Masukkan nomor menu = "))
        if pilih_menu == 1:
            add_item(graph1)
        elif pilih_menu == 2:
            remove_item(graph1)
        elif pilih_menu == 3:
            displayZat(graph1)
        elif pilih_menu == 4:
            define_room(used_colors)
        elif pilih_menu == 5:
            result_graph()
        elif pilih_menu == 6:
            exit()
        else:
            print("Inputan tidak valid, silahkan inputkan kembali")
            time.sleep(2)
            menu()
main()
