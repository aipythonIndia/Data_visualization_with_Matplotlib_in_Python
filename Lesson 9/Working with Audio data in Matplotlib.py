#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import wave


# ### Reading audio file and display using matplotlib

# In[6]:


# This sample wav file is downloaded from University of Illinois (Computer Science Dept) webpage
# link (https://www2.cs.uic.edu/~i101/SoundFiles/)

# Specify file and read wav file
file_location = r"D:\Courses\Matplotlib_Python\Code\PinkPanther60.wav"
wav_data = wave.open(file_location, 'r')

sample_length = 352 * 1000 * 60   #bitrate 352kbps , audio length 60 seconds
read_file_at_sample = wav_data.readframes(sample_length)
sig1 = np.frombuffer(read_file_at_sample, dtype=np.int16)

get_ipython().run_line_magic('matplotlib', 'notebook')
plt.plot(sig1)
plt.xlabel('Sample rate * time')
plt.ylabel('Amplitude')
plt.title('Audio waveform', fontsize=14)


# ### Analyzing various audio properties

# In[3]:


file_location = r"D:\Courses\Matplotlib_Python\Code\PinkPanther60.wav"
wav_data = wave.open(file_location, 'r')

print ("Sampling Frequency of this audio file is: ", wav_data.getframerate(), "Hz")
print ("Number of channels in this audio file is: ", wav_data.getnchannels())
print ("Total number of audio frames in this audio file is: ", wav_data.getnframes())
print ("Current reading position for this audio file: ", wav_data.tell(),'s')


# ### Slicing a sample length from the beginning

# In[5]:


# Removing below magic function will plot in the original figure (shown above)
get_ipython().run_line_magic('matplotlib', 'notebook')

file_location = r"D:\Courses\Matplotlib_Python\Code\PinkPanther60.wav"
wav_data = wave.open(file_location, 'r')

sample_length = 100 * 1000
read_file_at_sample = wav_data.readframes(sample_length)
sig1 = np.frombuffer(read_file_at_sample, dtype=np.int16)


plt.plot(sig1, 'r')
plt.xlabel('Sample rate * time')
plt.ylabel('Amplitude')
plt.title('Partial Audio waveform', fontsize=14)


# ### Slicing intermediate range

# In[7]:


get_ipython().run_line_magic('matplotlib', 'notebook')

file_location = r"D:\Courses\Matplotlib_Python\Code\PinkPanther60.wav"
wav_data = wave.open(file_location, 'r')


#Selecting specific raneg from the signal
wav_data.setpos(100000)
read_file_at_sample = wav_data.readframes(700000)
sig2 = np.frombuffer(read_file_at_sample, dtype=np.int16)

plt.plot(sig2, 'r')
plt.xlabel('Sample rate * time')
plt.ylabel('Amplitude')
plt.title('Customed range Audio waveform', fontsize=14)


# ### Plotting a spectogram of the signal (Frequency domain)

# In[8]:


get_ipython().run_line_magic('matplotlib', 'notebook')

file_location = r"D:\Courses\Matplotlib_Python\Code\PinkPanther60.wav"
wav_data = wave.open(file_location, 'r')

sample_length = 352 * 1000 * 60
read_file_at_sample = wav_data.readframes(sample_length)
sig1 = np.frombuffer(read_file_at_sample, dtype=np.int16)

plt.specgram(sig1, NFFT=1024, Fs= 2, noverlap = 256, scale= 'dB')


# In[ ]:




