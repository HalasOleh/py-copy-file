def copy_file(command: str) -> None:

    try:
        com = command.split()
        cp_com = com[0]
        fil = com[1]
        new_file = com[2]
    except IndexError:
        return

    if fil == new_file:
        return
    if cp_com != "cp":
        return

    try:
        with open(fil, "r") as file_in, open(new_file, "w") as file_out:
            data = file_in.read()
            file_out.write(data)
    except FileNotFoundError:
        return
