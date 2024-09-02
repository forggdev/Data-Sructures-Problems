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


directory_name = "Module_10"
file_names = [
    "Traductor_Ewokes_Castellano",
    "Las_Trillizas_de_Belleville",
    "Balotodo",
    "Plebeya_Academia_de_la_Jerga",
    "Conteo_de_votos",
    "Conjetura_de_Goldbach"
]

create_directory_and_files(directory_name, file_names)
