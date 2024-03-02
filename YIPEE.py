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


directory_name = "Module_1"
file_names = [
    "Encuentra_el_cuadrado",
    "Hola_mundo_bilingue",
    "Positivos_y_negativos",
    "Los_4_fantasticos",
    "Potencias_menores",
    "Conjetura_de_Collatz"
]

create_directory_and_files(directory_name, file_names)
