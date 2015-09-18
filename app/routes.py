from flask import render_template, request, redirect, url_for, send_from_directory
from app import app, UPLOAD_DIRECTORY
from werkzeug import secure_filename
import os


# route to main page
@app.route('/')
def home():
  return render_template('main.html')

# posts user-uploaded image to server and stores it in /static/images directory
@app.route('/upload', methods=['POST'])
def upload():
  if request.method == 'POST':
    img_file = request.files['file']
    if img_file:
      # return secure version of filename
      filename = secure_filename(img_file.filename)
      # save img file to upload directory
      img_file.save(os.path.join(app.config['UPLOAD_DIRECTORY'], filename))
      return redirect( url_for('show_photo', file=filename) )

# renders image template
@app.route('/display/<file>')
def show_photo(file): 
  return render_template('photo.html', file=file)

# retrieves image from /static/images directory to render it to photo.html
@app.route('/upload/<file>')
def send_file(file): 
  return send_from_directory(UPLOAD_DIRECTORY, file)

if __name__ == '__main__':
  app.run(debug=True)