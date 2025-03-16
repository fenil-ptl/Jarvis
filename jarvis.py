import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
engine = pyttsx3.init('sapi5') # voice api by microsoft , it will collect our voice as input 
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    '''
    this function will speak the given audio
    '''
    engine.say(audio) # it will speak our sentace of speak in main function 
    engine.runAndWait()
    

def wishMe():
    '''
    this function will wish me , good morning , evening , afternoon  
    
    '''
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("  Good Morning ")

    elif hour<=12 and hour>=18:
        speak(" good Afternoon")    

    else:
        speak("  Good Evening ")
    
    speak(" I'm Jarvis Sir. Please tell me  how may i help you ")


def takecommand():
    '''
    it takes microphone input and return string output  


    '''

    r=sr.Recognizer()

    with  sr.Microphone() as source:
        print(" Listening... : ")
        r.pause_threshold=1

        audio=r.listen(source)

    try:
        print(" Recognizing... : ")
        query=r.recognize_google(audio,language='en-in')
        print(f'user said : {query}\n ')

    except Exception as e:
        # print(e)

        print(" say that again please ... ")
        return "None" # returning none string 
    
    return query
    
wishMe()

while True :
    query=takecommand().lower()

# logic for executing the task based on query 
    if 'wikipedia' in query:
        speak('Searching wikipedia.....')
        query=query.replace("Wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak(" According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open linkedin' in query:
        webbrowser.open("linkedin.com")
    
    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open github' in query:
        webbrowser.open("github.com")

    elif 'open gmail' in query:
        webbrowser.open("gmail.com")

    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir , the time is {strTime}")
        print(f"sir the time is {strTime}")

    elif 'open code' in query:
        codepath="C:\\Users\\Fenil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

    elif 'exit' or 'quit' in query:
        speak(" Thank you sir , have a good day !")
        exit()