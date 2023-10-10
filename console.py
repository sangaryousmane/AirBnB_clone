#!/usr/bin/python3

"""This module defines the entry point of the
command interpreter, the AirBnB console application.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Implementation of the command interpreter."""
    prompt = ("(hbnb) ")

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, args):
        """Exits the program when an
           EOF signal is send & recieve.
        """
        return True

    def emptyline(self):
        """Prints nothing when an emtpy line is passed."""
        pass


if __name__ == "__main__":
    """Program entry point."""
    HBNBCommand().cmdloop()
