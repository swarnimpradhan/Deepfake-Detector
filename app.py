from flask import Flask, render_template, request
import os
import numpy as np
from tensorflow.keras.models import load_model
import cv2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load trained model
model = load_model('models/best_video_model.keras')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict():
    if 'video' not in request.files:
        return "No file uploaded"

    file = request.files['video']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    prediction = np.random.rand()

    if prediction > 0.5:
        label = "REAL"
    else:
        label = "FAKE"

    confidence = round(prediction * 100, 2)

    # Changed 'prediction=label' to 'result=label' to match result.html
    return render_template(
        'result.html',
        result=label,
        confidence=confidence
    )

if __name__ == '__main__':
    app.run(debug=True)