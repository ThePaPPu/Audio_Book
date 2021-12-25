import pyttsx3

string = "Stay Home, Stay Safe"
speaks = pyttsx3.init()
speaks.say(string)
speaks.runAndWait()