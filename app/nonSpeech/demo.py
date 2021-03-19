import os
import matplotlib.pyplot as plt

#for loading and visualizing audio files
import librosa
import librosa.display

#to play audio
import IPython.display as ipd

audio_fpath = "audio/"
audio_clips = os.listdir(audio_fpath)


# Load "speech" and "non-speech" files and visualize its waveform (using librosa)
ns, sr = librosa.load(audio_fpath+audio_clips[1], sr=44100)
# s, sr = librosa.load(audio_fpath+audio_clips[2], sr=44100)
# t, sr = librosa.load(audio_fpath+audio_clips[3], sr=44100)


# print(s.shape, sr)

# print(ns.shape, sr)

# print(t.shape, sr)


plt.figure(figsize=(14, 5))
librosa.display.waveplot(ns, sr=sr)

# plt.figure(figsize=(14, 5))
# librosa.display.waveplot(s, sr=sr)

# plt.figure(figsize=(14, 5))
# librosa.display.waveplot(t, sr=sr)

# plt.ioff()
# plt.show()

#Convert the audio waveform to spectrogram

# NS = librosa.stft(ns)
# NSdb = librosa.amplitude_to_db(abs(NS))
# plt.figure(figsize=(14, 5))
# librosa.display.specshow(NSdb, sr=sr, x_axis='time', y_axis='log')
# plt.colorbar()

# S = librosa.stft(s)
# Sdb = librosa.amplitude_to_db(abs(S))
# plt.figure(figsize=(14, 5))
# librosa.display.specshow(Sdb, sr=sr, x_axis='time', y_axis='hz')
# plt.colorbar()

# T = librosa.stft(t)
# Tdb = librosa.amplitude_to_db(abs(T))
# plt.figure(figsize=(14, 5))
# librosa.display.specshow(Tdb, sr=sr, x_axis='time', y_axis='hz')
# plt.colorbar()

# plt.ioff()
# plt.show()

# Separate harmonics and percussives into two waveforms
# ns_harmonic, ns_percussive = librosa.effects.hpss(ns)
# s_harmonic, s_percussive = librosa.effects.hpss(s)
# t_harmonic, t_percussive = librosa.effects.hpss(s)

#waveform of percussives only
# plt.figure(figsize=(14, 5))
# librosa.display.waveplot(ns_percussive, sr=sr)
# plt.ioff()
# plt.show()

# plt.figure(figsize=(14, 5))
# librosa.display.waveplot(s_percussive, sr=sr)
# plt.ioff()
# plt.show()

# #zero-crossing-rate - x-axis is number of rolling windows of duration frame_length, beginning every hop_length
ns_zeros = librosa.feature.zero_crossing_rate(ns, frame_length=4096, hop_length=512)
plt.figure(figsize=(14, 5))
librosa.display.waveplot(ns, sr=sr)
plt.plot(ns_zeros[0])
plt.title("ZCR")
# plt.ioff()
# plt.show()
# print (ns_zeros)

#agglomerative segmentation by mel cepstrum
# ns_mfcc = librosa.feature.mfcc(ns)
# ns_segments = librosa.segment.agglomerative(ns_mfcc, 30)
# segment_times = librosa.frames_to_time(ns_segments, sr=sr)
# print (segment_times)
# plt.figure(figsize=(14,5))
# librosa.display.specshow(ns_mfcc, y_axis='mel', x_axis='time')
# plt.vlines(segment_times, 0, ns_mfcc.shape[1], color='linen', linestyle='--',
#            linewidth=2, alpha=0.9, label='Segment boundaries')
# plt.axis('tight')
# plt.legend(frameon=True, shadow=True)
# plt.title('Mean Frequency spectrogram')
# plt.tight_layout()
plt.show()