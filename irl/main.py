from soundInput import soundInput
from ncancel import nCancel

while True:
    input = soundInput()

    nCancel(soundInput)
