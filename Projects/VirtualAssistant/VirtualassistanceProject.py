'''import gtts
from gtts import gTTS
text = 'Uppalapati Venkata Suryanarayana Prabhas Raju'

g= gTTS(text)

g.save('audio.mp3')
'''
'''
import gtts
from gtts import gTTS
import playsound
# now we give a text and convert to audio
text="Hello guys"
g=gTTS(text)
#save as audio file (mp3)
g.save('audio2.mp3')
playsound.playsound('audio2.mp3')
'''

#SpeechRecognition (STT) --> pip install SpeechRecognition

import gtts
from gtts import gTTS
import playsound
import speech_recognition as sr
from time import ctime #it returns current time
import os
import uuid

#Frist we will make our Virtual Assistant to understand what we speak

def listen():
    """SpeechRecogtion"""
    #we will make our system to check the microphone as source
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Now you can start talking")
        audio = r.listen(source,phrase_time_limit=5)
    #what ever we speak should store in data..
    data=""
    #now we will give our exception handiling to avoid any errors....
    try:
        data=r.recognize_google(audio,language="en-US")
        print("You said:",data)
    except sr.UnknownValueError:
        print("Make sure to speak Louder,so it can be audible")
    except sr.ReqestError as e :
        print("Request failed,please check your internet connection")
    return data
    """text = gTTS(data)
    text.save('new.mp3')
    playsound.playsound('new.mp3')
listen()
"""

#We will create seprate functions for responding back and virtual assistant
    #Actions

def respond(String):
    '''Responding function to get audio saved and text is spoken back '''
    print(String)
    tts=gTTS(text=String)
    #now we want only text to be modified in the audio file
    tts.save("Speech.mp3")
    #we use above audio file and modify the content in it
    filename="Speech%s.mp3"%str(uuid.uuid4())
    playsound.playsound(filename)
    os.remove(filename)
#next we will make our VirtualAssitant to function with the given conditions...
    
    
    
                            
        
