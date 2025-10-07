import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


# firstly we have to make recogizer object to recognize what we tell
recognizer = sr.Recognizer()
# next we have to initialize engine and by init it will be initialized
engine = pyttsx3.init()   
# newsapi = "0aefa14556b74b60949627f71f442813"


# now we have to make a function which takes text and speaks it
def speak(text):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine


# creating function for processing command
def processCommand(c):
  if "open google" in c.lower():
      speak("opening")
      webbrowser.open("https://www.google.com")
  elif "open facebook" in c.lower():
      speak("opening")
      webbrowser.open("https://www.facebook.com")
  elif "open youtube" in c.lower():
      speak("opening")
      webbrowser.open("https://www.youtube.com")
  elif "open linkedin" in c.lower():
      speak("opening")
      webbrowser.open("https://www.linkedin.com")
  elif c.lower().startswith("play"):
      song=c.lower().split(" ")[1]
      link=musicLibrary.music[song]
      webbrowser.open(link)
  elif "headlines" in c.lower():
      r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsapi}")

      if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
                print(article['title'])
  else:
      pass

if __name__ == "__main__":
    speak("Initializing Alexa....")
    while True:
        # listen for wake word Alexa
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing..")
        # recognize speech using sphinx
        try:  
            with sr.Microphone() as source:
                print("Listening for wake word Alexa...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            print(f"You said: {word}")
            if(word.lower()=="alexa"):
                speak("Ya, how can i help you")
                
                # listen for command
                with sr.Microphone() as source:
                    print("Alexa Active....")
                    print("Listening for command...")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    print(f"Command: {command}")
                    
                    
                    processCommand(command)
                
        except Exception as e:
            print("Error: {0}".format(e))







