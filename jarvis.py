import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os


#install all below module in your terminal before running code
# pip install pyttsx3
# pip install pypiwin32.
# pip install speechRecognition
# pip install wikipedia

 #if you getting a pyaudio error run below commands in terminal
    #pip install pipwin
    #pipwin install pyaudio



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")
    elif hour>=12 and hour<17:
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")

    speak("I am Jarvis AI please Command me")
    

def takeCommand():
    # takeCommand It takes microphone input from the user and retuns string output
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said:{query}\n')

    except Exception as e:
        
        print("Say that again please...")
        return "None"
    return query
if __name__ == "__main__":
    greetings()
    
    while True:
        query = takeCommand().lower()

        # for executing tasks based on query

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
           
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'G:\\phone music\\English' #give your music folder path dont forget to add double forward slash
            songs = os.listdir(music_dir)

            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}") 


        elif 'open code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"  #give target path of your vs code go to properties in file location folder copy target path and paste it here
            os.startfile(codePath)



