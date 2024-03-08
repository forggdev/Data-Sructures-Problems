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


directory_name = "Module_5"
file_names = [
    "Sumatoria_de_Multiplos",
    "De_Tin_Marin",
    "Teclado_Numerico",
    "Juego_de_Eliminacion",
    "Encontrando_la_mediana",
    "Autografo_de_Serena"
]

create_directory_and_files(directory_name, file_names)
