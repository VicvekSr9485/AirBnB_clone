#!/usr/bin/python3
"""This module defines a class HBNBCommand for python console
"""

import cmd
from models import storage
from models.base_model import BaseModel
import shlex
from datetime import datetime
from models.users import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {'BaseModel': BaseModel, "User": User, 'State': State,
           'Place': Place, 'City': City, 'Amenity': Amenity, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """HBNB Command(console application) Class"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """ End of program """
        return True

    def do_quit(self, arg):
        """ exit point of the program"""
        return True

    def emptyline(self):
        """ command to do nothing and print empty line """
        pass

    def do_create(self, args):
        """ create a new object """
        if not (args):
            print("** class name missing **")
        else:
            try:
                cls = classes[args]
            except KeyError:
                print("** class doesn't exist **")
            else:
                obj = cls()
                obj.save()
                print(obj.id)

    def do_show(self, args):
        """
        Print a string representation of an
        object based on the class name and id
        """
        if not (args):
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) == 1 and args[0] not in classes:
                print("** class doesn't exist **")
            elif len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in classes:
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    if args[1] == v.id:
                        print(v)
                        return
                print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id
        """
        if not (args):
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) == 1 and args[0] not in classes:
                print("** class doesn't exist **")
            elif len(args) != 2:
                print("** instance id missing **")
            else:
                for k, v in storage.all().items():
                    if args[1] == v.id:
                        del storage.all()[k]
                        storage.save()
                        return
                print("** no instance found **")

    def do_all(self, args):
        """  Prints all string representation of all
        instances based or not on the class name
        """
        if not (args):
            print([str(v) for v in storage.all().values()])
        else:
            args = args.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                print([str(v) for v in storage.all().values()])

    def do_update(self, arg):
        """ Updates an instance based on the class name and id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] in classes:
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                attrs = ["id", "created_at", "updated_at"]
                if obj:
                    args = shlex.split(arg)
                    if len(args) < 3:
                        print("** attribute name missing **")
                    elif len(args) < 4:
                        print("** value missing **")
                    elif args[2] not in attrs:
                        obj.__dict__[args[2]] = args[3]
                        obj.updated_at = datetime.now()
                        storage.save()
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
