import numpy as np
import simpleaudio as sa
from math import *
# calculate note frequencies
freq  = 1200


# get timesteps for each sample, T is note duration in seconds
sample_rate = 44100
T = 20
t = np.linspace(0, T, int(T * sample_rate), False)

# generate sine wave notes
note = []
for x in t:
    freq = (x/T)*2000 + 1000
    y = cos(2500*x)+sin(1200*x)
    note.append(y)

audio_data = np.array(note)
# concatenate notes
audio = np.hstack((audio_data))
# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

# wait for playback to finish before exiting
play_obj.wait_done()