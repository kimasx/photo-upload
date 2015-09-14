from flask import Flask
app = Flask(__name__)

# define & config directory path to store uploaded images
UPLOAD_DIRECTORY = './static/images/'
app.config['UPLOAD_DIRECTORY'] = UPLOAD_DIRECTORY