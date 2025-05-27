import cmd
class HBNBCammand(cmd.Cmd):
    prompt="(hbnb) "
    def do_quit(self,arg):
        '''quiting the console'''
        return True
    def do_EOF(self,arg):
        '''End of the file'''
        print()
        return True
    def emptyline(self):
        pass

if __name__=="__main__":
    obj=HBNBCammand()
    obj.cmdloop()