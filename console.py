#!/usr/bin/python3
"""This module defines a class HBNBCommand for python console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB Command(console application) Class"""
    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """ End of program """
        return True

    def do_quit(self, arg):
        """ exit point of the program"""
        return True

    def emptyline(self):
        """ command to do nothing and print empty line """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
