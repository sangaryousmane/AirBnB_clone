#!/usr/bin/python3
"""This module defines the entry point of the
command interpreter, the AirBnB Console Application.
"""

import cmd
import shlex
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
        if not args:
            # If no class name is provided, print all instances
            objs = storage.all()
            obj_list = list(objs.values())

        else:
            try:
                # Try to retrieve instances based on given class name
                class_instance = eval(args)
                obj_list = [obj for obj in storage.all().values()
                            if isinstance(obj, class_instance)]

            except NameError:
                print("** class doesn't exist **")
                return

        if not obj_list:
            print("No instances found")
            # pass
        else:
            formatted_list = [str(obj) for obj in obj_list]
            print(formatted_list)

    def do_update(self, args):
        """Updates an instance based on the class name
           and id given as args by adding or updating
           attribute & save changes into JSON file.
        """
        args = shlex.split(args)  # split command into tokens

        if len(args) == 0:
            print("** class name missing **")
            return

        cls_name = args[0]

        # check if class name exists in modules {}
        if cls_name not in modules:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj_id = args[1]
        attr_name = args[2]
        attr_val = args[3]

        key = "{}.{}".format(cls_name, obj_id)

        # Retrieve the object from storage
        obj_dict = storage.all()

        if key not in obj_dict:
            print("** no instance found **")
            return

        obj = obj_dict[key]

        try:
            attr = getattr(obj, attr_name)
            attr_type = type(attr)
            attr_val = attr_type(attr_val)

        except AttributeError:
            pass
        except (ValueError, TypeError):
            # might not be neccessary, delete later
            print("** value missing **")

        # update the instance attribute
        setattr(obj, attr_name, attr_val)
        obj.save()

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
