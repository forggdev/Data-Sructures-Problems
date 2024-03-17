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


directory_name = "Module_6"
file_names = [
    "Turnos_en_el_consultorio",
    "Lucha_de_los_menores",
    "Acumulador_Obsesivo_Compulsivo",
    "Menor_Suma_Posible",
    "Sintetizador_digital_periodico",
    "No_es_Josephus"
]

create_directory_and_files(directory_name, file_names)
