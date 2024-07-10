import speech_recognition 
import pyaudio
import pyttsx3

sr = speech_recognition.Recognizer()

def speakNow(command):
    print("command: ", command)
    voice = pyttsx3.init()
    voice.say(command)
    voice.runAndWait()


def s2t():
    with speech_recognition.Microphone() as source:
        print('Quite')
        sr.adjust_for_ambient_noise(source, duration = 2)
        print('Speak Now...')
        audio = sr.listen(source)

        try:
            text = sr.recognize_google(audio)
            text = text.lower()
            print("Did you say: ", text)
        except Exception as e:
            print("Errdo: ", str(e))
        return text
