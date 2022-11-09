with open('testdoc.txt') as line:

    charac = line.read()

    print(charac)

def wordfreq(string):

    list = string.split()
    
    newlist =  []

    for x in list :
        
        if x not in newlist :
            
            newlist.append(x)
    
    for x in range (0, len(newlist)) :
        
        print("The frequncy of the word", newlist[x], "is", list.count(newlist[x]))

        wordfreq(charac)

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pim.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


