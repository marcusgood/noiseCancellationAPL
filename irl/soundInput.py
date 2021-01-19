import pyaudio

def soundInput():
    p = pyaudio.PyAudio()
    format =




info = p.get_default_input_device_info()
print(info)
