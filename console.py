#!/usr/bin/python3
"""This module defines the entry point of the
command interpreter, the AirBnB Console Application.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place

modules = {'BaseModel': BaseModel, 'User': User, "State": State,
           "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

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

    def do_create(self, arg):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        args = arg.split()

        if not HBNBCommand.is_classname_valid(args):
            return

        new_obj = modules[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split()

        if not HBNBCommand.is_classname_valid(args, check_id=True):
            return

        all_obj = storage.all()
        key = f'{args[0]}.{args[1]}'
        show_instances = all_obj.get(key, None)
        if show_instances is None:
            print("** no instance found **")
            return

        print(show_instances)

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and
        id (save the change into the JSON file).
        """
        args = arg.split()
        if not HBNBCommand.is_classname_valid(args, check_id=True):
            return

        all_obj = storage.all()
        key = f'{args[0]}.{args[1]}'
        show_instances = all_obj.get(key, None)

        if show_instances is None:
            print(" ** no instance found **")
        print(show_instances)

        del all_obj[key]
        storage.save()

    def do_all(self, args):
        """ Prints all string representation of all instances
            based or not on the class name.
        """

    @staticmethod
    def is_classname_valid(args, check_id=False) -> bool:
        """ Validates classname, length of arugment, missing classname et al.
        """
        if len(args) < 1:
            print("** class name missing **")
            return False
        if args[0] not in modules.keys():
            print("** class doesn't exist **")
            return False
        if len(args) < 2 and check_id:
            print("** instance id missing **")
            return False
        return True

if __name__ == "__main__":
    """Program entry point."""
    HBNBCommand().cmdloop()
