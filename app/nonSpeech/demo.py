import os
import matplotlib.pyplot as plt
import numpy

#for loading and visualizing audio files
import librosa
import librosa.display

#to play audio
import IPython.display as ipd

audio_fpath = "audio/"
audio_clips = os.listdir(audio_fpath)


# Load "speech" and "non-speech" files and visualize its waveform (using librosa)
ns, sr = librosa.load(audio_fpath+audio_clips[0], sr=44100)

# print(ns.shape, sr)

# plt.figure(figsize=(14, 5))
# librosa.display.waveplot(ns, sr=sr)

#Convert the audio waveform to spectrogram

# NS = librosa.stft(ns)
# NSdb = librosa.amplitude_to_db(abs(NS))
# plt.figure(figsize=(14, 5))
# librosa.display.specshow(NSdb, sr=sr, x_axis='time', y_axis='log')
# plt.colorbar()

# # Separate harmonics and percussives into two waveforms
# ns_harmonic, ns_percussive = librosa.effects.hpss(ns)

# #waveform of percussives only
# plt.figure(figsize=(14, 5))
# librosa.display.waveplot(ns_percussive, sr=sr)

# #zero-crossing-rate - x-axis is number of rolling windows of duration frame_length, beginning every hop_length
ns_zeros = librosa.feature.zero_crossing_rate(ns, frame_length=2048, hop_length=512)
# ns_zeros_scaled = numpy.divide(ns_zeros, 86.13) 
plt.figure(figsize=(14, 5))
# librosa.display.waveplot(ns, sr=sr)
plt.plot(ns_zeros[0])
plt.title("ZCR")
print(ns_zeros.min())
print(ns_zeros[0].min())
print(ns_zeros.max())
print(ns_zeros[0].max())


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