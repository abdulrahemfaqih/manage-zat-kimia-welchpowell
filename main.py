from src.views.menu import menu, add_item, remove_item, result_graph, define_room, displayZat
from src.utils.graph_utils import *
import time


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


if __name__ == "__main__":
    main()

