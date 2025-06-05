#!/usr/bin/python3
"""console.py - Command interpreter for the AirBnB clone project.

This module defines the HBNBCammand class, which provides a command-line
interface to create, show, and destroy BaseModel instances.
"""

import cmd
import shlex

from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCammand(cmd.Cmd):
    """Console interpreter for AirBnB clone.

    Provides commands to create, show, and destroy BaseModel instances.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the console."""
        return True

    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D) to exit the console."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and print its id."""
        arg = shlex.split(arg)
        class_names = {'BaseModel':BaseModel,'User':User}
        if not arg:
            print("** class name missing **")
        elif arg[0] not in class_names:   
            print("** class doesn't exist **")
        else:
            inst = class_names[arg[0]]()
            inst.save()
            print(inst.id)

    def do_show(self, arg):
        """Show the string representation of an instance."""
        arg = shlex.split(arg)
        class_names = {'BaseModel':BaseModel,'User':User}
        if arg:
            if arg[0] not in class_names:
                print("** class doesn't exist **")
            else:
                if len(arg) < 2:
                    print("** instance id missing **")
                else:
                    obj_key = f"{arg[0]}.{arg[1]}"
                    objs = storage.all()
                    try:
                        obj = objs[obj_key]
                        print(obj)
                    except KeyError:
                        print('** no instance found **')
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        arg = shlex.split(arg)
        class_names = {'BaseModel':BaseModel,'User':User}
        if arg:
            if arg[0] not in class_names:
                print("** class doesn't exist **")
            else:
                if len(arg) < 2:
                    print("** instance id missing **")
                else:
                    obj_key = f"{arg[0]}.{arg[1]}"
                    objs = storage.all()
                    try:
                        del objs[obj_key]
                        storage.save()
                    except KeyError:
                        print('** no instance found **')
        else:
            print("** class name missing **")
    
    def do_all(self, arg):
        """Show all instances of a class or all instances if no class is specified."""
        arg = shlex.split(arg)
        class_names = {'BaseModel':BaseModel,'User':User}
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        elif arg[0] not in class_names:
            print("** class doesn't exist **")
        else:
            result = [str(obj) for key, obj in objs.items() if key.startswith(arg[0])]
            if result:
                print(result)
            else:
                print(' ** no instance found **')
            
    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        arg = shlex.split(arg)
        class_names = {'BaseModel':BaseModel,'User':User}
        if arg:
            if arg[0] not in class_names:
                print("** class doesn't exist **")
            else:
                if len(arg) < 2:
                    print("** instance id missing **")
                elif len(arg) < 3:
                    print("** attribute name missing **")
                elif len(arg) < 4:
                    print("** value missing **")
                else:
                    obj_key = f"{arg[0]}.{arg[1]}"
                    objs = storage.all()
                    try:
                        obj = objs[obj_key]
                        setattr(obj, arg[2], arg[3])
                        obj.save()
                    except KeyError:
                        print('** no instance found **')
        else:
            print("** class name missing **")


if __name__ == "__main__":
    obj = HBNBCammand()
    obj.cmdloop()