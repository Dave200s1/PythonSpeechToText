import speech_recognition as sr

speech_engine = sr.Recognizer()

def from_mircrophone():
    with sr.Microphone() as micro:
        audio = speech_engine.record(micro,duration=5 )
        print("Recording...")
        print("Recognized ;D")
        text = speech_engine.recognize_google(audio, language="bg-BG")
        return text
    
print(from_mircrophone())