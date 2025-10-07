import pyttsx3, time

engine = pyttsx3.init()
engine.say("Testing voice system. Jarvis is working fine.")
engine.runAndWait()
time.sleep(0.5)
engine.say("If you hear this, your text to speech is okay.")
engine.runAndWait()
