import os
import numpy as np
import sounddevice as sd
import soundfile as sf
from tensorflow import keras
import librosa
import audioread
from flask import Flask, request, jsonify, render_template
app= Flask(__name__)

model = keras.models.load_model('final_model.h5')

emotions = ['Agradecimiento', 'Ansiedad', 'Curiosidad', 'Expectativa', 'Felicidad', 'Seguridad', 'Tranquilidad']

def preprocess_audio(audio_path):
    if not os.path.exists(audio_path):
        return None
    try:
        with sf.SoundFile(audio_path) as f:
            sr = f.samplerate
            audio = f.read(dtype='float32')
        audio /= np.max(np.abs(audio))
        mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
        if mfcc.shape[1] > 100:
            mfcc = mfcc[:, :100]
        else:
            mfcc = np.pad(mfcc, ((0, 0), (0, 100 - mfcc.shape[1])), mode='constant')
        mfcc = np.expand_dims(mfcc, axis=0)
        mfcc = np.expand_dims(mfcc, axis=-1)
        return mfcc
    except Exception as e:
        print(f"Error al procesar el archivo de audio: {e}")
        return None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'wav'}

@app.route('/')
def index():
  return ('index.html')



