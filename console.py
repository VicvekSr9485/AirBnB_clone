#!/usr/bin/python3
"""This module defines a class HBNBCommand for python console
"""

import cmd
from models import storage
from models.base_model import BaseModel
import shlex

classes = {'BaseModel': BaseModel}


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
        elif args not in classes:
            print("** class doesn't exist **")
        else:
            obj = eval(args)
            obj.save
            print(obj.id)

    def do_show(self, args):
        """print a string representation of an object based on the class name and id """
        if not (args):
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in classes:
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    if args[1] == v.id:
                        print(v)
                        return
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
