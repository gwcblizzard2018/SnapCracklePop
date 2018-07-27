#  ~   Command Receptive Interactive Software .Py   ~  #
import pyautogui
import speech_recognition as sr

key_words = ['Location', 'Click', 'Right Click', 'Type' 'Scroll', 'Move to:', 'Close Tab', 'New Window', 'Next Tab', 'New Tab']
pyautogui.KEYBOARD_KEYS
print('''Hello and welcome to CRIS.Py. Your personal Command Receptive Interactive Software! This program will allow you to maneuver your personal computer hands free! With specified key words you can maneuver over screens, click buttons, open tabs and much more! ''')
print("  The key words are vocal commands you can say to cause an action. CRIS.Py's key words are as follows: {}".format(key_words))
print("""    The 'Move to:' key word functions to allow you to move your mouse anywhere one your screen based on an coordinate. For example if you say 'Move to: 0, 1079' the mouse will move to the bottom left corner of the window.   """)


while True:
    r = sr.Recognizer()
    m = sr.Microphone()
    try:
        print("A moment of silence, please...")
        #with m as source:
        r.adjust_for_ambient_noise(m)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                command = r.recognize_google(audio)

                # we need some special handling here to correctly print unicode characters to standard output
                #if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                    #print(u"You said {}".format(value).encode("utf-8"))
              # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(command.title()))
                command = command.title()
                if command == "Location":
                    print(pyautogui.position())
                elif command == "Click":
                    pyautogui.click()
                elif command == "Right Click":
                    pyautogui.rightClick()
                elif command == "Type":
                    colon = ":"
                    print("Say what you would like to type")
                    with m as source: audio = r.listen(source)
                    print("Got it! Now to recognize it...")
                    try:
                    # recognize speech using Google Speech Recognition
                        type_source = r.recognize_google(audio)
                        pyautogui.typewrite(type_source,1)
                    except:
                        pass
                elif command == "Scroll Up":
                    pyautogui.moveTo(960,540)
                    pyautogui.click()
                elif command == "Scroll Down":
                    pyautogui.moveTo(960,540)
                    pyautogui.scroll(-100)
                elif command == "Move to":
                    print("Okay please list your x-coordinate: ")
                    with m as source: audio = r.listen(source)
                    print("Got it! Now to recognize it...")
                    try:
                        # recognize speech using Google Speech Recognition
                        x_coor = r.recognize_google(audio)
                        print("Okay please list your y-coordinate: ")
                        with m as source: audio = r.listen(source)
                        print("Got it! Now to recognize it...")
                        # recognize speech using Google Speech Recognition
                        y_coor = r.recognize_google
                        pyautogui.moveTo(x_coor, y_coor)
                    except:
                        pass
                elif command == "Close Tab":
                    pyautogui.moveTo(960,540)
                    pyautogui.keyDown("ctrl")
                    pyautogui.keyDown("f4")
                    pyautogui.keyUp("ctrl")
                    pyautogui.keyUp("f4")
                elif command == "New Window":
                    pyautogui.moveTo(960,540)
                    pyautogui.keyDown("ctrl")
                    pyautogui.keyDown("n")
                    pyautogui.keyUp("ctrl")
                    pyautogui.keyUp("n")
                elif command == "New Tab":
                    pyautogui.moveTo(960,540)
                    pyautogui.keyDown('ctrl')
                    pyautogui.keyDown('t')
                    pyautogui.keyUp('ctrl')
                    pyautogui.keyUp('t')
                elif command == "Next Tab"
                    ,540)
                    pyautogui.keyDown('ctrl')
                    pyautogui.keyDown('tab')
                    pyautogui.keyUp('ctrl')
                    pyautogui.keyUp('tab')
                else:
                    print ("Sorry, I don't understand. Try one of these: {}".format(key_words))
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass


    #   ~    HOTKEYS    ~   #
    # ctrl + n = new window   ctrl + tab = next tab
    # ctrl + t = new tab      ctrl + F4 = close tab     F11 = full screen
