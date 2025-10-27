#!/usr/bin/env python3

# Dan Jenkins 09/04/25
#
# Helper program to convert Powershell scripts to one line for use with -Command / -c parameter.
# 
# The program does not check for syntax and assumes that the original script is in a format that, once converted 
# into a single line, will execute correctly when passed to the -Command / -c. Comments are removed from scripts.

def lineConditionsMet(l : str):
    met = True
    if (l == "" or 
        l.startswith("#")):

        met = False
    
    return met

import argparse
from pathlib import Path

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

# Open source file.
with sfile.open('r') as script:
    content = script.readlines()

# Modify list.
content = [line.strip() for line in content if lineConditionsMet(line.strip())]

# create one line with space splitting each item from contennt
one_line = ' '.join(content)

# Write out to a new file
fname = 'reduced.ps1'
with open(tdir / fname, 'w') as f:
    ver = 'v1.0'
    f.writelines([
        one_line + '\n',
        f"# execute --command \"C:\\Windows\\System32\\WindowsPowerShell\\{ver}\\powershell.exe -NoProfile -WindowStyle Hidden -Command \"{one_line}\"\""
    ])