from pynput.keyboard import Key, Listener, Controller

keyboard = Controller()

pointMed = "·"

listOfSing = [["'c'", "ce·tte"], ["'q'", "celui·elle"], ["'e'", "·e"], ["'d'", "du·de la"], ["'l'", "la·le"], ["'x'", "eux·se"], ["'t'", "tout·e"], ["'f'", "chef·fe"], ["'g'", "el·le"], ["'n'", "en·ne"], ["'y'", "er·ère"], ["'r'", "eur·euse"], ["'i'", "eur·rice"], ["'v'", "if·ive"]]
listOfPlur = [["'q'", "ceux·elles"], ["'e'", "·e·s"], ["'x'", "eux·ses"], ["'t'", "tou·te·s"], ["'u'", "aux·ales"], ["'f'", "chef·fe·s"], ["'g'", "el·le·s"], ["'n'", "en·ne·s"], ["'y'", "er·ère·s"], ["'r'", "eur·euse·s"], ["'i'", "eur·rice·s"], ["'v'", "if·ive·s"]]

activated = False
isPlur = False

def backspace():
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

def printWord(word):
    for x in word:
        keyboard.press(x)
        keyboard.release(x)

def on_press(key):
    global activated, isPlur
    if not(activated):
        if str(key) == "Key.shift_r":
            activated = True
            #print("hey")
    else: #activated == True
        #print("hi" + str(key))
        if str(key) == "Key.shift_r":
            activated = False
            isPlur = False
            printWord(pointMed)
        elif str(key).lower() == "'s'":
            #print("hello : " + str(isPlur))
            if isPlur:
                isPlur = False
                activated = False
            else:
                isPlur = True
                backspace()
        elif str(key) != "Key.backspace":
            activated = False
            if isPlur: #plural
                isPlur = False
                for x in listOfPlur:
                    if str(key).lower() == x[0].lower():
                        backspace()
                        printWord(x[1])
            else: #singular
                for x in listOfSing:
                    if str(key).lower() == x[0].lower():
                        backspace()
                        printWord(x[1])

def on_release(key):
    pass

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

