# Écriture Inclusive Keyboard


If you have any questions, feel free to email me at cryptoCookie@butre.fr

## Disclaimer
This keyboard was built on Ubuntu 20.04, it is pretty okay but it isn't great, but it's still pretty cool\
My keyboard is an English (US, intl, with dead keys) keyboard but it should work with other keyboards

You will be partially sacrificing your right shift key


## Documentation ?
Refer to list.txt for the shortcuts (most are logical, some are by lack of space) \
The format is
singular thing that will appear --> plural thing that will appear --> the letter to make it appear (for plural do s and then that letter)\
To change the shortcuts : change the lists at the start of the python script ecriture-inclusiveV2.py.


## For Installation

    open backgroundRunner.py and edit the PATH variable to be the path to ecriture-inclusiveV2.py (by default it's correct if you keep both files in the same folder)

    Bash
    pip install pynput

    then :
    open startupApplications
    Add
    name : what you want
    Command : python3 path/to/folder/ecriture-inclusive-code/backgroundRunner.py
    comment : what you want

    (the backgroundRunner relaunches the code every hour because the point median stops being outputted after a certain time ¯\_(ツ)_/¯)

    TADA

## For usage

    press right shift to start ecriture inclusive mode
    pressing right shift again will place a point median and leave ecriture inclusive mode

    pressing s will enter plural mode

    pressing a letter that is bound to a shortcut will make that shortcut appear (in plural if plural mode is on)
   
    any other letter will exit ecriture inclusive mode

woke on