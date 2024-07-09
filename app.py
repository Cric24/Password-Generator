from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Password generation route
@app.route('/generate_password', methods=['POST'])
def generate_password():
    # Get parameters from form submission
    length = int(request.form['length'])
    include_lowercase = 'lowercase' in request.form
    include_uppercase = 'uppercase' in request.form
    include_digits = 'digits' in request.form
    include_special = 'special' in request.form

    # Define character sets based on user input
    characters = ''
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    return render_template('result.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
