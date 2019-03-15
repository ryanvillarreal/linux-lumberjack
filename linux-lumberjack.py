#!/usr/bin/python
from shutil import copyfile
from shutil import move
from os import remove
import os
import os.path
import sys


homedir = os.environ['HOME']
target_file = homedir + "/.bashrc"
backup_file = homedir + "/.backup-bashrc"
new_file = homedir + "/.newbashrc"

def add_log_file_creation():
        with open(target_file, "a") as f:
                ### Add a line to the .bashrc file to create a new log file and log all shell commands
                f.write("test \"$(ps -ocommand= -p $PPID | awk \'{print $1}\')\" == \'script\' || (script -f $HOME/$(date +\"%d-%b-%y_%H-%M-%S\")_"$companyname"_shell.log)")

def modify_terminal_line():
        with open(new_file, "w") as newfile:
                with open (target_file) as oldfile:
                        for line in oldfile:
                                if line.find("PS1") != -1 and not line.strip().startswith("#"):
                                        if line.strip().startswith('PS1="\[\e]'):
                                                #print "Correct: " + line.strip()
                                                newfile.write("echo 'who are we hacking today?'; read companyname; PS1=\'[`date  +\"%d-%b-%y %T\"`][rlv][$companyname]\\[\\033[01;31m\\] \\[\\033[00m\\] \\[\\033[01;34m\\]\\W\\[\\033[00m\\] >'"  + "\n")
                                        else:
                                                newfile.write(line)
                                else:
                                        newfile.write(line)
        remove(target_file)
        move(new_file,target_file)

def main():
        if os.path.isfile(target_file):
                copyfile(target_file, backup_file) ### make a back-up of the .bashrc
                             add_log_file_creation()
                modify_terminal_line()
   
        else:
                print "No .bashrc exists.  Exiting..."

if __name__ == "__main__":
        main()
        print "Might need to start a new terimnal or source .bashrc"
