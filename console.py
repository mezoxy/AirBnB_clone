#!/usr/bin/python3
"""The module: console"""
import cmd
import re
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """subclass of cmd"""
    prompt = "(hbnb) "

    classes = {
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "BaseModel": BaseModel,
            "User": User,
            "State": State
            }

    def do_destroy(self, args):
        """destroy: Deletes an instance"""
        lis = []
        lis = args.split()
        if len(lis) == 0:
            print("** class name missing **")
        else:
            if lis[0] not in self.classes:
                print("** class doesn't exist **")
            elif lis[0] in self.classes and len(lis) == 1:
                print("** instance id missing **")
            elif len(lis) == 2 and lis[0] in self.classes:
                cle = lis[0] + "." + lis[1]
                if cle in storage.all().keys():
                    del storage.all()[cle]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_create(self, args):
        """Creates a new instance of BaseModel\n"""

        if args in self.classes:
            u = self.classes[args]()
            storage.new(u)
            storage.save()
            print(u.id)
        if args not in self.classes and len(args) != 0:
            print("** class doesn't exist **")
        if not args:
            print("** class name missing **")

    def do_update(self, args):
        """
            Updates an instance based on the class name and id
            by adding or updating attribute
            Usage: update <class name> <id> <attribute name> "<attribute value>
        """
        lis = args.split()
        if not args:
            print("** class name missing **")
        else:
            if lis[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                if len(lis) == 1:
                    print("** instance id missing **")
                elif len(lis) == 2:
                    print("** attribute name missing **")
                elif len(lis) == 3:
                    print("** value missing **")
                else:
                    if lis[0] + "." + lis[1] in storage.all():
                        obj = storage.all()[lis[0] + "." + lis[1]]
                        try:
                            setattr(obj, lis[2], eval(eval(lis[3])))

                        except Exception:
                            setattr(obj, lis[2], eval(lis[3]))
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_show(self, args):
        """Prints the attributes of an instance based on the class name and id
            To use the command show type: show "class_name" "id"
        """
        lis = []
        lis = args.split()
        if len(lis) == 0:
            print("** class name missing **")
        else:
            if lis[0] not in self.classes:
                print("** class doesn't exist **")
            elif lis[0] in self.classes and len(lis) == 1:
                print("** instance id missing **")
            elif len(lis) == 2 and lis[0] in self.classes:
                cle = lis[0] + "." + lis[1]
                if cle in storage.all():
                    print(storage.all()[cle])
                else:
                    print("** no instance found **")

    def do_all(self, args):
        """all: prints all instances of class"""
        lis = []
        patern = r"^{}.*".format(args)
        if len(args) != 0:
            if args in self.classes:
                lis = [
                        str(val)
                        for key, val in storage.all().items() if re.match(
                            patern, key)]
                print(lis)
            else:
                print("** class doesn't exist **")
        else:
            lis = [str(val) for val in storage.all().values()]
            print(lis)

    def do_EOF(self, args):
        """EOF: exit the program\n"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        print()

    def default(self, args):
        try:
            lis = args.split(".")
            if lis[1] == "all()":
                self.do_all(lis[0])
            elif lis[1] == "count()":
                self.do_count(lis[0])
            elif re.match(r"show.*", lis[1]):
                match = re.search(r"show\(\"(.*)\"\)", lis[1])
                if match:
                    iD = match.group(1)
                    self.do_show(lis[0] + " " + iD)
            elif re.match(r"destroy", lis[1]):
                match = re.match(r"destroy\(\"(.*)\"\)", lis[1])
                iD = match.group(1)
                self.do_destroy(lis[0] + " " + iD)
            else:
                super().default(args)
        except Exception:
            super().default(args)

    def do_count(self, args):
        """Count: Count the number of intance"""
        patern = r"^{}.*".format(args)
        num_of_obj = 0
        if args:
            for key in storage.all():
                if re.match(patern, key):
                    num_of_obj += 1
            print(num_of_obj)
        else:
            for key in storage.all():
                num_of_obj += 1
            print(num_of_obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
