from flask import Flask, request,render_template, redirect
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')


app.run(debug=True)