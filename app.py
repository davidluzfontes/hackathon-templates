from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    """Render the main page."""
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    """Handle file uploads and display them."""
    if request.method == 'POST':
        uploaded_files = request.files.getlist('file')
        filenames = []
        
        for file in uploaded_files:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            filenames.append(filename)
        
    return render_template("index.html", files=filenames)

if __name__ == "__main__":
    app.run(debug=True)
