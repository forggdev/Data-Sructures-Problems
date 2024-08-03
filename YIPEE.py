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


directory_name = "Module_7"
file_names = [
    "Recorrido_en_pre-orden",
    "Altura_de_un_arbol",
    "Cantidad_de_hojas",
    "Hijos_unicos",
    "Dibujo_de_un_arbol",
    "Arboles_binarios_completos"
]

create_directory_and_files(directory_name, file_names)
