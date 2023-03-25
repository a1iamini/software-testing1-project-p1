from inout import get_command, print_message
from commands import add


def runner():
    command = get_command()
    if command.startswith("add ") and add(command):
        print_message("Done")
    else:
        print_message("invalid command")


def main():
    keep_gonna = True
    while keep_gonna:
        runner()


if __name__ == "__main__":
    main()
