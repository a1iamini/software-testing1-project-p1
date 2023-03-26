from inout import get_command, print_message
from commands import add, define


def runner():
    command = get_command()
    if command.startswith("add ") and add(command):
        print_message("Done")
    elif command.startswith("define sweets "):
        define(command)
    elif command == "exit":
        return False
    else:
        print_message("invalid command")
    return True


def main():
    keep_gonna = True
    while keep_gonna:
        if not runner():
            keep_gonna = False
    exit(0)


if __name__ == "__main__":
    main()
