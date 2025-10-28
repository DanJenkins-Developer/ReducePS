#!/usr/bin/env python3

# Dan Jenkins 09/04/25
#
# Helper program to convert Powershell scripts to one line for use with -Command / -c parameter.
# 
# The program does not check for syntax and assumes that the original script is in a format that, once converted 
# into a single line, will execute correctly when passed to the -Command / -c. Comments are removed from scripts.

import argparse
from pathlib import Path

def reduce(script: str):
    # Open source file.
    with script.open('r') as s:
        lines = s.readlines()

    # Strip out content like comments and spaces
    commands = [line.strip() for line in lines if lineConditionsMet(line.strip())]

    # create one line with space splitting each item from contennt then append to the path to powershell
    command = ' '.join(commands)
    path = 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -NoProfile -WindowStyle Hidden -Command'
    cmd = f"{path} \"{command}\""

    return cmd

def lineConditionsMet(l : str):
    met = True
    if (l == "" or 
        l.startswith("#")):

        met = False
    
    return met

def write_out(content: str, directory: str, file: str = ""):

    if (file ==""):
        file = 'reduced.cmd'

    with open(directory / file, 'w') as f:
        f.writelines(content)

if __name__ == "__main__":

    # Parse command line args. Source powershell script and a target directory for the reduced script are required.
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file", help="Path to Powershell script.", type=str)
    parser.add_argument("target_directory", help="Target directory for the converted file.", type=str)
    args = parser.parse_args()

    # Make provided paths absolute
    sfile = Path(args.source_file).resolve()
    tdir = Path(args.target_directory).resolve()

    # Check if the user provided arguments exist.
    if (not sfile.is_file()):
        msg = f"reducePS: {str(sfile)} : No such file" 
        exit(msg)

    if (not tdir.is_dir()):
        msg = f"reducePS: {str(tdir)} : No such directory"
        exit(msg)

    write_out(reduce(sfile), tdir)




