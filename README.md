# coding-challenges
This repo contains all challenges i am working on from codingChallenges


#challenges
- Word count which mimic the linux wc terminal command.
  -  It's implementation is in Python.
  -  finds the word count, byte count, line count and character count of a file

# How to use  CCWC to mimic wc command
### - fork this repo
### - change to ccwc folder 
### - you can run the ccwc.py script by running the python interpreter
### - since it is not ideal because it won't be same as linux wc command
### - change to dist sub directory and run the executable ccwc.exe which was built using pyinstaller
### - don't forget to add the path to the file you want to extract line, word, bytes about

# Different forms of running CCWC
- python ccwc.py -c file_name.txt
- python ccwc.py -l file_name.txt
- python ccwc.py -m file_name.txt
- python ccwc.py -w file_name
## or exactly 
- ccwc.exe -c file_name.txt
- ccwc.exe -l file_name.txt
- ccwc.exe -m file_name.txt
- ccwc.exe -w file_name.txt
- ccwc.exe  file_name.txt


