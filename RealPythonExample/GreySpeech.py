# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 00:01:44 2020

@author: steve
"""

import speech_recognition as sr
sr.__version__


r = sr.Recognizer()
mic = sr.Microphone()
sr.Microphone.list_microphone_names()
mic = sr.Microphone(device_index=3)

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    
sentence = r.recognize_google(audio)
print(sentence)
