import os
import matplotlib.pyplot as plt

#for loading and visualizing audio files
import librosa
import librosa.display

#to play audio
import IPython.display as ipd

audio_fpath = "uploads/*.wav"
audio_clips = os.listdir(audio_fpath)

ns, sr = librosa.load(audio_fpath+audio_clips[1], sr=44100)

