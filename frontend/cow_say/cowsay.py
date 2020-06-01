
# Original repo: https://github.com/VaasuDevanS/cowsay-python
# Modified to print to the stream instead of console

#  Developer : Vaasu Devan S
#  Email     : vaasuceg.96@gmail.com
#              www.github.com/VaasuDevanS

#  cowsay for GNU/Linux was initially written in perl by Tony Monroe (tony@nog.net), with suggestions from Shannon Appel (appel@CSUA.Berkeley.EDU) and contributions from Anthony Polito (aspolito@CSUA.Berkeley.EDU).

# ___________________________________________________________________________________________________________________________ #

# Characters.py contains the Ascii code for the characters.
# Initial cowsay will have lots of characters than this.. But these are my favourite.

from __future__ import print_function
import re
import sys
import io

flg=[]

Cow = '''

   ^__^                             
   (oo)\_______                   
   (__)\       )\/\             
       ||----w |           
       ||     ||  
       
       '''


Pig = '''

             ,.
            (_|,.
            ,' /, )_______   _
        __j o``-'        `.'-)'
        (")                 \'
        `-j                |
            `-._(           /
                |_\  |--^.  /
            /_]'|_| /_)_/
                /_]'  /_]'

      '''


Tux = ''' 

        .--.
       |o_o |
       |:_/ |
      //   \\ \\
     (|     | )
    /'\\_   _/`\\
    \\___)=(___/
    
    '''

def about():
    
    print('''
    
             Original Author---> Tony Monroe (tony@nog.net)       # Thanks to him... !
             For Python     ---> Vaasu Devan S
             Email          ---> vaasuceg.96@gmail.com
             __version__    ---> 2.0.3
             
             visit my github page @ www.github.com/VaasuDevanS
             
             Cowsay for GNU/Linux is very very famous. 
			 It would be fun and cool to have those characters in python..
             
             Available Characters (in python): 
             ==============================================
             |'beavis'     'dragon'         'pig'         |
             |'turtle'     'ghostbusters'   'tux'         |
             |'cheese'     'kitty'          'turkey'      |
             |'daemon'     'meow'           'stegosaurus' |
             |'cow'        'milk'           'stimpy'      |
             ==============================================
             
             syntax:-
             
             >>> import cowsay 
             >>> cowsay.<character-name>(text-message)
             
                            (or)
                            
             >>> from cowsay import *
             >>> <character-name>(text-message)
             
             Example:-
             
             >>> import cowsay
             >>> cowsay.tux("Python is fun")
        
                 _______________            
                < Python is fun >
                -----------------
                               \\
                                \\
                                 \\
                                   .--.
                                  |o_o |
                                  |:_/ |
                                //   \\ \\
                                (|     | )
                               /'\\_   _/`\\
                               \\___)=(___/
                               
                               
            Enjoy coding with python and cowsay   :)
    
        ''')

__version__ = '2.0.3'
__name__ = 'cowsay' #For python


def String_processing(out, args):

    args=str(args)
    length=len(args)
    lines=args.split("\n")
    lines=[i.strip() for i in lines]
    lines=[i for i in lines if len(i)!=0]
    length=len(lines)
    
    if length==1:
        flag=len(lines[0])
        if flag<50:
            print("  "+"_"*flag, file=out)
            print("< "+lines[0]+" "*(flag-len(lines[0])+1)+">", file=out)
            print("  "+"="*flag, file=out)
            flg.append(flag)
        else:
            args=list("".join(lines[0]))
            for j,i in enumerate(args):
                if j%50==0:
                    args.insert(j,"\n")
            String_processing(out, "".join(args))
               
    else:
        flag=len(max(lines,key=len))
        if all(len(i)<50 for i in lines): 
            print("  "+"_"*flag, file=out)
            print(" /"+" "*flag+"\\", file=out)            
            for i in lines:
                print("| "+i+" "*(flag-len(i)+1)+"|", file=out)
            print(" \\"+" "*flag+"/", file=out)
            print("  "+"="*flag, file=out)
            flg.append(flag)                    
        else:
            new_lines=[]
            for i in lines:
                if len(i)>50:
                    args=list("".join(i))
                    for j,i in enumerate(args):
                        if j%50==0:
                            args.insert(j,"\n") 
                    new_lines.append("".join(args))
                else:
                    new_lines.append(i+"\n")
            String_processing(out, "".join(new_lines))
                    
                    
# Functions start here..        
    
def cow(args):

    with io.StringIO() as output: 
        String_processing(output, args)
        flag=flg[-1]
            
        print(" "*(flag+5)+"\\", file=output)
        print(" "*(flag+6)+"\\", file=output)
    
        char_lines=Cow.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag+5)+i, file=output)
        
        return output.getvalue()



def pig(args):

    with io.StringIO() as output: 

        String_processing(output, args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\", file=output)
        print(" "*(flag+6)+"\\", file=output)
        print(" "*(flag+7)+"\\", file=output)
        print(" "*(flag+8)+"\\", file=output)

        char_lines=Pig.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*(flag+5)+i, file=output)

        return output.getvalue() 


def tux(args):

    with io.StringIO() as output: 
                
        String_processing(output, args)
        flag=flg[-1]
        
        print(" "*(flag+5)+"\\", file=output)
        print(" "*(flag+6)+"\\", file=output)
        print(" "*(flag+7)+"\\", end='', file=output)
    
        char_lines=Tux.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]
    
        for i in char_lines:
            print(" "*(flag)+i, file=output)

        return output.getvalue() 

chars = [cow ,  pig,  tux]

char_names = ['beavis', 'cheese', 'daemon', 'cow', 'dragon', 'ghostbusters', 'kitty', 'meow', 'milk', 'pig', 'stegosaurus', 'stimpy', 'turkey', 'turtle', 'tux']
    
def cli():
    if '--version' in sys.argv[1:]:
        print(__version__)
        exit(0)
    cow(' '.join(sys.argv[1:]))
# End of File #
