from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_password():
    length = int(request.form['length'])

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbol = string.punctuation

    all_chars = lower + upper + num + symbol

    password_list = random.sample(all_chars, length)
    password = ''.join(password_list)

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
