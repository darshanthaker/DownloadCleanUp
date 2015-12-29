"""
    Cleanup program to eliminate duplicate downloads by softlinking the duplicate files
    to the original file
"""
import sys
import os
import re

def main():
    with open('clean.txt') as inp:
        while True:
            line = inp.readline()
            if line == "":
                break
            searchObj = re.search( r' \(\d+\)\.', line, 0)
            line = line[0:len(line) - 1]
            
            if (searchObj is not None):
                original = line.replace(searchObj.group(0), ".")
                print line
                print original
                command = 'ln -sf ~/Downloads/"' + original + '" ~/Downloads/"' + line + '"'
                os.system(command)

if __name__=="__main__":
    main()

