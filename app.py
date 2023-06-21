import json
import sqlite3
from flask import Flask, redirect, render_template, request, send_from_directory, url_for, send_static_file
from flask_cors import CORS

#ENTRYPOINT ["gunicorn", "app:app", "--bind", "0.0.0.0:5008", "--timeout", "10000"]


app = Flask(__name__)

CORS(app)

@app.route('/hello')
def hello():
   return render_template('hello.html')


if __name__ == '__main__':
   app.run(port=5010)

