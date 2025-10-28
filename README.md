# ReducePS
Helper program to convert Powershell scripts to one line for use with -Command / -c parameter. 
The program does not check for syntax and assumes that the source script is in a format that, once converted into a single line, will be interpreted correctly by cmd. For example, you will need to add semicolons to the end of statements and double quotes will need to be escaped.  


```
usage: reducePS.py [-h] source_file target_directory
```

1. For an example run the following command:
```
python3 reducePS.py examples/example1.ps1 examples
```

2. Paste result into the command argument `execute --command ""` in response actions. 