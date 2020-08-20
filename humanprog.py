import os
import pyttsx3 as p
print("Hello Sir, I am a menu driven python program and I will do following for you.\n")
p.speak("Hello Sir, I am a menu driven python program and I will do following for you.")
print('I can open Windows Media Player.\nI can open Google Chrome.\nI can open SoundWire Server.\nI can open Command Prompt.\nI can open Internet Explorer.\nI can open notepad.\nI can open This PC.\nI can open Calculator.\nI can open Microsoft Paint.\n')
print("Please tell me what I have to do for you Sir?\n")
p.speak("Please tell me what I have to do for you Sir?")
while True:
    n = input()
    n = n.lower()
    if ((("open" in n) or ("start" in n) or ("run" in n) or ("execute" in n)) and (("soundwire" in n) or ("soundwire server" in n))):
        p.speak("opening soundwire server, sir")
        os.system("SoundWireServer")

    elif ((("open" in n) or ("start" in n) or ("run" in n) or ("execute" in n)) and (("notepad" in n) or ("text editor" in n) or ("text file" in n))):
        p.speak("opening notepad, sir")
        os.system("notepad")
        
    elif ((("open" in n) or ("start" in n) or ("run" in n) or ("execute" in n)) and (("windows media" in n) or ("media player" in n))):
        p.speak("opening windows media player, sir")
        os.system("wmplayer")
        
    elif ((("open" in n) or ("start" in n) or ("run" in n) or ("execute" in n)) and (("google" in n) or ("chrome" in n) or ("browser" in n))):
        p.speak("opening google chrome, sir")
        os.system("chrome")
        
    elif ((("open" in n) or ("start" in n) or ("run" in n) or ("execute" in n)) and (("internet explorer" in n) or ("explorer" in n))):
        p.speak("opening internet explorer, sir")
        os.system("iexplore")
        
    elif ((("open" in n) or ("start" in n) or ("run" in n) or ("execute" in n)) and (("this pc" in n) or ("this computer" in n) or ("file manager" in n))):
        p.speak("opening file manager, sir")
        os.system("explorer")
        
    elif ((("open" in n) or ("start" in n) or ("run" in n) or ("execute" in n)) and ("calculator" in n)):
        p.speak("opening calculator, sir")
        os.system("calc")
        
    elif ((("open" in n) or ("start" in n) or ("run" in n) or ("execute" in n)) and (("paint" in n) or ("drawing board" in n))):
        p.speak("opening microsoft paint, sir")
        os.system("mspaint")

    elif ((("open" in n) or ("start" in n) or ("run" in n) or ("execute" in n)) and (("cmd" in n) or ("command prompt" in n))):
        p.speak("opening command prompt, sir")
        os.system("cmd")
        
    elif ((("do not" in n) or ("don't" in n) or ("dont" in n) or ("doesn't" in n) or ("not" in n)) and (("anything" in n) or ("task" in n))):
        print("Ok sir, I am always at your service you can call me anytime, Thank You")
        p.speak("Ok sir, I am always at your service you can call me anytime, Thank You")
        break
    else:
        print("Sir, I can't understand which type of task you want to give to me. Please enter a valid task.")
        p.speak("Sir, I can't understand which type of task you want to give to me. Please enter a valid task.")


    print("You can give me more tasks as you like.\n")
    p.speak("You can give me more tasks as you like, sir")

