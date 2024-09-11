import os


def create_directory_and_files(directory_name, file_names):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    # Change directory to the newly created one
    os.chdir(directory_name)

    # Create Python files with names from the list
    for file_name in file_names:
        with open(file_name + ".py", "w") as file:
            file.write("")


directory_name = "Module_11"
file_names = [
    "Paulina_Bailarina",
    "La_magia_del_chisme",
    "Juego_de_tronos_criollo",
    "Grafos_bipartitos",
    "Deforestacion_en_el_amazonas",
    "Movimientos_del_caballo"
]

create_directory_and_files(directory_name, file_names)
