"""

"""

import jsonrpclib
import json
import sys
from jsonrpclib import Server as server
from jsonrpclib import *
from pprint import pprint as pp

eos = []
commands = []
""" connect to the EOS boxes """

def connect_box (filename):
    try:
        dfile = open(filename, "r") 
    except IOError:
        #print ("file doesn't exist\n")
        pass
    else:
        with dfile:
            lines = dfile.readlines ()
            for i in range (len(lines)):
                eos.append (server (lines[i]))

""" get all the commands from text file """    
def get_cmds (filename):
    try:
        dcmds = open(filename, "r")
    except IOError:
        #print ("file doesn't exist\n")
        pass
    else:
        with dcmds:
            lines = dcmds.readlines ()
            for i in range (len (lines)):
                commands.append (lines[i])
""" run the commands and get output """  
def run_cmds ():
    for i in range (len (eos)):
        try:
            data = eos[i].runCmds (1, commands)
        except:
            pass
            #sys.exit(1)

    with open ('data.txt', 'w') as out:
        json.dump (data, out)
#        pp (data)

connect_box ("urls.txt")
get_cmds ("cmds.txt")
run_cmds ()
