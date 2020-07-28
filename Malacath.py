#!/usr/bin/python3
import cmd
import subprocess


class Malacath(cmd.Cmd):
    """Simple command processor example."""
    prompt = 'Malacath> '

    def __init__(self):
        super().__init__()
        print(r"""                                                                                                                                                                                                                                                                                                                                                                                                             
     MMMMMMMM               MMMMMMMM                  lllllll                                                                tttt         hhhhhhh             
     M:::::::M             M:::::::M                  l:::::l                                                             ttt:::t         h:::::h             
     M::::::::M           M::::::::M                  l:::::l                                                             t:::::t         h:::::h             
     M:::::::::M         M:::::::::M                  l:::::l                                                             t:::::t         h:::::h             
     M::::::::::M       M::::::::::M  aaaaaaaaaaaaa    l::::l   aaaaaaaaaaaaa      cccccccccccccccc  aaaaaaaaaaaaa  ttttttt:::::ttttttt    h::::h hhhhh       
     M:::::::::::M     M:::::::::::M  a::::::::::::a   l::::l   a::::::::::::a   cc:::::::::::::::c  a::::::::::::a t:::::::::::::::::t    h::::hh:::::hhh    
     M:::::::M::::M   M::::M:::::::M  aaaaaaaaa:::::a  l::::l   aaaaaaaaa:::::a c:::::::::::::::::c  aaaaaaaaa:::::at:::::::::::::::::t    h::::::::::::::hh  
     M::::::M M::::M M::::M M::::::M           a::::a  l::::l            a::::ac:::::::cccccc:::::c           a::::atttttt:::::::tttttt    h:::::::hhh::::::h 
     M::::::M  M::::M::::M  M::::::M    aaaaaaa:::::a  l::::l     aaaaaaa:::::ac::::::c     ccccccc    aaaaaaa:::::a      t:::::t          h::::::h   h::::::h
     M::::::M   M:::::::M   M::::::M  aa::::::::::::a  l::::l   aa::::::::::::ac:::::c               aa::::::::::::a      t:::::t          h:::::h     h:::::h
     M::::::M    M:::::M    M::::::M a::::aaaa::::::a  l::::l  a::::aaaa::::::ac:::::c              a::::aaaa::::::a      t:::::t          h:::::h     h:::::h
     M::::::M     MMMMM     M::::::Ma::::a    a:::::a  l::::l a::::a    a:::::ac::::::c     ccccccca::::a    a:::::a      t:::::t    tttttth:::::h     h:::::h
     M::::::M               M::::::Ma::::a    a:::::a l::::::la::::a    a:::::ac:::::::cccccc:::::ca::::a    a:::::a      t::::::tttt:::::th:::::h     h:::::h
     M::::::M               M::::::Ma:::::aaaa::::::a l::::::la:::::aaaa::::::a c:::::::::::::::::ca:::::aaaa::::::a      tt::::::::::::::th:::::h     h:::::h
     M::::::M               M::::::M a::::::::::aa:::al::::::l a::::::::::aa:::a cc:::::::::::::::c a::::::::::aa:::a       tt:::::::::::tth:::::h     h:::::h
     MMMMMMMM               MMMMMMMM  aaaaaaaaaa  aaaallllllll  aaaaaaaaaa  aaaa   cccccccccccccccc  aaaaaaaaaa  aaaa         ttttttttttt  hhhhhhh     hhhhhhh                                                                                                         
        """)

    def do_greet(self, line):
        """just print hello"""
        print('hello')

    def do_exit(self, line):
        print("goodbye")
        return True

    def help_exit(self):
        print('.'.join([
            'this command will make you exit from the shell',
        ]))

    def do_shell(self, line):
        "Run a shell command"
        print("running shell command:", line)
        sub_cmd = subprocess.Popen(line,
                                   shell=True,
                                   stdout=subprocess.PIPE)
        output = sub_cmd.communicate()[0].decode('utf-8')
        print(output)


if __name__ == '__main__':
    Malacath().cmdloop()
