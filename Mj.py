#imorting File
import cv2
import speech_recognition as sr
import pyttsx3
import datetime
import os
import pywhatkit as kit
import pyjokes
import wikipedia
import webbrowser
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from MjUi import Ui_MjUi




engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)


#text to voice
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# For Greeting
def greet():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your Virtual Assistant Mj. How Can help you?")


#Creating Threadclass
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExeceution()
        

    #voice to text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            
            audio = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User: {query}")

        except Exception as e:
            speak("Sorry! Please Say that again...")
            return "none"
        query = query.lower()
        return query

    #Task Handling
    def TaskExeceution(self):
        greet()
        while True:
            self.query = self.takecommand()
            #logic Query for Task

            if 'open command prompt' in self.query:
                os.system("start cmd")

            elif 'open notepad' in self.query:
                os.system("start notepads")


            elif "open youtube" in self.query:
                speak("what should I play?")
                cy = self.takecommand().lower()
                kit.playonyt(f"{cy}")

            elif "open github" in self.query:
                webbrowser.open("www.github.com")
                

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open instagram" in self.query:
                webbrowser.open("www.instagram.com")

            elif "open linkedin" in self.query:
                webbrowser.open("www.linkedin.com")

            elif "send a mail" in self.query:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")

            elif "open google" in self.query:
                speak("What should I serach for?")
                search = self.takecommand().lower()
                webbrowser.open(f"{search}")

            elif 'open camera' in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('camera', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif "play" in self.query:
                song = self.query.replace('play', '')
                speak('playing ' + song)
                kit.playonyt(song)

            elif "who are you" in self.query:
                speak("I am your Virtual Assistant. I am here to help you.")

            elif "where are you" in self.query:
                speak("I am hidden inside your system, but I am always here for you.")

            elif "can you dance" in self.query:
                speak("I love to, but you didn't gave me legs to dance with.")

            elif "today's date" in self.query:
                date = datetime.datetime.now().strftime("%B %d, %Y")
                speak("Today's date is " + date)

            elif 'time' in self.query:
                time = datetime.datetime.now().strftime('%H:%M %p')
                speak('Current time is ' + time)

            elif 'how are you' in self.query:
                speak("I am tickety-boo! How's your day going?")

            elif 'are you single' in self.query:
                speak('I am in relationship with your system')

            elif 'can you be my girlfriend' in self.query:
                speak(
                    'This is one of the thing we would both agree on. I would prefer to keep uor relation friendly. Rommance makes me incredibly awkward. ')

            elif 'joke' in self.query:
                speak(pyjokes.get_joke())

            elif "no thanks" in self.query:
                speak("Thanks for using me, Have a good day.")
                sys.exit()

            elif 'wikipedia' or 'search for' or 'who is' or 'what is' or 'where is' in self.query:
                want = self.query.replace('search for' or 'who is' or 'what is' or 'where is', '')
                info = wikipedia.summary(self.query, sentences=2)
                speak(info)




            speak("Anything else I can do for you")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MjUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)


    def startTask(self):
        self.ui.movie = QtGui.QMovie("lib/face.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

        
        

    
    def showText(self):
         text = speak
         self.ui.textBrowser.setText(text)



app = QApplication(sys.argv)
Mj = Main()
Mj.show()
exit(app.exec_())




