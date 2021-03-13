# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:18:02 2021

@author: Marshall.McDougall
"""
import speech_recognition as sr
#from os import path
#from pydub import AudioSegment

# convert mp3 file to wav                                                       
#sound = AudioSegment.from_mp3("test.mp3")
#sound.export("test.wav", format="wav")
#HOUNDIFY_CLIENT_ID = "riarNlLoRaPRF-lxk9pobA=="
#HOUNDIFY_CLIENT_KEY = "LdfbAtRj97tnoWvzYpzPvHShoYG4L8z-FGrQjHNawDx42XBAivrpThxpFEkSzsYLTKJPnTwRIWJrulmMzBf02g=="

# transcribe audio file                                                         
AUDIO_FILE = "SimpleTest.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))