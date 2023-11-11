#!/usr/bin/python3
import cmd

class Test(cmd.Cmd):
    """Testing"""
    def default_(self, args):
        """hola"""
        print(args)

if __name__ == '__main__':
    Test().cmdloop()
