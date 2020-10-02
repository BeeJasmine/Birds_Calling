import sys
import librosa  # python package for music and audio analysis
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau, ModelCheckpoint
import efficientnet.tfkeras as efn #Convolutional Neural Network architecture
from efficientnet.keras import center_crop_and_resize, preprocess_input
from sklearn.utils import class_weight


#tous les import OK! :)



#convert mp3 
from os import path
from pydub import AudioSegment

# files                                                                         
src = 'data/cygnus_cygnus/cygnus_cygnus.mp3'
dst = 'data/cygnus_cygnus/cygnus_cygnus.wav'

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")





SOUND_DIR='data/cygnus_cygnus/cygnus_cygnus.wav'
# listen to the recording
ipd.display(ipd.Audio(SOUND_DIR))

# load the mp3 file
signal, sr = librosa.load(SOUND_DIR,duration=10) # sr = sampling rate

# plot recording signal
plt.figure(figsize=(10, 4))
librosa.display.waveplot(signal, sr=sr)
plt.title('Monophonic')
plt.show()