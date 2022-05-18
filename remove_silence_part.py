import os
import shutil
from pydub import AudioSegment,silence
from pydub.silence import split_on_silence

# Crop silence part program in python

# Prerequisite:
# pip install pydub

# Description
# The sample project provide you an example to remove silence part in audios and save to new audios.
# Please put images in root directory.
# The generated new files stored in output folder

file_extension = ["wav"]
shutil.rmtree("output")
os.mkdir("output")

for entry in os.scandir('.'):
  if entry.is_file():
    filename = entry.name
    for ext in file_extension:
      if (filename.endswith("."+ext)):
        myaudio = AudioSegment.from_wav(filename)
        audio_chunks = split_on_silence(myaudio, min_silence_len=500, silence_thresh=-20)
        for i, chunk in enumerate(audio_chunks):
            chunk.export("output/"+filename.split(".")[0] + ".wav", format="wav")
