from inout import get_command
from commands import add


def runner():
    command = get_command()
    if command.startswith("add "):
        add(command)


def main():
    keep_gonna = True
    while keep_gonna:
        runner()


if __name__ == "__main__":
    main()
