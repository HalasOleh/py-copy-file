def copy_file(command: str) -> None:

    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    destination_file = command_parts[1]
    new_file = command_parts[2]

    try:
        with (open(destination_file, "r") as file_in,
              open(new_file, "w") as file_out):
            data = file_in.read()
            file_out.write(data)
    except FileNotFoundError:
        return
