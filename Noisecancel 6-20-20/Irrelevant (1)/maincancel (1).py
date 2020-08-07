from noicecancelLMS import lms_loop
from noise_inputs_goal import wave_measure
from noise_inputs_goal import output_goal
import time

while True: #Constantly loops this at 2 second intervals
   
    lms_loop(wave_measure, output_goal)

    time.sleep (2)