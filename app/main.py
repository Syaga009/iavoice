import os
import numpy as np
import sounddevice as sd
import soundfile as sf
from tensorflow import keras
import librosa
import audioread
from flask import Flask, request, render_template
app= Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')
if __name__ == '__main__':
  app.run()