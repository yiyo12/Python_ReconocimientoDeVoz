#!/usr/bin/env python3

# pip install SpeechRecognition

# https://pypi.python.org/pypi/SpeechRecognition/
# recognizer_instance.recognize_google(audio_data, key = None, language = "en-US", show_all = False)
# Performs speech recognition on audio_data (an AudioData instance), using the Google Speech Recognition API.
# The Google Speech Recognition API key is specified by key. If not specified, it uses a generic key that works out of the box.
# This should generally be used for personal or testing purposes only, as it may be revoked by Google at any time.

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr #importas la libreria, usas as como lo que es un operador de asignacion para el speech

# Para obtener el audio del micro
r = sr.Recognizer() #Metodo de reconocimiento de voz (es el bueno), contiene los demas metodos de la API a utilizar
with sr.Microphone() as source: #activa el microfono que se encuentra conectado y lo usa como entrada de audio
	print("Say something!")
	audio = r.listen(source) #convierte en un objeto el audio que entra por el microfono 

# recognize speech using Google Speech Recognition
try:
	# for testing purposes, we're just using the default API key
	# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	# instead of `r.recognize_google(audio)`
	print("Google Speech Recognition thinks you said in Spanis: -  " + r.recognize_google(audio, language = "es-MX"))#recognize_google devuelve el audio capturado y es convertido en texto
	
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(e))