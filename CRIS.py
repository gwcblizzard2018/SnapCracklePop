#  ~   Command Receptive Interactive Software .Py   ~  #
import pyautogui
import speech_recognition as sr

key_words = ['Location', 'Click', 'Right Click', 'Scroll', 'Move To', 'Close Tab', 'New Window', 'Next Tab', 'New Tab', 'Reopen Tab', 'Exit']
pyautogui.KEYBOARD_KEYS
print('''Hello and welcome to CRIS.Py. Your personal Command Receptive Interactive Software! This program will allow you to maneuver your personal computer hands free! With specified key words you can maneuver over screens, click buttons, open tabs and much more! ''')
print("  The key words are vocal commands you can say to cause an action. CRIS.Py's key words are as follows: {}".format(key_words))
print("""    The 'Move to:' key word functions to allow you to move your mouse anywhere one your screen based on an coordinate. For example if you say 'Move to: 0, 1079' the mouse will move to the bottom left corner of the window.   """)


while True:
    r = sr.Recognizer()
    m = sr.Microphone()
    try:
        print("A moment of silence, please...")
        with m as source: r.adjust_for_ambient_noise(source)
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

                elif command == "Scroll Up":
                    pyautogui.scroll(100)

                elif command == "Scroll Down":
                    pyautogui.scroll(-100)

                elif command == "Move To":
                    print("Okay please list your x-coordinate: ")
                    while True:
                        try:
                        # recognize speech using Google Speech Recognition
                            with m as source: audio = r.listen(source)
                            print("Got it! Now to recognize it...")
                            x_coor = int(r.recognize_google(audio))
                            print("You said {}".format(x_coor))
                            break
                        except:
                            print("Sorry, I don't understand.")
                    print("Okay please list your y-coordinate: ")
                    while True:
                        try:
                        # recognize speech using Google Speech Recognition
                            with m as source: audio = r.listen(source)
                            print("Got it! Now to recognize it...")
                            y_coor = int(r.recognize_google(audio))
                            print("You said {}".format(y_coor))
                            break
                        except:
                            print("Sorry, I don't understand.")
                    pyautogui.moveTo(x_coor, y_coor)

                elif command == "Close Tab":
                    pyautogui.keyDown("ctrl")
                    pyautogui.keyDown("f4")
                    pyautogui.keyUp("ctrl")
                    pyautogui.keyUp("f4")

                elif command == "Reopen Tab":
                    pyautogui.keyDown("ctrl")
                    pyautogui.keyDown("t")
                    pyautogui.keyDown("shift")
                    pyautogui.keyUp("shift")
                    pyautogui.keyUp("ctrl")
                    pyautogui.keyUp("t")

                elif command == "New Window":
                    pyautogui.keyDown("ctrl")
                    pyautogui.keyDown("n")
                    pyautogui.keyUp("ctrl")
                    pyautogui.keyUp("n")

                elif command == "New Tab":
                    pyautogui.keyDown('ctrl')
                    pyautogui.keyDown('t')
                    pyautogui.keyUp('ctrl')
                    pyautogui.keyUp('t')

                elif command == "Next Tab":
                    pyautogui.keyDown('ctrl')
                    pyautogui.keyDown('tab')
                    pyautogui.keyUp('ctrl')
                    pyautogui.keyUp('tab')

                elif command == "Exit":
                    break
                else:
                    print ("Sorry, I don't understand. Try one of these: {}".format(key_words))
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass
    break 
