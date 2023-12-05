import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_KEY = "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"

import openai
openai.api_key = OPENAI_KEY

def SpeakText(command):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    engine.say(command)
    engine.runAndWait()
    

r = sr.Recognizer()

def record_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("i'm listening")
                
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                
               
                return MyText
                    
                
               
            
        except sr.RequestError as e:
            print("could not request results: {0}".format(e))
        except sr.UnKnownValueError:
            print("unknown error occured")
            
def send_to_chatGPT(messages,model = "gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages = messages,y
        max_tokens = 100,
        n =1,
        stop = None,
        temperature = 0.5,
        
    )    
    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message

def shutDown():
    print("shutting down..")
    quit()


messages = [{"role":"user","content":"you are a personal assistant. Give them suggestion when they asking about places,hotels,travel routes and personal related stuffs"}]
while(1):
    text = record_text()
    if text == "shutdown" or text == "shut-down":
        shutDown()
    messages.append({"role":"user","content":text})
    response = send_to_chatGPT(messages)
    SpeakText(response)
    print(response)
    yn = input("do you need any image related to anything:(Y/N)=")
    if(yn.upper() == "Y"):
        user_prompt = input("enter the descrition to get your image(ai): ")

        response = openai.Image.create(
        prompt=user_prompt,
        n=1,
        size = '1024x1024'
        )

        webbrowser.open(response['data'][0]['url'])