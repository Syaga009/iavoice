import os
import numpy as np
import sounddevice as sd
from flask import Flask, request, render_template
app= Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')