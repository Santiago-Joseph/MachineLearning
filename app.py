from flask import Flask
from flask import render_template, request
from werkzeug.utils import redirect
from test import mushroom
import os

app = Flask(__name__,static_folder='static')
APP_ROOT=os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def aboutMushroomApp():
    return render_template('about.html')

@app.route("/classify")
def classifyMushroom():
    return render_template("classify.html")

@app.route("/upload",methods=["GET","POST"])
def upload():
    target = os.path.join(APP_ROOT, 'static/img/')
    if request.method == 'POST':
        file = request.files['img']
        filename = file.filename
        file.save("".join([target, filename]))
        print("upload Completed")
        return redirect('/classification/{}'.format(filename))

@app.route("/classification/<filename>",methods=["GET","POST"])
def prediction(filename):
    IMAGE_FOLDER = os.path.join('..','static','img')
    app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER
    print(filename)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    fullPath= "../" + full_filename
    x=mushroom()
    return render_template('output.html',results=x,image=full_filename)


if __name__ == "__main__":
    app.run()