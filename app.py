from inout import get_command, print_message
from commands import add, define, buy


def runner():
    command = get_command()
    if command.startswith("add ") and add(command):
        print_message("Done")
    elif command.startswith("define sweets ") and define(command):
        print_message("Done")
    elif command.startswith("customer buy "):
        try:
            if buy(command):
                print_message("Done")
            else:
                print_message("Insufficient material")
        except ValueError:
            print_message("invalid command")
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
