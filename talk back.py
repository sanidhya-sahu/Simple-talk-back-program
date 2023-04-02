import speech_recognition as s_r
import os

cmd = "pip install speechrecognition"
os.system(cmd)
print(s_r.__version__)  # just to print the version not required
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1)  # my device index is 1, you have to put your device index
while (True):
    with my_mic as source:
        print("Say now!!!!")
        # r.adjust_for_ambient_noise(source)  # reduce noise
        audio = r.listen(source)  # take voice input from the microphone
        try:
            x = r.recognize_google(audio)  # to print voice into text
        except:
            x = "unable to hear you"
    if x == "stop":
        print('stopped')

        break
    print(x)
    command = f'''  PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');'''
    os.system(command)
x = "Stopped hearing, bye bye!!"
command = f'''  PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');'''
os.system(command)
