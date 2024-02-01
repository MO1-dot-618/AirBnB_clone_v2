#!/usr/bin/python3
"""Module for HBNBCommand class"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command Line Interpreter"""

    prompt = "(hbnb) "
    all_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, args):
        """Quits program"""
        return True

    def do_EOF(self, line):
        """ Quits program """
        return True

    def emptyline(self):
        """does not execute anything"""
        pass

    def do_create(self, args):
        """creates an instance of a  class"""
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        else:
            B = eval(args)()
            print(B.id)
            storage.save()

    def do_show(self, args):
        """ prints instance of class"""
        a = args.split()
        if not args:
            print("** class name missing **")
        elif a[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif len(a) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                if value.id == a[1].strip():
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """ destroys an instance of class"""
        a = args.split()
        if not args:
            print("** class name missing **")
        elif a[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif len(a) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                if value.id == a[1].strip():
                    del(value)
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances"""

        a = args.split()
        if len(a) == 0 or a[0] in HBNBCommand.all_classes:
            all_list = []
            all_objs = storage.all()
            for key, value in all_objs.items():
                all_list.append(str(value))
            print(all_list)
        elif a[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id"""

        arg = args.split()
        if not args:
            print("** class name missing **")
        if arg[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        elif len(arg) > 4:
            return
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                if value.id == arg[1].strip():
                    if hasattr(value, arg[2]):
                        setattr(storage._FileStorage__objects[key],
                                arg[2], arg[3])
                        storage.save()
                        return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
